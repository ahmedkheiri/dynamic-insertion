# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 11:10:37 2022

@author: Ahmed Kheiri
"""

import random
from LocalSearch import LocalSearch

class SRIE(LocalSearch):
    def improve(self):
        
        obj = self.getObjective()
        prev_sol = self.getCopySolution()
        
        for iteration in range(self.getNumberOfIterationsFactor() * self.getSolution().getSolutionNumberOfSatisfiedCustomers()):
            llh = random.randint(0, self.getNumberOfLLHs() - 1)
            self.applyLLH(llh)
            newObj = self.getObjective()
            if  newObj <= obj:
                obj = newObj
                prev_sol = self.getCopySolution()
            else : 
                self.copyFrom(prev_sol)