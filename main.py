import numpy as np
# size = [100,200,500,1000, 2000,5000,10000]
# file = [1, 2, 3]

def problem(file, size):
  # File 1 from binary file to a np array where each line has become a list
  knapsackProblem = open(f"./Dataset/{file}/{size}/knapPI_{file}_{size}_1000_1", "r").readlines()
  new_knapsackProblem = np.array([x.split() for x in knapsackProblem], dtype=int).astype(int)

  # get first element cause it contains the total items and the knapsack's capacity
  problemLength, knapsackCapacity = new_knapsackProblem[:1][0] 
  # print('problemLength:', problemLength)
  # print('knapsackCapacity:',  knapsackCapacity)

  # get the rest cause it is the list of items for the 0/1 knapsack problem
  np_knapsackProblem = new_knapsackProblem[1:]
  # print(np_knapsackProblem)

  # File 3
  optimalKnapsackValue: int = int(open(f"./Dataset/{file}/{size}/knapPI_{file}_{size}_1000_1o", "r").read())
  # print('optimalKnapsackValue:', optimalKnapsackValue)

  value, weight = np_knapsackProblem.T

  return {
    'problemLength': problemLength,
    'value': value, 
    'weight': weight, 
    'knapsackCapacity': knapsackCapacity,
    'optimalKnapsackValue': optimalKnapsackValue
  }

def optimalSolution(file, size):  
  # File 2: Optimal Solution Array of 1 and 0 to NumPy Array of Boolean Values
  optimalSolution = open(f"./Dataset/{file}/{size}/knapPI_{file}_{size}_1000_1a", "r").read()
  np_booleanArray = np.array(optimalSolution.split(), dtype=int)
  # print(len(np_booleanArray))
  return np_booleanArray.tolist()