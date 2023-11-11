# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 11:10:37 2022

@author: Ahmed Kheiri
"""

from Solver import Solver
from Vehicle import Vehicle

class SequentialInsertion(Solver):
    def getCustomerDistanceToDepot(self, customer_index):
        return ((self.getProblem().getCustomer(customer_index).getX() - self.getProblem().getDepot().getX()) ** 2 + (self.getProblem().getCustomer(customer_index).getY() - self.getProblem().getDepot().getY()) ** 2) ** 0.5
    
    def solve(self):
        current_vehicle = 0
        current_customer = 0
        self.getSolution().setVehicle(Vehicle(self.getProblem().getDepot()))
        
        keep_track = self.getSolution().getSolutionNumberOfSatisfiedCustomers()
        while True:
            best_loc = -1
            best_obj = 1000000000000
            
            if self.getCustomerDistanceToDepot(current_customer) * 2 >  self.getProblem().getD():
                current_customer += 1
                if current_customer >= self.getProblem().getNumberOfCustomers():
                    break
                continue
            
            for j in range(self.getSolution().getVehicle(current_vehicle).getNumberOfCustomerVisits() + 1):
                self.getSolution().getVehicle(current_vehicle).insertCustomerVisit(j, self.getProblem().getCustomer(current_customer))
                if self.getSolution().getVehicle(current_vehicle).getTotalDistance() <=  self.getProblem().getD():
                    if self.getSolution().getVehicle(current_vehicle).getTotalDistance() < best_obj:
                        best_loc = j
                        best_obj = self.getSolution().getVehicle(current_vehicle).getTotalDistance()
                self.getSolution().getVehicle(current_vehicle).deleteCustomerVisit(j)
            if best_loc != -1:
                self.getSolution().getVehicle(current_vehicle).insertCustomerVisit(best_loc, self.getProblem().getCustomer(current_customer))
                current_customer += 1
                if current_customer >= self.getProblem().getNumberOfCustomers():
                    break
            else:
                if self.getSolution().getNumberOfVehicles() < self.getProblem().getM():
                    current_vehicle += 1
                    self.getSolution().setVehicle(Vehicle(self.getProblem().getDepot()))
                else:
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