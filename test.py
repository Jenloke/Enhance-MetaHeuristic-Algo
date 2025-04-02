from main import problem
from pso import pso

x = problem(1, 100)

y = pso(x['problemLength'], x['value'], x['weight'], x['knapsackCapacity'])
print(y)