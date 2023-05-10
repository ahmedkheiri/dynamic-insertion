# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 11:10:37 2022

@author: Ahmed Kheiri
"""

from Vehicle import Vehicle

class Solution:
    def __init__(self):
        self.__vehicles = []
    def getVehicle(self, index) -> Vehicle:
        return self.__vehicles[index]
    def setVehicle(self, vehicle):
        self.__vehicles.append(vehicle)
    def getNumberOfVehicles(self):
        return len(self.__vehicles)
    def getNumberOfVehiclesUsed(self):
        totalVehUsed = 0
        for i in range(self.getNumberOfVehicles()):
            if self.getVehicle(i).getNumberOfCustomerVisits() > 0:
                totalVehUsed += 1
        return totalVehUsed
    def getSolutionTotalDistance(self):
        totalDistance = 0
        for i in range(self.getNumberOfVehicles()):
            totalDistance += self.getVehicle(i).getTotalDistance()
        return totalDistance
    def getSolutionSquaredTotalDistance(self):
        totalDistance = 0
        for i in range(self.getNumberOfVehicles()):
            totalDistance += self.getVehicle(i).getTotalDistance()**2
        return totalDistance
    def getSolutionTotalDemand(self):
        totalDemand = 0
        for i in range(self.getNumberOfVehicles()):
            totalDemand += self.getVehicle(i).getTotalDemand()
        return totalDemand
    def getSolutionNumberOfSatisfiedCustomers(self):
        total = 0
        for i in range(self.getNumberOfVehicles()):
            total += self.getVehicle(i).getNumberOfCustomerVisits()
        return total
    def __str__(self):
        return "Sol Satisfied Customers: {}\n\nSol Total Dist: {}\n\nSol Total Demand: {}\n\nSol Number Of Vehicles: {}\n\nVehicles: {}".format(self.getSolutionNumberOfSatisfiedCustomers(), self.getSolutionTotalDistance(), self.getSolutionTotalDemand(), self.getNumberOfVehicles(), self.__vehicles)
