# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 11:10:37 2022

@author: Ahmed Kheiri
"""

from Solution import Solution
from Problem import Problem

class Solver:
    def __init__(self, problem):
        self.__problem = problem
        self.__solution = Solution()
    def getProblem(self) -> Problem:
        return self.__problem
    def getSolution(self) -> Solution:
        return self.__solution
