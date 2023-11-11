# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 11:10:37 2022

@author: Ahmed Kheiri
"""

from Problem import Problem
from SequentialInsertion import SequentialInsertion
from QuasiSequentialInsertion import QuasiSequentialInsertion
from NaiveParallelInsertion import NaiveParallelInsertion
from ParallelInsertionWithSeeds import ParallelInsertionWithSeeds
from SumOfSquaresInsertion import SumOfSquaresInsertion
from SRIE import SRIE

parameters = []
parameters.append(("dataset/instanceAUni.xy", 5, 2, "instanceAUni"))
parameters.append(("dataset/instanceBUni.xy", 5, 4, "instanceBUni"))
parameters.append(("dataset/instanceCUni.xy", 5, 2, "instanceCUni"))
parameters.append(("dataset/instanceDUni.xy", 5, 4, "instanceDUni"))
parameters.append(("dataset/instanceAExp.xy", 5, 2, "instanceAExp"))
parameters.append(("dataset/instanceBExp.xy", 5, 4, "instanceBExp"))
parameters.append(("dataset/instanceCExp.xy", 5, 2, "instanceCExp"))
parameters.append(("dataset/instanceDExp.xy", 5, 4, "instanceDExp"))

no_runs = 10
solvers = [SequentialInsertion, QuasiSequentialInsertion, NaiveParallelInsertion, ParallelInsertionWithSeeds, SumOfSquaresInsertion]

no_iterations_factor_LS = 10
number_of_customers_served_to_apply_LS = 1 # 0 means LS will not be applied
isSumSqObj_LS = [False,True]


########## UPDATED PARAMETERS FOR TESTING
#parameters = [("dataset/instanceAUni.xy", 5, 2, "instanceAUni")]
no_runs = 1
solvers = [SumOfSquaresInsertion]
isSumSqObj_LS = [True]
#####################

for isSumSqObj in isSumSqObj_LS:
    print("LS:",number_of_customers_served_to_apply_LS, "sum_sq_LS:",isSumSqObj)
    for i in range(len(parameters)):
        print(parameters[i][-1])
        for s in range(len(solvers)):
            dist = []
            no_customers = []
            LSCalled = []
            for run in range(no_runs):
                pr = Problem(parameters[i][0], parameters[i][1], parameters[i][2], parameters[i][3])
                #pr.shuffleOrders(run)
                solver = solvers[s](pr, SRIE(no_iterations_factor_LS, isSumSqObj), number_of_customers_served_to_apply_LS)
                solver.solve()
                dist.append(solver.getSolution().getSolutionTotalDistance())
                no_customers.append(solver.getSolution().getSolutionNumberOfSatisfiedCustomers())
                LSCalled.append(solver.getNumberOfTimeLSIsCalled())
                #print(solver.getSolution())
                solver.getSolution().DrawSolution(parameters[i][-1]+"WithLS")
            print(solver,"\t", sum(dist) / len(dist), "\t",sum(no_customers) / len(no_customers), "\t",sum(LSCalled) / len(LSCalled))
        print()