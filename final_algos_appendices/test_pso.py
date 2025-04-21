import numpy as np

def pso(problemLength, value, weight, knapsackCapacity, optimalKnapsackValue, population, n_iterations):
  # Problem Parameters
  n_items = problemLength  # Number of items
  max_weight = knapsackCapacity
  values = value
  weights = weight

  # PSO Parameters
  n_particles = population
  max_iterations = n_iterations
  w = 0.7  # Inertia weight
  c1, c2 = 1.5, 1.5  # Acceleration coefficients

  # Initialize particles
  X = np.random.randint(0, 2, (n_particles, n_items)) # Position matrix
  V = np.random.uniform(-1, 1, (n_particles, n_items)) # Velocity matrix
  
  pBest = X.copy()
  pBest_scores = np.array([0 if np.dot(x, weights) > max_weight else np.dot(x, values) for x in X])
  
  gBest = pBest[np.argmax(pBest_scores)].copy()
  gBest_score = np.max(pBest_scores)

  # Velocity to Probability Mapping:
  # In continuous PSO, particle velocities represent the step size and direction of movement. In BPSO, however, these velocities need to be converted to probabilities for binary decisions. This is achieved using the sigmoid function:
  def sigmoid(x):
    return 1 / (1 + np.exp(-x))
  
  def repair_solution(solution):
    # Ensures solution is within the weight constraint.
    while np.dot(solution, weights) > max_weight:
      idx = np.where(solution == 1)[0]
      if len(idx) == 0:
        break
      worst_idx = idx[np.argmin(values[idx] / weights[idx])]
      solution[worst_idx] = 0
    return solution

  best_SolutionPerIteration = np.array([], dtype=int)

  # PSO Loop
  for itr in range(max_iterations):
    for i in range(n_particles):
      # Update velocity
      r1, r2 = np.random.rand(n_items), np.random.rand(n_items)
      V[i] = w * V[i] + c1 * r1 * (pBest[i] - X[i]) + c2 * r2 * (gBest - X[i])
      
      # Update position using sigmoid function
      X[i] = (sigmoid(V[i]) > np.random.rand(n_items)).astype(int)
      X[i] = repair_solution(X[i])
      
      # Evaluate new solution
      fitness = np.dot(X[i], values) if np.dot(X[i], weights) <= max_weight else 0
      
      # Update personal best
      if fitness > pBest_scores[i]:
        pBest[i] = X[i].copy()
        pBest_scores[i] = fitness

    best_value = np.max(pBest_scores)
    best_SolutionPerIteration = np.append(best_SolutionPerIteration, best_value)
    
    # Update global best
    if best_value > gBest_score:
      gBest = pBest[np.argmax(pBest_scores)].copy()
      gBest_score = np.max(pBest_scores)
      
    if best_value == optimalKnapsackValue:
      return {
        'solValue': gBest_score.item(),
        'solWeight': np.dot(gBest, weights).item(),
        'solArray': gBest.tolist(),
        'numberIterations': itr+1,
        'best_SolutionPerIteration': best_SolutionPerIteration.tolist(),
      }

  return {
    'solValue': gBest_score.item(),
    'solWeight': np.dot(gBest, weights).item(),
    'solArray': gBest.tolist(),
    'numberIterations': max_iterations,
    'best_SolutionPerIteration': best_SolutionPerIteration.tolist(),
  }
