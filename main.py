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

knapsackProblem = open(f"./Dataset/{1}/{100}/knapPI_{1}_{100}_1000_1", "r").read()
optimalSolution = open(f"./Dataset/{1}/{100}/knapPI_{1}_{100}_1000_1a", "r").read()
optimalKnapsackValue = open(f"./Dataset/{1}/{100}/knapPI_{1}_{100}_1000_1o", "r").read()
