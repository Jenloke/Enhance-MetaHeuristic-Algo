from main import problem
from main import optimalSolution
from numpy import random

from datetime import datetime
import tracemalloc

import csv

from pso import pso
from epso import epso
from hsa import hsa

from test_hsa import test_hsa
from test_pso import test_pso
from test_g1_epso import test_g1_epso
from test_ga_epso import test_ga_epso

# problem_seeds = [12, 49, 2]
problem_seeds = [293]

sets = [1, 2, 3]
# sets = [1]

sizes = [100, 200, 500, 1000, 2000, 5000]
# sizes = [100]

# n for pso/epso = particles
# n for hsa = harmony memory size (HMS)
problem_parameters = [
  {'n': 20, 'iterations': 100}, 
  {'n': 20, 'iterations': 500}
]

algos = [test_hsa, test_pso, test_g1_epso, test_ga_epso]
# algos = [test_hsa]

solutions = []

for seed in problem_seeds:
  random.seed(seed)
  print('Run Seed:', seed)
  for x in problem_parameters:
    for set in sets:
      print('Problem Set:', set)
      for size in sizes:
        prob = problem(set, size)
        for algo in algos:
          algorithm = algo.__name__
          
          tracemalloc.start()
          
          start_time = datetime.now()
          
          algo = algo(**prob, population=x['n'], n_iterations=x['iterations'])
          # algo = pso(**prob, particles=n, n_iterations=iterations)
          # algo = hsa(**prob, harmonyMemorySize=n, n_iterations=iterations)
          # algo = epso(**prob, particles=n, n_iterations=iterations)
          # algo = test_hsa(**prob, harmonyMemorySize=n, n_iterations=iterations)
          # algo = test_pso(**prob, particles=n, n_iterations=iterations)
          # algo = test_epso(**prob, particles=n, n_iterations=iterations)

          end_time = datetime.now()
          runTime = (end_time - start_time).total_seconds()
          # print(runTime, 'seconds')

          # Capture the memory usage
          _, peak = tracemalloc.get_traced_memory()
          # Stop the memory tracking
          tracemalloc.stop()
          memory_peak = peak / 1024
          # print(f"Peak memory usage: {memory_peak} kilobytes") # Kilobytes
          
          # print('solvalue', algo['solValue'])
          
          # Sucess Rate
          sucessRate = algo['solValue'] / prob['optimalKnapsackValue'] * 100
          # print('percentage:', sucessRate)
          
          # Compare finalSol to optiSol
          optiSolution = optimalSolution(set, size)
          decrepancy = []    
          for idx in range(prob['problemLength']):
            if (optiSolution[idx] == 1 and algo['solArray'][idx] == 0):
              decrepancy.append({
                'index': idx,
                'value': prob['value'][idx].item(),
                'weight': prob['weight'][idx].item(),
                'case': 'O=1, S=0, should be in Solution', 
              })
            if (optiSolution[idx] == 0 and algo['solArray'][idx] == 1):
              decrepancy.append({
                'index': idx,
                'value': prob['value'][idx].item(),
                'weight': prob['weight'][idx].item(),
                'case': 'O=0, S=1, should not be in Solution', 
              })

          final = {
            #Problem
            'seed': seed,
            'set': set,
            'size': size,
            'algo': algorithm,
            #Problem_Parameters
            'n': x['n'],
            'iterations': x['iterations'],
            # Solution
            'numberIterations': algo['numberIterations'],
            'solArray': algo['solArray'],
            'solValue': algo['solValue'],
            'solWeight': algo['solWeight'],
            'greedy_solValue': algo['greedy_solValue'] if algorithm == 'test_epso' else -1,
            # Objective #1
            'best_SolutionPerIteration': algo['best_SolutionPerIteration'],
            'runTime': runTime,
            # Objective #2
            'memoryPeak': memory_peak,
            # Objective #3
            'decrepancy': decrepancy, 
            'sucessRate': sucessRate,
          }
          # print(final)
          print(f'Seed: {seed}, Set: {set}, Algorithm: {algorithm}, Size: {size}, Total Iterations: {x['iterations']}, Problem Population: {x['n']}')
          print(f'Solution Value: {final['solValue']}, Solution Weight: {final['solWeight']}, Iterations Upon Completion: {final['numberIterations']}')
          print(f'Optimality Rate: {final['sucessRate']}, Runtime: {final['runTime']}, Peak Memory Usage: {final['memoryPeak']}')
          print('')
          solutions.append(final)

headers = solutions[0].keys()
# Write CSV using dictionary unpacking
with open("output.csv", "w", newline="") as csvfile:
  writer = csv.DictWriter(csvfile, fieldnames=headers)
  writer.writeheader()
  for row in solutions:
    writer.writerow({**row})  # Using unpacking/spreading
print('Algorithm Run Success')