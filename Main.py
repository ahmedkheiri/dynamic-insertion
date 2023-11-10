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

problem_version = ["DC", "DD"]
parameters = []
parameters.append(("dataset/instanceAUni.xy", 5, 10, True, 2*5, "instanceAUni"))
parameters.append(("dataset/instanceBUni.xy", 5, 10, True, 2*5, "instanceBUni"))
parameters.append(("dataset/instanceCUni.xy", 5, 10, True, 2*5, "instanceCUni"))
parameters.append(("dataset/instanceDUni.xy", 5, 10, True, 2*5, "instanceDUni"))
parameters.append(("dataset/instanceAExp.xy", 5, 10, True, 2*5, "instanceAExp"))
parameters.append(("dataset/instanceBExp.xy", 5, 10, True, 2*5, "instanceBExp"))
parameters.append(("dataset/instanceCExp.xy", 5, 10, True, 2*5, "instanceCExp"))
parameters.append(("dataset/instanceDExp.xy", 5, 10, True, 2*5, "instanceDExp"))



'''
parameters.append(("dataset/instance1.xy", 5, 10, True, 4*5, "RandomInstance1"))
parameters.append(("dataset/instance2.xy", 5, 10, True, 4*5, "RandomInstance2"))
parameters.append(("dataset/instance3.xy", 5, 10, True, 4*5, "RandomInstance3"))
parameters.append(("dataset/instance4.xy", 5, 10, True, 4*5, "RandomInstance4"))

parameters.append(("dataset/instance5.xy", 5, 10, True, 2*5, "RandomInstance5"))
parameters.append(("dataset/instance6.xy", 5, 10, True, 2*5, "RandomInstance6"))
parameters.append(("dataset/instance7.xy", 5, 10, True, 2*5, "RandomInstance7"))
parameters.append(("dataset/instance8.xy", 5, 10, True, 2*5, "RandomInstance8"))
'''

'''
parameters.append(("dataset/araq41.xy", 4, 10, False, 647, "AKMP1"))
parameters.append(("dataset/araq51.xy", 7, 8, False, 875, "AKMP7"))
parameters.append(("dataset/araq51.xy", 4, 15, False, 678, "AKMP8"))
parameters.append(("dataset/araq61.xy", 2, 30, False, 688, "AKMP13"))
parameters.append(("dataset/eil22.xy", 7, 3, False, 530, "AKMP15"))
parameters.append(("dataset/eil22.xy", 3, 7, False, 341, "AKMP16"))
parameters.append(("dataset/eil30.xy", 8, 4, True, 832, "AKMP17"))
parameters.append(("dataset/eil30.xy", 5, 6, True, 639, "AKMP18"))
parameters.append(("dataset/eil33ud.xy", 7, 5, True, 627, "AKMP19"))
parameters.append(("dataset/eil33ud.xy", 4, 8, True, 497, "AKMP20"))
'''
no_runs = 10
solvers = [SequentialInsertion, QuasiSequentialInsertion, NaiveParallelInsertion, ParallelInsertionWithSeeds, SumOfSquaresInsertion]

no_iterations_factor_LS = 10
number_of_customers_served_to_apply_LS = 0 # 0 means LS will not be applied
isSumSqObj_LS = [False,True]


########## UPDATED PARAMETERS FOR TESTING
problem_version = ["DD"]
#parameters = [("dataset/instanceDExp.xy", 5, 10, True, 2*5, "instanceDExp")]
no_runs = 1
solvers = [ParallelInsertionWithSeeds]
isSumSqObj_LS = [True]
#####################

for ver in problem_version:
    for isSumSqObj in isSumSqObj_LS:
        print(ver,"LS:",number_of_customers_served_to_apply_LS, "sum_sq_LS:",isSumSqObj)
        for i in range(len(parameters)):
            print(parameters[i][5])
            for s in range(len(solvers)):
                dist = []
                no_customers = []
                LSCalled = []
                for run in range(no_runs):
                    pr = Problem(parameters[i][0], parameters[i][1], parameters[i][2], parameters[i][3], parameters[i][4], parameters[i][5], ver)
                    #pr.shuffleOrders(run)
                    solver = solvers[s](pr, SRIE(no_iterations_factor_LS, isSumSqObj), number_of_customers_served_to_apply_LS)
                    solver.solve()
                    dist.append(solver.getSolution().getSolutionTotalDistance())
                    no_customers.append(solver.getSolution().getSolutionNumberOfSatisfiedCustomers())
                    LSCalled.append(solver.getNumberOfTimeLSIsCalled())
                    #print(solver.getSolution())
                    #solver.getSolution().DrawSolution()
                    
                print(solver,"\t", sum(dist) / len(dist), "\t",sum(no_customers) / len(no_customers), "\t",sum(LSCalled) / len(LSCalled))
                
            print()

'''
for i in range(len(parameters)):
    pr = Problem(parameters[i][0], parameters[i][1], parameters[i][2], parameters[i][3], parameters[i][4], parameters[i][5], problem_version[0])
    #solver = SequentialInsertion(pr)
    #solver = QuasiSequentialInsertion(pr)
    #solver = NaiveParallelInsertion(pr)
    #solver = ParallelInsertionWithSeeds(pr)
    solver = SumOfSquaresInsertion(pr)
    solver.solve()
    print(solver.getProblem().getInstanceName(), solver.getSolution().getSolutionTotalDistance(), solver.getSolution().getSolutionNumberOfSatisfiedCustomers(), solver.getSolution().getNumberOfVehicles(), solver.getSolution().getNumberOfVehiclesUsed())
    #print(solver.getSolution())
'''
