import json
import numpy as np
# from datetime import datetime

# Randomly generate item values and weights
# np.random.seed(42)

# start_time = datetime.now()

def pso(problemLength, value, weight, knapsackCapacity):
  # Problem Parameters
  n_items = problemLength  # Number of items
  max_weight = knapsackCapacity  # Knapsack capacity
  values = value
  weights = weight

  # PSO Parameters
  n_particles = 20
  max_iterations = 100
  w = 0.7  # Inertia weight
  c1, c2 = 1.5, 1.5  # Acceleration coefficients

  # Initialize particles
  X = np.random.randint(0, 2, (n_particles, n_items))  # Position matrix
  V = np.random.uniform(-1, 1, (n_particles, n_items))  # Velocity matrix
  pBest = X.copy()
  pBest_scores = np.array([0 if np.sum(weights * x) > max_weight else np.sum(values * x) for x in X])
  gBest = pBest[np.argmax(pBest_scores)].copy()
  gBest_score = np.max(pBest_scores)

  def sigmoid(x):
    return 1 / (1 + np.exp(-x))

  def repair_solution(solution):
    # """Ensures solution is within the weight constraint."""
    while np.sum(weights * solution) > max_weight:
      idx = np.where(solution == 1)[0]
      if len(idx) == 0:
        break
      worst_idx = idx[np.argmin(values[idx] / weights[idx])]
      solution[worst_idx] = 0
    return solution

  # PSO Loop
  for _ in range(max_iterations):
    for i in range(n_particles):
      # Update velocity
      r1, r2 = np.random.rand(n_items), np.random.rand(n_items)
      V[i] = w * V[i] + c1 * r1 * (pBest[i] - X[i]) + c2 * r2 * (gBest - X[i])
      
      # Update position using sigmoid function
      X[i] = (sigmoid(V[i]) > np.random.rand(n_items)).astype(int)
      X[i] = repair_solution(X[i])
      
      # Evaluate new solution
      fitness = np.sum(values * X[i]) if np.sum(weights * X[i]) <= max_weight else 0
      
      # Update personal best
      if fitness > pBest_scores[i]:
        pBest[i] = X[i].copy()
        pBest_scores[i] = fitness

    # Update global best
    if np.max(pBest_scores) > gBest_score:
      gBest = pBest[np.argmax(pBest_scores)].copy()
      gBest_score = np.max(pBest_scores)
    
  # Output best solution
  # print("Best value obtained:", gBest_score)
  # print("Best selection of items:", gBest)  
  
  return {
    'solValue': gBest_score,
    'solArray': gBest,
  }


# end_time = datetime.now()
# print(end_time - start_time)