# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 11:10:37 2022

@author: Ahmed Kheiri
"""

from Solution import Solution
from Problem import Problem
from LocalSearch import LocalSearch

class Solver:
    def __init__(self, problem, local_search, number_of_customers_to_apply_LS):
        self.__problem = problem
        self.__solution = Solution()
        self.__local_search = local_search
        self.__local_search.setProblem(problem)
        self.__local_search.setSolution(self.__solution)
        self.__number_of_customers_to_apply_LS = number_of_customers_to_apply_LS
        self.__number_of_time_LS_is_called = 0
        
    def getProblem(self) -> Problem:
        return self.__problem
    def getSolution(self) -> Solution:
        return self.__solution
    def getLocalSearch(self) -> LocalSearch:
        return self.__local_search
    def getNumberOfCustomersToApplyLS(self):
        return self.__number_of_customers_to_apply_LS
    def getNumberOfTimeLSIsCalled(self):
        return self.__number_of_time_LS_is_called
    def increaseNumberOfTimeLSIsCalled(self):
        self.__number_of_time_LS_is_called += 1
    def __str__(self):
        return self.__class__.__name__