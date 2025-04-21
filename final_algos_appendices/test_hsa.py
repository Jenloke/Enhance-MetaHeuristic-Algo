import numpy as np

def hsa(problemLength, value, weight, knapsackCapacity, optimalKnapsackValue, population, n_iterations):
	# Problem Parameters
	num_items = problemLength
	max_weight = knapsackCapacity
	values = value # Values of items
	weights = weight # Weights of items

	# HSA Parameters
	HMS = population  # Harmony Memory Size
	max_iterations = n_iterations
	HMCR = 0.8 # Harmony Memory Consideration Rate
	PAR = 0.2 # Pitch Adjustment Rate
	PAR_min = PAR
	PAR_max = PAR + 0.6

	def repair_solution(solution):
		# Ensures solution is within the weight constraint.
		while np.dot(solution, weights) > max_weight:
			idx = np.where(solution == 1)[0]
			if len(idx) == 0:
				break
			worst_idx = idx[np.argmin(values[idx] / weights[idx])]
			solution[worst_idx] = 0
		return solution

	# Generate Initial Harmony Memory (Random Feasible Solutions)
	def generate_solution():
		solution = np.random.randint(0, 2, num_items)
		repair_solution(solution)
		return solution

	harmony_memory = np.array([generate_solution() for _ in range(HMS)])
	harmony_values = np.array([np.dot(solution, values) for solution in harmony_memory])

	best_SolutionPerIteration = np.array([], dtype=int)

	# Harmony Search Optimization Loop
	for itr in range(max_iterations):
		# Step 1: Improvise New Harmony
		new_harmony = np.zeros(num_items, dtype=int)
		for i in range(num_items):
			if np.random.rand() < HMCR:  # Memory consideration
				new_harmony[i] = np.random.choice([hm[i] for hm in harmony_memory])
			else:  # Random selection
				new_harmony[i] = np.random.randint(0, 2)

			PAR = PAR_min + ((PAR_max - PAR_min) / max_iterations) * (itr/max_iterations)
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

		best_SolutionPerIteration = np.append(best_SolutionPerIteration, harmony_values[np.argmax(harmony_values)])

		if harmony_values[np.argmax(harmony_values)] == optimalKnapsackValue:
			best_index = np.argmax(harmony_values)
			return {
				'solValue': harmony_values[best_index].item(),
				'solWeight': np.dot(harmony_memory[best_index], weights).item(),		
				'solArray': harmony_memory[best_index].tolist(),
				'numberIterations': itr+1,
				'best_SolutionPerIteration': best_SolutionPerIteration.tolist(),
			}  

	# Best Solution Found
	best_index = np.argmax(harmony_values)
	best_solution = harmony_memory[best_index]
	best_value = harmony_values[best_index]

	return {
		'solValue': best_value.item(),
		'solWeight': np.dot(best_solution, weights).item(),
		'solArray': best_solution.tolist(),
		'numberIterations': max_iterations,
		'best_SolutionPerIteration': best_SolutionPerIteration.tolist(),
	}