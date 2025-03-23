import numpy as np

# size = [100,200,500,1000, 2000,5000,10000]
# file = [1, 2, 3]

def problem(file, size):
  # file = 1
  # size = 100

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
  # combination = np.stack((value, weight, np_booleanArray), axis=1)

  # print(np_booleanArray)
  # print(np.dot(np_booleanArray, value))

  return {
    'problemLength': problemLength,
    'value': value, 
    'weight': weight, 
    'knapsackCapacity': knapsackCapacity
  }
  

  # Correct
  # print(len(np_booleanArray))
  # print(len(weight))
  # print(len(value))
  # print(np_booleanArray)
  # print(weight)
  # print(value)

  # print(np_booleanArray[37])
  # print(np_knapsackProblem[37])
  # print(combination[37])
  
  # File 2
  # Optimal Solution Array of 1 and 0 to NumPy Array of Boolean Values
  # optimalSolution = open(f"./Dataset/{file}/{size}/knapPI_{file}_{size}_1000_1a", "r").read()
  # np_booleanArray = np.array(optimalSolution.split(), dtype=int).astype(bool)
  # np_booleanArray = np.array(optimalSolution.split(), dtype=int)
  # print(len(np_booleanArray))