import random

class TabuSearchKnapsack:
    def __init__(self, values, weights, capacity, tabu_tenure=5, max_iterations=100):
        self.values = values
        self.weights = weights
        self.capacity = capacity
        self.tabu_tenure = tabu_tenure
        self.max_iterations = max_iterations
        self.num_items = len(values)

    def initial_solution(self):
        """Generate an initial feasible solution using a greedy heuristic."""
        indices = sorted(range(self.num_items), key=lambda i: self.values[i] / self.weights[i], reverse=True)
        solution = [0] * self.num_items
        total_weight = 0

        for i in indices:
            if total_weight + self.weights[i] <= self.capacity:
                solution[i] = 1
                total_weight += self.weights[i]
        
        return solution

    def objective(self, solution):
        """Compute the total value of the solution."""
        return sum(v * x for v, x in zip(self.values, solution))

    def weight(self, solution):
        """Compute the total weight of the solution."""
        return sum(w * x for w, x in zip(self.weights, solution))

    def get_neighbors(self, solution):
        """Generate neighboring solutions by flipping one item's selection."""
        neighbors = []
        for i in range(self.num_items):
            new_solution = solution[:]
            new_solution[i] = 1 - new_solution[i]  # Flip 0 to 1 or 1 to 0
            
            if self.weight(new_solution) <= self.capacity:  # Ensure feasibility
                neighbors.append(new_solution)
        
        return neighbors

    def search(self):
        """Perform Tabu Search to optimize the 0-1 Knapsack problem."""
        current_solution = self.initial_solution()
        best_solution = current_solution[:]
        best_value = self.objective(best_solution)
        tabu_list = []
        
        for _ in range(self.max_iterations):
            neighbors = self.get_neighbors(current_solution)
            if not neighbors:
                break
            
            best_neighbor = None
            best_neighbor_value = float('-inf')

            for neighbor in neighbors:
                neighbor_value = self.objective(neighbor)

                if neighbor not in tabu_list and neighbor_value > best_neighbor_value:
                    best_neighbor = neighbor
                    best_neighbor_value = neighbor_value

            if best_neighbor is None:
                break  # No valid move available
            
            current_solution = best_neighbor

            if best_neighbor_value > best_value:
                best_solution = best_neighbor[:]
                best_value = best_neighbor_value

            tabu_list.append(best_neighbor)
            if len(tabu_list) > self.tabu_tenure:
                tabu_list.pop(0)  # Maintain tabu tenure

        return best_solution, best_value

import numpy as np

file = 1
size = 1000

# File 1
# from binary file to a np array where each line has become a list
knapsackProblem = open(f"./Dataset/{file}/{size}/knapPI_{file}_{size}_1000_1", "r").readlines()
new_knapsackProblem = np.array([x.split() for x in knapsackProblem], dtype=int).astype(int)

# get first element cause it contains the total items and the knapsack's capacity
knapsackTotalItems, knapsackCapacity = new_knapsackProblem[:1][0] 
print(knapsackTotalItems, knapsackCapacity)

# get the rest cause it is the list of items for the 0/1 knapsack problem
np_knapsackProblem = new_knapsackProblem[1:]
# print(np_knapsackProblem)

# File 2
# Optimal Solution Array of 1 and 0 to NumPy Array of Boolean Values
optimalSolution = open(f"./Dataset/{file}/{size}/knapPI_{file}_{size}_1000_1a", "r").read()
np_booleanArray = np.array(optimalSolution.split(), dtype=int)
print(len(np_booleanArray))

# File 3
optimalKnapsackValue: int = int(open(f"./Dataset/{file}/{size}/knapPI_{file}_{size}_1000_1o", "r").read())
print(optimalKnapsackValue)

# Combining File 1 && 3
value, weight = np_knapsackProblem.T

# Example usage
values = value
weights = weight
capacity = knapsackCapacity

ts_knapsack = TabuSearchKnapsack(values, weights, capacity)
best_sol, best_val = ts_knapsack.search()

print("Best solution:", best_sol)
print("Best value:", best_val)
