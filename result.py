import numpy as np

# gbest = array solution 
# np_booleanArray = from dataset solution

# TESTING FINAL SOLUTION
decrepancy = np.array([])
for i in range(len(gBest)):
  if gBest[i] != np_booleanArray[i]:
    description = 'object not counted' if np_booleanArray[i] == 1 else 'should not be included'
    decrepancy = np.append(decrepancy, {
      'index': i,
      'weight': weight[i].item(),
      'value': value[i].item(),
      'pso_value': gBest[i].item(),
      'optimal_value': np_booleanArray[i].item(),
      'description': description,
    })

sol_weight = np.dot(gBest, weight)
opti_weight = np.dot(np_booleanArray, weight)

print('sol_weight', sol_weight)
print('opti_weight', opti_weight)

with open('out.json', 'w') as outfile:
  json.dump(decrepancy.tolist(), outfile)

# FINAL DISCREPANCY
# Compare finalSol to optiSol
optiSolution = optimalSolution(set, size)
decrepancy = []    
for idx in range(prob['problemLength']):
  if (optiSolution[idx] == 1 and algo['solArray'][idx] == 0):
    decrepancy.append({
      'index': idx,
      'value': prob['value'][idx].item(),
      'weight': prob['weight'][idx].item(),
      'case': 'O=1, S=0, should be in Solution', 
    })
  if (optiSolution[idx] == 0 and algo['solArray'][idx] == 1):
    decrepancy.append({
      'index': idx,
      'value': prob['value'][idx].item(),
      'weight': prob['weight'][idx].item(),
      'case': 'O=0, S=1, should not be in Solution', 
    })