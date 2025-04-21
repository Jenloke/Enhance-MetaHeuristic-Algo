from main import problem
from main import optimalSolution
from numpy import random

from datetime import datetime
import tracemalloc

import csv

from test_hsa import test_hsa
from test_pso import test_pso
from test_g1_epso import test_g1_epso
from test_ga_epso import test_ga_epso

problem_seeds = [293]
sets = [1, 2, 3]
sizes = [100, 200, 500, 1000, 2000, 5000]

# n for pso/epso = particles
# n for hsa = harmony memory size (HMS)
problem_parameters = [
  {'n': 20, 'iterations': 100}, 
  {'n': 20, 'iterations': 500}
]
algos = [test_hsa, test_pso, test_g1_epso, test_ga_epso]

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
          
          tracemalloc.start() # Start Space Complexity Tracking
          start_time = datetime.now() # Start Runtime Tracking
          
          algo = algo(**prob, population=x['n'], n_iterations=x['iterations'])

          # Capture Runtime
          end_time = datetime.now() # Stop Runtime Tracking
          runTime = (end_time - start_time).total_seconds()

          # Capture the memory usage
          _, peak = tracemalloc.get_traced_memory()
          tracemalloc.stop() # Stop the memory tracking
          memory_peak = peak / 1024 # Convert bytes to kilobytes
          
          # Sucess Rate
          sucessRate = algo['solValue'] / prob['optimalKnapsackValue'] * 100
          
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