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
    def __init__(self, file_name, m, D, instanceName):
        self.__file_name = file_name
        self.__customers = []
        self.__m= m
        self.__instanceName = instanceName
        self.__D = D
             
        df = pd.read_table(self.getFileName())
        for i in range(1,len(df)):
            c = df.iloc[i, 0].split(" ")
            self.setCustomer(Customer(int(c[0]), float(c[1]),float(c[2])))
        d = df.iloc[0, 0].split(" ")

        self.setDepot(Depot(int(d[0]), float(d[1]),float(d[2])))
        
    def getFileName(self):
        return self.__file_name
    def getInstanceName(self):
        return self.__instanceName
    def getD(self):
        return self.__D
    def getM(self):
        return self.__m
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