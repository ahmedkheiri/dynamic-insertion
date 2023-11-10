# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 11:10:37 2022

@author: Ahmed Kheiri
"""

class Customer:
    def __init__(self, ID, x, y, demand):
        self.__ID = ID
        self.__x = x
        self.__y = y
        self.__demand = demand
    def getID(self):
        return self.__ID
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    def getDemand(self):
        return self.__demand
    def __str__(self):
        return "Customer{}({},{},{})".format(self.__ID,self.__x,self.__y,self.__demand)
    def __repr__(self):
        return self.__str__()
