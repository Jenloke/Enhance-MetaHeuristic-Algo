import numpy as np

file = 1
size = 100
# File 1
# from binary file to a np array where each line has become a list
knapsackProblem = open(f"./Dataset/{file}/{size}/knapPI_{file}_{size}_1000_1", "r").readlines()
new_knapsackProblem = np.array([x.split() for x in knapsackProblem], dtype=int).astype(int)

# get first element cause it contains the total items and the knapsack's capacity
problemLength, knapsackCapacity = new_knapsackProblem[:1][0]
print('problemLength:', problemLength)
print('knapsackCapacity:',  knapsackCapacity)

# get the rest cause it is the list of items for the 0/1 knapsack problem
np_knapsackProblem = new_knapsackProblem[1:]
# print(np_knapsackProblem)

# File 3
optimalKnapsackValue: int = int(open(f"./Dataset/{file}/{size}/knapPI_{file}_{size}_1000_1o", "r").read())
print('optimalKnapsackValue:', optimalKnapsackValue)

# Combining File 1 && 3
value, weight = np_knapsackProblem.T

# Problem Parameters
# weights = [2, 3, 4, 5, 9]  # Weights of items
# values = [3, 4, 8, 8, 10]  # Values of items
weights = weight
values = value

# weights = weight  # Weights of items
# values = value  # Values of items
capacity = knapsackCapacity  # Knapsack capacity
num_items = len(weights)

# print(num_items)

# Harmony Search Parameters
HMS = 1000  # Harmony Memory Size
HMCR = 0.7  # Harmony Memory Consideration Rate
PAR = 0.3  # Pitch Adjustment Rate
iterations = 3000

# Generate Initial Harmony Memory (Random\ Feasible Solutions)
def generate_solution():
	# return np.random.randint(0, 2, num_items)
	# solution = np.random.randint(0, 2, num_items)
	# while True:
	# 	if np.dot(solution, weights) <= capacity:
	# 		# print(np.dot(solution, values))
	# 		return solution
	# 	else:
	# 		idx = np.random.choice(np.where(solution == 1)[0])  # Pick a random 1
	# 		solution[idx] = 0  # Remove the item

	solution = np.random.randint(0, 2, num_items)
	N = int(num_items * 0.5)
	while True:
		if np.dot(solution, weights) <= capacity:
			# print(np.dot(solution, values))
			return solution
		else:
			indices = np.random.choice(len(solution), N, replace=False)
			solution[indices] = 0


	# not worth solution stuck at same solution (local optima)
	# capacity_sol = capacity
	# solution = np.zeros(num_items)
	# j = 0
	# while j <= capacity_sol-1:
	# 	if capacity_sol >= weights[j]:
	# 		solution[j] = 1
	# 		capacity_sol -= weights[j]
	# 	j += 1
	# return solution

harmony_memory = [generate_solution() for _ in range(HMS)]
harmony_values = [np.dot(sol, values) for sol in harmony_memory]

# old_argmax = 0
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

	# if np.argmax(harmony_values) != old_argmax:
	# 	print(_, np.argmax(harmony_values))
	# old_argmax = np.argmax(harmony_values)

# Best Solution Found
best_index = np.argmax(harmony_values)
best_solution = harmony_memory[best_index]
best_value = harmony_values[best_index]

print("Best Solution:", best_solution)
print("Total Value:", best_value)
