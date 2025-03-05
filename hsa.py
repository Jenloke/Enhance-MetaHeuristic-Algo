# # import numpy as np
# # import random 

# # random.seed('spearhead')

# # generate hm memory
# # {items: [0, 1, 0, ...], value: x, weight: y}
# # 
# # 
# # 
# # 

# # def randomSolution() -> np:
# #   return

# # # list = [1,2,3]
# # HM = np.array([1, 2, 3])
# # print(HM)

# import numpy as np

# def objective_function(x):
# 	# Example objective function: Sphere function.
# 	return sum(x_i ** 2 for x_i in x)

# def initialize_harmony_memory(hm_size, dim, lower_bound, upper_bound):
# 	"""Initialize the harmony memory with random solutions."""
# 	x = np.random.uniform(lower_bound, upper_bound, (hm_size, dim))
# 	print(x)
# 	return x

# def improvise_new_harmony(harmony_memory, hmcr, par, lower_bound, upper_bound):
# 	# Generate a new harmony based on memory considerations and randomization.
# 	dim = harmony_memory.shape[1]
# 	new_harmony = np.zeros(dim)
	
# 	for i in range(dim):
# 		if np.random.rand() < hmcr:
# 			new_harmony[i] = np.random.choice(harmony_memory[:, i])
# 			if np.random.rand() < par:
# 				adjustment = np.random.uniform(-0.1, 0.1)  # Small adjustment
# 				new_harmony[i] += adjustment
# 			else:
# 				new_harmony[i] = np.random.uniform(lower_bound, upper_bound)
	
# 	return np.clip(new_harmony, lower_bound, upper_bound)

# #hm size - total knapsack items

# # def harmony_search(objective_function, dim, lower_bound, upper_bound, hm_size=10, hmcr=0.9, par=0.3, max_iter=10):
# def harmony_search(objective_function, dim, lower_bound, upper_bound, hm_size=10, hmcr=0.9, par=0.3, max_iter=10):
# 	# Main harmony search algorithm.
# 	harmony_memory = initialize_harmony_memory(hm_size, dim, lower_bound, upper_bound)
# 	harmony_fitness = np.apply_along_axis(objective_function, 1, harmony_memory)
	
# 	for _ in range(max_iter):
# 		new_harmony = improvise_new_harmony(harmony_memory, hmcr, par, lower_bound, upper_bound)
# 		new_fitness = objective_function(new_harmony)

# 		worst_index = np.argmax(harmony_fitness)
# 		if new_fitness < harmony_fitness[worst_index]:
# 			harmony_memory[worst_index] = new_harmony
# 			harmony_fitness[worst_index] = new_fitness

# 		best_index = np.argmin(harmony_fitness)
# 		return harmony_memory[best_index], harmony_fitness[best_index]

# # Example usage
# dim = 10
# lower_bound = -10
# upper_bound = 10
# best_solution, best_fitness = harmony_search(objective_function, dim, lower_bound, upper_bound)
# print("Best solution:", best_solution)
# print("Best fitness:", best_fitness)


import numpy as np

# Problem Proper
# File 1
# from binary file to a np array where each line has become a list
knapsackProblem = open(f"./Dataset/{1}/{100}/knapPI_{1}_{100}_1000_1", "r").readlines()
new_knapsackProblem = np.array([x.split() for x in knapsackProblem], dtype=int).astype(int)

# get first element cause it contains the total items and the knapsack's capacity
knapsackTotalItems, knapsackCapacity = new_knapsackProblem[:1][0] 
# print(knapsackTotalItems, knapsackCapacity)

# get the rest cause it is the list of items for the 0/1 knapsack problem
np_knapsackProblem = new_knapsackProblem[1:]
# print(np_knapsackProblem)

# File 2
# Optimal Solution Array of 1 and 0 to NumPy Array of Boolean Values
optimalSolution = open(f"./Dataset/{1}/{100}/knapPI_{1}_{100}_1000_1a", "r").read()
np_booleanArray = np.array(optimalSolution.split(), dtype=int).astype(bool)
# print(len(np_booleanArray))

# File 3
optimalKnapsackValue: int = int(open(f"./Dataset/{1}/{100}/knapPI_{1}_{100}_1000_1o", "r").read())
# print(optimalKnapsackValue)

# Combining File 1 && 3
value, weight = np_knapsackProblem.T

# Problem Parameters
weights = [2, 3, 4, 5, 9]  # Weights of items
values = [3, 4, 8, 8, 10]  # Values of items

# weights = weight  # Weights of items
# values = value  # Values of items
capacity = 10  # Knapsack capacity
num_items = len(weights)

print(num_items)

# Harmony Search Parameters
HMS = 100  # Harmony Memory Size
HMCR = 0.9  # Harmony Memory Consideration Rate
PAR = 0.3  # Pitch Adjustment Rate
iterations = 1000

# Generate Initial Harmony Memory (Random Feasible Solutions)
def generate_solution():
	while True:
		solution = np.random.randint(0, 2, num_items)
		x = np.dot(solution, weights)
		print(x)
		if x <= capacity:
			return solution

harmony_memory = [generate_solution() for _ in range(HMS)]
harmony_values = [np.dot(sol, values) for sol in harmony_memory]

# Harmony Search Optimization Loop
for _ in range(iterations):
	# Step 1: Improvise New Harmony
	new_harmony = np.zeros(num_items, dtype=int)
	for i in range(num_items):
		if np.random.rand() < HMCR:  # Memory consideration
			new_harmony[i] = np.random.choice([hm[i] for hm in harmony_memory])
		else:  # Random selection
			new_harmony[i] = np.random.randint(0, 2)

			# Pitch Adjustment (Small Modification)
		if np.random.rand() < PAR:
			new_harmony[i] = 1 - new_harmony[i]  # Flip bit

	# Step 2: Ensure Feasibility
	while np.dot(new_harmony, weights) > capacity:
		idx = np.random.choice(np.where(new_harmony == 1)[0])  # Pick a random 1
		new_harmony[idx] = 0  # Remove the item

	# Step 3: Evaluate and Update Harmony Memory
	new_value = np.dot(new_harmony, values)
	min_idx = np.argmin(harmony_values)
	if new_value > harmony_values[min_idx]:  # Replace the worst solution
		harmony_memory[min_idx] = new_harmony
		harmony_values[min_idx] = new_value

# Best Solution Found
best_index = np.argmax(harmony_values)
best_solution = harmony_memory[best_index]
best_value = harmony_values[best_index]

print("Best Solution:", best_solution)
print("Total Value:", best_value)
