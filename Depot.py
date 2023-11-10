# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 11:10:37 2022

@author: Ahmed Kheiri
"""

class Depot:
    def __init__(self, ID, x, y):
        self.__ID = ID
        self.__x = x
        self.__y = y
    def getID(self):
        return self.__ID
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    def __str__(self):
        return "Depot{}({},{})".format(self.__id,self.__x,self.__y)
