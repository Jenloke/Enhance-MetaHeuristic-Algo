import numpy as np

# Define the 0/1 Knapsack Problem
def knapsack_fitness(solution, values, weights, capacity):
  total_value = np.sum(solution * values)
  total_weight = np.sum(solution * weights)
  
  if total_weight > capacity:
    return 0  # Penalize infeasible solutions
  return total_value

# Initialize WOA parameters
class WOA_Knapsack:
  def __init__(self, values, weights, capacity, num_whales=30, max_iter=100):
      self.values = np.array(values)
      self.weights = np.array(weights)
      self.capacity = capacity
      self.num_whales = num_whales
      self.max_iter = max_iter
      self.num_items = len(values)

  def optimize(self):
    # Initialize whale population randomly (binary solutions)
    whales = np.random.randint(0, 2, (self.num_whales, self.num_items))
    best_whale = None
    best_fitness = -np.inf

    # Evaluate initial population
    fitness = np.array([knapsack_fitness(whale, self.values, self.weights, self.capacity) for whale in whales])
    best_idx = np.argmax(fitness)
    best_whale = whales[best_idx].copy()
    best_fitness = fitness[best_idx]

    # WOA Main Loop
    for iteration in range(self.max_iter):
      a = 2 - (2 * iteration / self.max_iter)  # Linearly decreasing coefficient
      for i in range(self.num_whales):
        r = np.random.rand()
        A = 2 * a * r - a  # Compute A vector
        C = 2 * np.random.rand()  # Compute C vector

        if np.random.rand() < 0.5:
          if abs(A) < 1:
            # Encircling best solution
            D = np.abs(best_whale - whales[i])
            whales[i] = np.clip(best_whale - A * D, 0, 1).astype(int)
          else:
            # Exploration phase
            rand_whale = whales[np.random.randint(0, self.num_whales)]
            D = np.abs(rand_whale - whales[i])
            whales[i] = np.clip(rand_whale - A * D, 0, 1).astype(int)
      else:
        # Spiral updating position
        b = 1  # Constant for spiral equation
        l = np.random.uniform(-1, 1)  # Random number
        D_prime = np.abs(best_whale - whales[i])
        whales[i] = np.clip(D_prime * np.exp(b * l) * np.cos(2 * np.pi * l) + best_whale, 0, 1).astype(int)

        # Ensure solutions satisfy constraints
        if np.sum(whales[i] * self.weights) > self.capacity:
            whales[i] = self.repair_solution(whales[i])

        # Evaluate fitness
        fitness[i] = knapsack_fitness(whales[i], self.values, self.weights, self.capacity)

        # Update best solution
        if fitness[i] > best_fitness:
          best_fitness = fitness[i]
          best_whale = whales[i].copy()
    return best_whale, best_fitness

  def repair_solution(self, solution):
    """ Repair infeasible solution by removing items with lowest value/weight ratio """
    while np.sum(solution * self.weights) > self.capacity:
      idxs = np.where(solution == 1)[0]
      if len(idxs) == 0:
        break
      worst_idx = idxs[np.argmin(self.values[idxs] / self.weights[idxs])]
      solution[worst_idx] = 0
    return solution


file = 1
size = 10000

knapsackProblem = open(f"./Dataset/{file}/{size}/knapPI_{file}_{size}_1000_1", "r").readlines()
new_knapsackProblem = np.array([x.split() for x in knapsackProblem], dtype=int).astype(int)
# get first element cause it contains the total items and the knapsack's capacity
knapsackTotalItems, knapsackCapacity = new_knapsackProblem[:1][0] 
print(knapsackTotalItems, knapsackCapacity)
# get the rest cause it is the list of items for the 0/1 knapsack problem
np_knapsackProblem = new_knapsackProblem[1:]

# File 2
# Optimal Solution Array of 1 and 0 to NumPy Array of Boolean Values
optimalSolution = open(f"./Dataset/{file}/{size}/knapPI_{file}_{size}_1000_1a", "r").read()
np_booleanArray = np.array(optimalSolution.split(), dtype=int)
print(np_booleanArray)

# File 3
optimalKnapsackValue: int = int(open(f"./Dataset/{file}/{size}/knapPI_{file}_{size}_1000_1o", "r").read())
print(optimalKnapsackValue)

# Combining File 1 && 3
value, weight = np_knapsackProblem.T

# Example usage
values = value
weights = weight
capacity = knapsackCapacity

woa = WOA_Knapsack(values, weights, capacity, num_whales=20, max_iter=100)

best_solution, best_value = woa.optimize()
print("Best Solution:", best_solution)
print("Best Value:", best_value)
