# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 11:10:37 2022

@author: Ahmed Kheiri
"""

from Solution import Solution
from Problem import Problem
import random

class LocalSearch:
    def __init__(self, number_of_iterations_factor, sumOfSquaresObjective):
        self.__number_of_iterations_factor = number_of_iterations_factor
        self.__sumOfSquaresObjective = sumOfSquaresObjective

    def setProblem(self, problem):
        self.__problem = problem
    def setSolution(self, solution):
        self.__solution = solution
    def isSumOfSquaresObjective(self):
        return self.__sumOfSquaresObjective
    def getNumberOfIterationsFactor(self):
        return self.__number_of_iterations_factor
    def getProblem(self) -> Problem:
        return self.__problem
    def getSolution(self) -> Solution:
        return self.__solution
    
    def getCopySolution(self):
        return self.getSolution().copy()
    def copyFrom(self, sol):
        self.getSolution().setVehiclesList(sol.getVehiclesList())
    
    def improve(self):
        pass
    
    ########################### Objectives Section
    
    def getFeasibility(self):
        feas = 0
        for current_vehicle in range(self.getSolution().getNumberOfVehicles()):
            if self.getProblem().getConstraintType() == "DC":
                feas += max(0,self.getSolution().getVehicle(current_vehicle).getTotalDemand() - self.getSolution().getVehicle(current_vehicle).getCapacity())
            elif self.getProblem().getConstraintType() == "DD":
                feas += max(0,self.getSolution().getVehicle(current_vehicle).getTotalDistance() -  self.getProblem().getOptimalObj()/self.getProblem().getM())
        return feas
    
    def getObjective(self, w1=100000000, w2=100000, w3=1):
        if self.isSumOfSquaresObjective():
            return w1*self.getFeasibility() + w2*self.getSolution().getSolutionNumberOfSatisfiedCustomers() + w3*self.getSolution().getSolutionSquaredTotalDistance()
        else:
            return w1*self.getFeasibility() + w2*self.getSolution().getSolutionNumberOfSatisfiedCustomers() + w3*self.getSolution().getSolutionTotalDistance()
            
    
    ########################### LLHs Section
    
    def getNumberOfLLHs(self):
        return 4
    
    def applyLLH(self, llh):
        if llh == 0:
            self.SwapCustomersDifferentVehicles()
        elif llh == 1:
            self.InsertCustomerDifferentVehicle()
        elif llh == 2:
            self.SwapCustomersSameVehicle()
        elif llh == 3:
            self.InsertCustomerSameVehicle()
            
    def SwapCustomersSameVehicle(self):
        if self.getSolution().getNumberOfVehicles() <= 0:
            return
        
        vehicle = random.randint(0, self.getSolution().getNumberOfVehicles()-1)
        if self.getSolution().getVehicle(vehicle).getNumberOfCustomerVisits() <= 1:
            return
        
        customer1 = random.randint(0, self.getSolution().getVehicle(vehicle).getNumberOfCustomerVisits() - 1)
        customer2 = random.randint(0, self.getSolution().getVehicle(vehicle).getNumberOfCustomerVisits() - 1)
        self.getSolution().getVehicle(vehicle).getCustomerVisitsList()[customer1], self.getSolution().getVehicle(vehicle).getCustomerVisitsList()[customer2] = self.getSolution().getVehicle(vehicle).getCustomerVisitsList()[customer2], self.getSolution().getVehicle(vehicle).getCustomerVisitsList()[customer1]
    
    def SwapCustomersDifferentVehicles(self):
        if self.getSolution().getNumberOfVehicles() <= 0:
            return
        vehicle1 = random.randint(0, self.getSolution().getNumberOfVehicles()-1)
        
        if self.getSolution().getVehicle(vehicle1).getNumberOfCustomerVisits() <= 0:
            return
        
        vehicle2 = random.randint(0, self.getSolution().getNumberOfVehicles()-1)
        
        if self.getSolution().getVehicle(vehicle2).getNumberOfCustomerVisits() <= 0:
            return
        
        customer1 = random.randint(0, self.getSolution().getVehicle(vehicle1).getNumberOfCustomerVisits() - 1)
        customer2 = random.randint(0, self.getSolution().getVehicle(vehicle2).getNumberOfCustomerVisits() - 1)
        self.getSolution().getVehicle(vehicle1).getCustomerVisitsList()[customer1], self.getSolution().getVehicle(vehicle2).getCustomerVisitsList()[customer2] = self.getSolution().getVehicle(vehicle2).getCustomerVisitsList()[customer2], self.getSolution().getVehicle(vehicle1).getCustomerVisitsList()[customer1]
        
    def InsertCustomerSameVehicle(self):
        if self.getSolution().getNumberOfVehicles() <= 0:
            return
        
        vehicle = random.randint(0, self.getSolution().getNumberOfVehicles()-1)
        
        if self.getSolution().getVehicle(vehicle).getNumberOfCustomerVisits() <= 1:
            return
        
        current_index = random.randint(0, self.getSolution().getVehicle(vehicle).getNumberOfCustomerVisits() - 1)
        new_index = random.randint(0, self.getSolution().getVehicle(vehicle).getNumberOfCustomerVisits() - 1)
        
        element = self.getSolution().getVehicle(vehicle).getCustomerVisitsList().pop(current_index)
        self.getSolution().getVehicle(vehicle).getCustomerVisitsList().insert(new_index, element)
        
    def InsertCustomerDifferentVehicle(self):
        if self.getSolution().getNumberOfVehicles() <= 0:
            return

        vehicle1 = random.randint(0, self.getSolution().getNumberOfVehicles()-1)
        
        if self.getSolution().getVehicle(vehicle1).getNumberOfCustomerVisits() <= 0:
            return
        
        vehicle2 = random.randint(0, self.getSolution().getNumberOfVehicles()-1)
        
        current_index = random.randint(0, self.getSolution().getVehicle(vehicle1).getNumberOfCustomerVisits() - 1)
        
        new_index = random.randint(0, self.getSolution().getVehicle(vehicle2).getNumberOfCustomerVisits())
        
        element = self.getSolution().getVehicle(vehicle1).getCustomerVisitsList().pop(current_index)
        self.getSolution().getVehicle(vehicle2).getCustomerVisitsList().insert(new_index, element)
        
        