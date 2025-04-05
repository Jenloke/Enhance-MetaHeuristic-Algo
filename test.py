from main import problem
from main import optimalSolution
from numpy import random

from datetime import datetime
import tracemalloc

from pso import pso
from epso import epso
from hsa import hsa

from test_hsa import test_hsa

random.seed(12)

# set = [1, 2, 3]
sets = [2]

# size = [100, 200, 500, 1000, 2000, 5000]
# size = [100, 200, 500]
sizes = [100]

# n for pso/epso = particles
# n for hsa = harmony memory size (HMS)
n = 20
iterations = 100

for set in sets:
  for size in sizes:
    prob = problem(set, size)
    
    tracemalloc.start()
    
    start_time = datetime.now()
    
    algo = pso(**prob, particles=n, n_iterations=iterations)
    # algo = hsa(**prob, harmonyMemorySize=n, n_iterations=iterations)
    # algo = epso(**prob, particles=n, n_iterations=iterations)
    
    # algo = test_hsa(**prob, harmonyMemorySize=n, n_iterations=iterations)

    end_time = datetime.now()
    print(end_time - start_time)

    # Capture the memory usage
    current, peak = tracemalloc.get_traced_memory()
    # Stop the memory tracking
    tracemalloc.stop()
    print(f"Peak memory usage: {peak} bytes") # Bytes
    print(f"Peak memory usage: {peak / 1024:.3f} kilobytes") # Kilobytes
    print(f"Peak memory usage: {peak / 10**6:.3f} megabytes") # Megabytes

    if algo['numberIterations'] == iterations:
      print('Solved at MAX ITR', iterations)
    else:
      print('Solved before MAX specified ITR reached', algo['numberIterations'])

    # Final Value
    print(algo['solValue'])
    
    # Sucess Rate
    print('percentage:', algo['solValue']/prob['optimalKnapsackValue']*100)
    
    # Compare finalSol to optiSol
    # compare each item to opti compare lang
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
        # print(eval, 'sol - should be one')
      if (optiSolution[idx] == 0 and algo['solArray'][idx] == 1):
        decrepancy.append({
          'index': idx,
          'value': prob['value'][idx].item(),
          'weight': prob['weight'][idx].item(),
          'case': 'O=0, S=1, should not be in Solution', 
        })
        # print(eval, 'sol - should be zero')

    print(decrepancy)

"""
Convergence Speed 
  get best value per iteration - check
  get where solution flattens - evaluate - could be done in jupyter notebook - where solution stalls
    get mean or avg solution to essentially determine if it still finds another solution
Memory Complexity - Completed
  using tracemalloc - check
Sucess Rate 
  algo / prob - check
"""