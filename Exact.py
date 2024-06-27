# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 11:10:37 2022

@author: Ahmed Kheiri

Implementation of Adam Letchford's UB model

# before applying the upper-bounding procedure to a given instance, you will 
# need to remove any customers such that t_{0i} > T/2. (Such customers could 
# never be served, since it would take a vehicle longer than T units of time 
# just to travel from the depot to the customer and back

"""

from Solver import Solver
from Vehicle import Vehicle
import pulp

class Exact(Solver):
    def solve(self):
        # Create the problem instance
        prob = pulp.LpProblem("ExactModel", pulp.LpMaximize)
        
        # Parameters
        n = self.getProblem().getNumberOfCustomers()   # Number of customers
        m = self.getProblem().getM()   # Number of vehicles
        T = self.getProblem().getD()   # Time limit
        
        # Calculate travel times from depot to each customer
        t_depot_to_customer = []
        for j in range(1, n + 1):
            travel_time = ((self.getProblem().getDepot().getX() - self.getProblem().getCustomer(j - 1).getX()) ** 2 + 
                           (self.getProblem().getDepot().getY() - self.getProblem().getCustomer(j - 1).getY()) ** 2) ** 0.5
            t_depot_to_customer.append((j, travel_time))
        
        # Filter out customers with travel time greater than T/2
        filtered_customers = [j for j, travel_time in t_depot_to_customer if travel_time <= T / 2]
        
        # Update number of customers
        n = len(filtered_customers)
        
        s = [0 for _ in range(n + 1)]  # Service time at each node
        
        # Initialise travel time array t
        t = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        for i in range(n + 1):
            for j in range(n + 1):
                if i == 0:  # From depot to customers
                    if j > 0:
                        t[i][j] = ((self.getProblem().getDepot().getX() - self.getProblem().getCustomer(filtered_customers[j - 1] - 1).getX()) ** 2 + 
                                   (self.getProblem().getDepot().getY() - self.getProblem().getCustomer(filtered_customers[j - 1] - 1).getY()) ** 2) ** 0.5
                elif j == 0:  # From customers to depot
                    if i > 0:
                        t[i][j] = ((self.getProblem().getCustomer(filtered_customers[i - 1] - 1).getX() - self.getProblem().getDepot().getX()) ** 2 + 
                                   (self.getProblem().getCustomer(filtered_customers[i - 1] - 1).getY() - self.getProblem().getDepot().getY()) ** 2) ** 0.5
                else:  # Between customers
                    t[i][j] = ((self.getProblem().getCustomer(filtered_customers[i - 1] - 1).getX() - self.getProblem().getCustomer(filtered_customers[j - 1] - 1).getX()) ** 2 + 
                               (self.getProblem().getCustomer(filtered_customers[i - 1] - 1).getY() - self.getProblem().getCustomer(filtered_customers[j - 1] - 1).getY()) ** 2) ** 0.5
        
        # Define the binary variables x_ij
        x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n + 1) for j in range(n + 1)), cat='Binary')
        
        # Define the continuous variables f_ij
        f = pulp.LpVariable.dicts("f", ((i, j) for i in range(n + 1) for j in range(n + 1)), lowBound=0, cat='Continuous')
        
        # Define the binary variables y_i
        y = pulp.LpVariable.dicts("y", (i for i in range(1, n + 1)), cat='Binary')
        
        # Objective function: maximise the number of satisfied customers
        prob += pulp.lpSum([y[i] for i in range(1, n + 1)])
        
        # Constraints
        # Constraint (1): Sum of vehicles starting from depot equals m
        prob += pulp.lpSum([x[0, i] for i in range(1, n + 1)]) == m
        
        # Constraints (2) and (3): For each customer, exactly one vehicle arrives and departs
        for i in range(1, n + 1):
            prob += pulp.lpSum([x[i, j] for j in range(n + 1) if j != i]) == y[i]
            prob += pulp.lpSum([x[j, i] for j in range(n + 1) if j != i]) == y[i]
        
        # Constraint (4): f
        for i in range(1, n + 1):
            prob += pulp.lpSum([f[i, j] for j in range(n + 1) if j != i]) >= \
                    pulp.lpSum([f[j, i] for j in range(n + 1) if j != i]) + pulp.lpSum([t[j][i] * x[j, i] for j in range(n + 1) if j != i]) + s[i] * y[i]
        
        # Constraint (5-7): Bounds on the f variables
        for i in range(n + 1):
            for j in range(1, n + 1):
                if i != j:
                    prob += f[i, j] <= T * x[i, j]
        
        for i in range(1, n + 1):
            prob += f[i, 0] <= (T - t[i][0]) * x[i, 0]
        
        # Constraints (8) and (9): Binary conditions
        for i in range(n + 1):
            for j in range(n + 1):
                if i != j:
                    prob += x[i, j] >= 0
                    prob += x[i, j] <= 1
        
        for i in range(1, n + 1):
            prob += y[i] >= 0
            prob += y[i] <= 1
        
        # Strengthened time bounds
        for i in range(1, n + 1):
            for j in range(n + 1):
                if j != i:
                    prob += f[i, j] >= (t[0][i] + s[i]) * x[i, j]
                    
        for i in range(n + 1):
            for j in range(1, n + 1):
                if j != i:
                    prob += f[i, j] <= (T - t[i][j] - s[j] - t[j][0]) * x[i, j]
        
        prob.solve(pulp.GUROBI(msg=0, timeLimit=2*60*60))
        
        # Output the results
        print(f"Status: {pulp.LpStatus[prob.status]}")
        print(f"Objective value: {pulp.value(prob.objective)}")
        print(f"Upper Bound = {pulp.value(prob.solverModel.ObjBound)}")
        print(f"Lower Bound = {pulp.value(prob.solverModel.ObjVal)}")
        print(f"GAP = {pulp.value(prob.solverModel.MIPGap)}")
        
        # Create a list to store the routes for each vehicle
        routes = [[] for _ in range(m)]
        
        # Extract the routes from the solution
        for v in range(m):
            curr_vehicle = v
            current_node = 0
            route = []
            while True:
                next_node = None
                for j in range(1, n + 1):
                    if pulp.value(x[current_node, j]) == 1:
                        if curr_vehicle != 0:
                            curr_vehicle -= 1
                            continue
                        next_node = j
                        route.append(next_node)
                        current_node = next_node
                        break
                if next_node is None:
                    break
            routes[v] = route
        
        #print("Test", routes)
        
        # Set the solution
        for v in range(m):
            if routes[v]:
                vehicle = Vehicle(self.getProblem().getDepot())
                for customer in routes[v]:
                    vehicle.insertCustomerVisit(vehicle.getNumberOfCustomerVisits(), self.getProblem().getCustomer(filtered_customers[customer - 1] - 1))
                self.getSolution().setVehicle(vehicle)
