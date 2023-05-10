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

problem_version = ["DC", "DD"]
parameters = []
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
no_runs = 1000
solvers = [SequentialInsertion, QuasiSequentialInsertion, NaiveParallelInsertion, ParallelInsertionWithSeeds, SumOfSquaresInsertion]


########## TEST
problem_version = ["DC"]
parameters = [("dataset/araq41.xy", 4, 10, False, 647, "AKMP1")]
no_runs = 1
solvers = [SequentialInsertion]
#####################

for ver in problem_version:
    print(ver)
    for i in range(len(parameters)):
        print(parameters[i][5],end=" ")
        for s in range(len(solvers)):
            dist = []
            no_customers = []
            for run in range(no_runs):
                pr = Problem(parameters[i][0], parameters[i][1], parameters[i][2], parameters[i][3], parameters[i][4], parameters[i][5], ver)
                pr.shuffleOrders(run)
                solver = solvers[s](pr)
                solver.solve()
                dist.append(solver.getSolution().getSolutionTotalDistance())
                no_customers.append(solver.getSolution().getSolutionNumberOfSatisfiedCustomers())
            print(sum(dist) / len(dist), sum(no_customers) / len(no_customers),end=" ")
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
