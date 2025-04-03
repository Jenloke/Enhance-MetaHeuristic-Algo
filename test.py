from main import problem
from main import optimalSolution
from pso import pso

size = [100, 200, 500, 1000, 2000, 5000]

for m in size:
  x = problem(1, m)
  y = pso(x['problemLength'], x['value'], x['weight'], x['knapsackCapacity'], x['optimalKnapsackValue'], particles=20 , iterations=500)
  print(y['solValue'], '\n')