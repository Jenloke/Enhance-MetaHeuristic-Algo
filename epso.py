import numpy as np

def epso(problemLength, value, weight, knapsackCapacity, optimalKnapsackValue, particles, n_iterations):
  # Problem Parameters
  n_items = problemLength  # Number of items
  max_weight = knapsackCapacity  # Knapsack capacity
  values = value
  weights = weight

  # EPSO Parameters
  n_particles = particles
  max_iterations = n_iterations
  w = 0.7  # Inertia weight
  c1, c2 = 1.5, 1.5  # Acceleration coefficients
  # c1, c2 = 0.5, 0.5

  def repair_solution(solution):
    # Ensures solution is within the weight constraint.
    while np.dot(solution, weights) > max_weight:
      idx = np.where(solution == 1)[0]
      if len(idx) == 0:
        break
      worst_idx = idx[np.argmin(values[idx] / weights[idx])]
      solution[worst_idx] = 0
    return solution

  def greedy_solution(weights, values, capacity):
    # Generates a greedy solution based on value-to-weight ratio
    num_items = len(weights)
    
    # Calculate value-to-weight ratios
    ratios = [(i, values[i] / weights[i]) for i in range(num_items)]
    # Sort by ratio in descending order
    ratios.sort(key=lambda x: x[1], reverse=True)
    
    solution = np.zeros(num_items)
    total_weight = 0
    
    for idx, _ in ratios:
      if total_weight + weights[idx] <= capacity:
        solution[idx] = 1
        total_weight += weights[idx]
    
    print('greedy solution value', np.dot(value, solution))
    return solution
  
  def initialize_particles(weights, values, capacity, n_particles, n_items):
    #Initialize particles using greedy solution with random perturbations
    particles = np.zeros((n_particles, n_items))
    
    # Start with greedy solution
    greedy = greedy_solution(weights, values, capacity)
    
    for i in range(n_particles):
      if i == 0:
        # Keep one pure greedy solution
        particles[i] = greedy
      else:
        # Create perturbations of greedy solution
        particles[i] = greedy.copy()
        
        # Randomly flip some bits (with higher probability for 0s)
        for j in range(n_items):
          if particles[i][j] == 1 and np.random.rand() < 0.2:
            particles[i][j] = 0
          elif particles[i][j] == 0 and np.random.rand() < 0.25:
            particles[i][j] = 1
        
        # Repair if needed
        particles[i] = repair_solution(particles[i])

    return particles
  
  # Initialize particles
  X = initialize_particles(weights, values, max_weight, n_particles, n_items)
  V = np.random.uniform(-1, 1, (n_particles, n_items)) # Velocity matrix
  
  pBest = X.copy()
  pBest_scores = np.array([0 if np.dot(x, weights) > max_weight else np.dot(x, values) for x in X])
  
  gBest = pBest[np.argmax(pBest_scores)].copy()
  gBest_score = np.max(pBest_scores)

  # Velocity to Probability Mapping:
  # In continuous PSO, particle velocities represent the step size and direction of movement. In BPSO, however, these velocities need to be converted to probabilities for binary decisions. This is achieved using the sigmoid function:
  def sigmoid(x):
    return 1 / (1 + np.exp(-x))
  
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
    'numberIterations': max_iterations,
  }
