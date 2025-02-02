# Basic File Reading Python
# file = [100,200,500,1000, 2000,5000,10000]
# log = 0
# for i in range(3):
#   for x in file:
#     file1 = open(f"./Dataset/{i+1}/{x}/knapPI_{i+1}_{x}_1000_1", "r")
#     log = log + 1
#     print(file1.read)
# print(log)

# with open(f"./Dataset/{1}/{100}/knapPI_{1}_{100}_1000_1", "r") as file:
#   content = file.read()
#   print(content)

# knapsackProblem = "knapPI_1_100_1000_1"
# optimalSolution = "knapPI_1_100_1000_1a"
# optimalKnapsackValue = "knapPI_1_100_1000_1o"

# print(open(f"./Dataset/{1}/{100}/knapPI_{1}_{100}_1000_1", "r").read())

import numpy as np

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
# value, weight = np.hsplit(np_knapsackProblem, 2)
# value = value.flatten()
# weight = weight.flatten()
combination = np.stack((value, weight, np_booleanArray), axis=1)

# Correct
print(len(np_booleanArray))
print(len(weight))
print(len(value))

# Sample Values
# print(np_booleanArray[6])
# print(np_knapsackProblem[6])
# print(combination[6])
# print(np_booleanArray[10])
# print(np_knapsackProblem[10])
# print(combination[10])
# print(np_booleanArray[37]) 
# print(np_knapsackProblem[37])
# print(combination[37])
