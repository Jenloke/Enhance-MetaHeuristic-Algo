# import numpy as np
# import random 

# random.seed('spearhead')

# generate hm memory
# {items: [0, 1, 0, ...], value: x, weight: y}
# 
# 
# 
# 

# def randomSolution() -> np:
#   return

# # list = [1,2,3]
# HM = np.array([1, 2, 3])
# print(HM)

import numpy as np

def objective_function(x):
    # Example objective function: Sphere function.
    return sum(x_i ** 2 for x_i in x)

def initialize_harmony_memory(hm_size, dim, lower_bound, upper_bound):
    """Initialize the harmony memory with random solutions."""
    x = np.random.uniform(lower_bound, upper_bound, (hm_size, dim))
    print(x)
    return x

def improvise_new_harmony(harmony_memory, hmcr, par, lower_bound, upper_bound):
    # Generate a new harmony based on memory considerations and randomization.
    dim = harmony_memory.shape[1]
    new_harmony = np.zeros(dim)
    
    for i in range(dim):
        if np.random.rand() < hmcr:
            new_harmony[i] = np.random.choice(harmony_memory[:, i])
            if np.random.rand() < par:
                adjustment = np.random.uniform(-0.1, 0.1)  # Small adjustment
                new_harmony[i] += adjustment
        else:
            new_harmony[i] = np.random.uniform(lower_bound, upper_bound)
    
    return np.clip(new_harmony, lower_bound, upper_bound)

#hm size - total knapsack items

def harmony_search(objective_function, dim, lower_bound, upper_bound, hm_size=10, hmcr=0.9, par=0.3, max_iter=10):
    # Main harmony search algorithm.
    harmony_memory = initialize_harmony_memory(hm_size, dim, lower_bound, upper_bound)
    harmony_fitness = np.apply_along_axis(objective_function, 1, harmony_memory)
    
    for _ in range(max_iter):
        new_harmony = improvise_new_harmony(harmony_memory, hmcr, par, lower_bound, upper_bound)
        new_fitness = objective_function(new_harmony)
        
        worst_index = np.argmax(harmony_fitness)
        if new_fitness < harmony_fitness[worst_index]:
            harmony_memory[worst_index] = new_harmony
            harmony_fitness[worst_index] = new_fitness
    
    best_index = np.argmin(harmony_fitness)
    return harmony_memory[best_index], harmony_fitness[best_index]

# Example usage
dim = 10
lower_bound = -10
upper_bound = 10
best_solution, best_fitness = harmony_search(objective_function, dim, lower_bound, upper_bound)
print("Best solution:", best_solution)
print("Best fitness:", best_fitness)
