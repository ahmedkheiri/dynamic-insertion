# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 11:10:37 2022

@author: Ahmed Kheiri
"""

from Solver import Solver
from Vehicle import Vehicle

class ParallelInsertionWithSeeds(Solver):
    def solve(self):
        current_customer = 0
        self.getSolution().setVehicle(Vehicle(self.getProblem().getDepot()))
        
        keep_track = self.getSolution().getSolutionNumberOfSatisfiedCustomers()
        while True:
            best_loc = -1
            best_veh = -1
            best_obj = 1000000000000
            for veh in range(self.getSolution().getNumberOfVehicles()):
                
                #quick check to see if there is an empty vehicle
                empty_vehicle_exists = False
                for q_veh in range(self.getSolution().getNumberOfVehicles()):
                    if self.getSolution().getVehicle(q_veh).getNumberOfCustomerVisits() == 0:
                        empty_vehicle_exists = True
                        break
                
                if empty_vehicle_exists:
                    if self.getSolution().getVehicle(veh).getNumberOfCustomerVisits() > 0:
                        continue
                
                for j in range(self.getSolution().getVehicle(veh).getNumberOfCustomerVisits() + 1):
                    self.getSolution().getVehicle(veh).insertCustomerVisit(j, self.getProblem().getCustomer(current_customer))
                    if self.getSolution().getVehicle(veh).getTotalDistance() <=  self.getProblem().getD():
                        if self.getSolution().getSolutionTotalDistance() < best_obj:
                            best_loc = j
                            best_veh = veh
                            best_obj = self.getSolution().getSolutionTotalDistance()
                    self.getSolution().getVehicle(veh).deleteCustomerVisit(j)
            if best_loc != -1:
                self.getSolution().getVehicle(best_veh).insertCustomerVisit(best_loc, self.getProblem().getCustomer(current_customer))
            if self.getSolution().getVehicle(self.getSolution().getNumberOfVehicles() - 1).getNumberOfCustomerVisits() != 0:
                if self.getSolution().getNumberOfVehicles() < self.getProblem().getM():
                    self.getSolution().setVehicle(Vehicle(self.getProblem().getDepot()))
            current_customer += 1
            if current_customer >= self.getProblem().getNumberOfCustomers():
                break
            
            if self.getNumberOfCustomersToApplyLS() != 0:
                if self.getSolution().getSolutionNumberOfSatisfiedCustomers() % self.getNumberOfCustomersToApplyLS() == 0:
                    if keep_track != self.getSolution().getSolutionNumberOfSatisfiedCustomers():
                        self.increaseNumberOfTimeLSIsCalled()
                        self.getLocalSearch().improve()
                        keep_track = self.getSolution().getSolutionNumberOfSatisfiedCustomers()
        
        if self.getNumberOfCustomersToApplyLS() != 0:
            self.increaseNumberOfTimeLSIsCalled()
            self.getLocalSearch().improve()