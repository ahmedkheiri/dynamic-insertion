# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 11:10:37 2022

@author: Ahmed Kheiri
"""

import pandas as pd
from Depot import Depot
from Customer import Customer
import random

class Problem:
    def __init__(self, file_name, m, Q, isDepotFirst, optimalObj, instanceName, constraintType):
        self.__file_name = file_name
        self.__customers = []
        self.__m= m
        self.__Q = Q
        self.__depot = None
        self.__constraintType = constraintType
        self.__instanceName = instanceName
        self.__optimalObj = optimalObj
        assert(constraintType == "DC" or constraintType == "DD")
             
        df = pd.read_table(self.getFileName())
        cust_start = 0
        cust_end = len(df)-1
        dep = len(df)-1
        if isDepotFirst:
            cust_start += 1
            cust_end += 1
            dep = 0
        for i in range(cust_start,cust_end):
            c = df.iloc[i][0].split(" ")
            demand = 1
            self.setCustomer(Customer(int(c[0]), float(c[1]),float(c[2]),demand))
        d = df.iloc[dep][0].split(" ")
        self.setDepot(Depot(int(d[0]), float(d[1]),float(d[2])))
        
    def getFileName(self):
        return self.__file_name
    def getInstanceName(self):
        return self.__instanceName
    def getConstraintType(self):
        return self.__constraintType
    def getOptimalObj(self):
        return self.__optimalObj
    def getM(self):
        return self.__m
    def getQ(self):
        return self.__Q
    def getDepot(self) -> Depot:
        return self.__depot
    def setDepot(self, depot):
        self.__depot = depot
    def getCustomer(self, index) -> Customer:
        return self.__customers[index]
    def setCustomer(self, customer):
        self.__customers.append(customer)
    def getNumberOfCustomers(self):
        return len(self.__customers)
    def shuffleOrders(self, seed):
        random.seed(seed)
        random.shuffle(self.__customers)