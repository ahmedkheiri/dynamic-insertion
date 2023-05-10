# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 11:10:37 2022

@author: Ahmed Kheiri
"""

class Depot:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    def __str__(self):
        return "Depot({},{})".format(self.__x,self.__y)
