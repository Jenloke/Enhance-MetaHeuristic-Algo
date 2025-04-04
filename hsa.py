import numpy as np

def hsa(problemLength, value, weight, knapsackCapacity, optimalKnapsackValue, harmonyMemorySize, iterations):
	np.random.seed(12)
	# Problem Parameters
	num_items = problemLength
	capacity = knapsackCapacity  # Knapsack capacity
	values = value # Values of items
	weights = weight # Weights of items

	# Harmony Search Parameters
	HMS = harmonyMemorySize  # Harmony Memory Size
	# iterations = 100
	HMCR = 0.7 # Harmony Memory Consideration Rate
	PAR = 0.3 # Pitch Adjustment Rate
	PAR_min = PAR
	PAR_max = PAR + 0.6

	def repair_solution(solution):
		# Ensures solution is within the weight constraint.
		while np.sum(weights * solution) > capacity:
			idx = np.where(solution == 1)[0]
			if len(idx) == 0:
				break
			worst_idx = idx[np.argmin(values[idx] / weights[idx])]
			solution[worst_idx] = 0
		return solution

	# Generate Initial Harmony Memory (Random\ Feasible Solutions)
	def generate_solution():
		solution = np.random.randint(0, 2, num_items)
		repair_solution(solution)
		return solution

	harmony_memory = [generate_solution() for _ in range(HMS)]
	harmony_values = [np.dot(sol, values) for sol in harmony_memory]

	# Harmony Search Optimization Loop
	for itr in range(iterations):
		# Step 1: Improvise New Harmony
		new_harmony = np.zeros(num_items, dtype=int)
		for i in range(num_items):
			if np.random.rand() < HMCR:  # Memory consideration
				new_harmony[i] = np.random.choice([hm[i] for hm in harmony_memory])
			else:  # Random selection
				new_harmony[i] = np.random.randint(0, 2)

			PAR = PAR_min + ((PAR_max - PAR_min) / iterations) * (itr/iterations)
			# Pitch Adjustment (Small Modification)
			if np.random.rand() < PAR:
				new_harmony[i] = 1 - new_harmony[i]  # Flip bit

		# Step 2: Ensure Feasibility
		repair_solution(new_harmony)

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

	# print("Best Solution:", best_solution)
	# print("Total Value:", best_value)

	return {
		'solValue': best_value,
		'solArray': best_solution,
		'numberIterations': iterations,
	}

# if harmony_values[np.argmax(harmony_values)] == optimalKnapsackValue:
# 	return {
# 		'solValue': best_value,
# 		'solArray': best_solution,
# 		'numberIterations': iterations,
# 		'numberIterations': itr+1,
# 	}

# Old Step2
# while np.dot(new_harmony, weights) > capacity:
# 	idx = np.random.choice(np.where(new_harmony == 1)[0])  # Pick a random 1
# 	new_harmony[idx] = 0  # Remove the item

# old_argmax = 0
# if np.argmax(harmony_values) != old_argmax:
# 	print(_, np.argmax(harmony_values))
# old_argmax = np.argmax(harmony_values)