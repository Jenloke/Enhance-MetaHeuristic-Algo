from main import problem
from main import optimalSolution

from datetime import datetime

from pso import pso
from epso import epso
from hsa import hsa

size = [100, 200, 500, 1000, 2000, 5000]
# size = [100, 200, 500]
# size = [500]

n = 20
iterations = 500

print('epso start')
for m in size:
  x = problem(1, m)
  start_time = datetime.now()
  y = hsa(x['problemLength'], x['value'], x['weight'], x['knapsackCapacity'], x['optimalKnapsackValue'], n, iterations=iterations)
  end_time = datetime.now()
  print(end_time - start_time)
  
  if y['numberIterations'] == iterations:
    print('Solved at MAX ITR', iterations)
  else:
    print('Solved before MAX specified ITR reached', y['numberIterations'])
  
  print(y['solValue'], '\n')
  
# Convergence Speed - 
# Memory Complexity - 
# Sucess Rate - Partially Completed