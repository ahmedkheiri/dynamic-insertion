# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 11:10:37 2022

@author: Ahmed Kheiri
"""

from Customer import Customer
from Depot import Depot

class Vehicle:
    def __init__(self,depot):
        self.__depot = depot
        self.__customer_visits = []
    
    def getDepot(self) -> Depot:
        return self.__depot
    def getCustomerVisit(self, index) -> Customer:
        return self.__customer_visits[index]
    def getCustomerVisitsList(self):
        return self.__customer_visits
    def insertCustomerVisit(self, visit_index, customer):
        self.__customer_visits.insert(visit_index, customer)
    def deleteCustomerVisit(self, visit_index):
        self.__customer_visits.pop(visit_index)
    def getNumberOfCustomerVisits(self):
        return len(self.__customer_visits)
    def getTotalDistance(self):
        if self.getNumberOfCustomerVisits() == 0:
            return 0
        totalDist = 0
        for i in range(self.getNumberOfCustomerVisits() - 1):
            totalDist += ((self.getCustomerVisit(i).getX() - self.getCustomerVisit(i+1).getX()) ** 2 + (self.getCustomerVisit(i).getY() - self.getCustomerVisit(i+1).getY()) ** 2) ** 0.5
        totalDist += ((self.getCustomerVisit(0).getX() - self.getDepot().getX()) ** 2 + (self.getCustomerVisit(0).getY() - self.getDepot().getY()) ** 2) ** 0.5
        totalDist += ((self.getCustomerVisit(self.getNumberOfCustomerVisits() - 1).getX() - self.getDepot().getX()) ** 2 + (self.getCustomerVisit(self.getNumberOfCustomerVisits() - 1).getY() - self.getDepot().getY()) ** 2) ** 0.5
        return totalDist

    def __str__(self):
        return "Total Distance: {}, Visits: {}".format(self.getTotalDistance(), self.__customer_visits)
    def __repr__(self):
        return self.__str__()
