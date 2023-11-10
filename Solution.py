# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 11:10:37 2022

@author: Ahmed Kheiri
"""
from Vehicle import Vehicle
import copy
import numpy as np
import matplotlib.pyplot as plt

class Solution:
    def __init__(self, vehicles=None):
        if vehicles is None:
            vehicles = []
        self.__vehicles = vehicles

    # Create a new instance with the same vehicles - needed for the local solver
    def copy(self):
        return copy.deepcopy(self)
    def setVehiclesList(self, vehicles_list):
        self.__vehicles = copy.deepcopy(vehicles_list)
    def getVehiclesList(self):
        return self.__vehicles    
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
    
    def DrawSolution(self):

        color = plt.cm.rainbow(np.linspace(0, 1, self.getNumberOfVehicles()))
        count = 1
        plt.figure(figsize=(8, 6), dpi=80)
        for route, c in zip(self.getVehiclesList(), color):
            xs = [route.getCustomerVisit(x).getX() for x in range(route.getNumberOfCustomerVisits())]
            ys = [route.getCustomerVisit(x).getY() for x in range(route.getNumberOfCustomerVisits())]
            plt.scatter(self.getVehicle(0).getDepot().getX(), self.getVehicle(0).getDepot().getY(),color='red',marker='.', s=100)
            plt.scatter(xs, ys,color=c,label="Vehicle" + str(count),marker='.',s=100)
            plt.plot(xs, ys,c=c)
            xs = [xs[0], self.getVehicle(0).getDepot().getX(), xs [-1]]
            ys = [ys[0], self.getVehicle(0).getDepot().getY(), ys [-1]]
            plt.plot(xs, ys,c=c,linestyle='dashed')
            count+=1 
        plt.grid()
        plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
        plt.tight_layout()
        plt.show()    
    
    def __str__(self):
        return "Sol Satisfied Customers: {}\nSol Total Dist: {}\nSol Total Demand: {}\nSol Number Of Vehicles: {}\nVehicles: {}\n".format(self.getSolutionNumberOfSatisfiedCustomers(), self.getSolutionTotalDistance(), self.getSolutionTotalDemand(), self.getNumberOfVehicles(), self.__vehicles)
