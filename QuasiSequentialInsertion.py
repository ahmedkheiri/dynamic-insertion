# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 11:10:37 2022

@author: Ahmed Kheiri
"""

from Solver import Solver
from Vehicle import Vehicle

class QuasiSequentialInsertion(Solver):
    def solve(self):
        current_customer = 0
        current_vehicle = 0
        self.getSolution().setVehicle(Vehicle(self.getProblem().getQ(), self.getProblem().getDepot()))
        
        keep_track = self.getSolution().getSolutionNumberOfSatisfiedCustomers()
        while True:
            best_loc = -1
            best_obj = 1000000000000
            for j in range(self.getSolution().getVehicle(current_vehicle).getNumberOfCustomerVisits() + 1):
                self.getSolution().getVehicle(current_vehicle).insertCustomerVisit(j, self.getProblem().getCustomer(current_customer))
                # "DC" constraint
                if (self.getProblem().getConstraintType() == "DC") and (self.getSolution().getVehicle(current_vehicle).getTotalDemand() <= self.getSolution().getVehicle(current_vehicle).getCapacity()):
                    if self.getSolution().getVehicle(current_vehicle).getTotalDistance() < best_obj:
                        best_loc = j
                        best_obj = self.getSolution().getVehicle(current_vehicle).getTotalDistance()
                # "DD" conatrint    
                elif (self.getProblem().getConstraintType() == "DD") and (self.getSolution().getVehicle(current_vehicle).getTotalDistance() <=  self.getProblem().getOptimalObj()/self.getProblem().getM()):
                    if self.getSolution().getVehicle(current_vehicle).getTotalDistance() < best_obj:
                        best_loc = j
                        best_obj = self.getSolution().getVehicle(current_vehicle).getTotalDistance()
                        
                        
                self.getSolution().getVehicle(current_vehicle).deleteCustomerVisit(j)
            if best_loc != -1:
                self.getSolution().getVehicle(current_vehicle).insertCustomerVisit(best_loc, self.getProblem().getCustomer(current_customer))
                current_customer += 1
                current_vehicle = 0
                if current_customer >= self.getProblem().getNumberOfCustomers():
                    break
            else:
                current_vehicle += 1
                if current_vehicle >= self.getSolution().getNumberOfVehicles():
                    
                    if self.getSolution().getNumberOfVehicles() < self.getProblem().getM():
                        self.getSolution().setVehicle(Vehicle(self.getProblem().getQ(), self.getProblem().getDepot()))
                    else:
                        current_customer += 1
                        current_vehicle = 0
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