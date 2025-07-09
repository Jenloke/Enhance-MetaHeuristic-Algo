# Enhancing a Metaheuristic Optimization Algorithm for the 0/1 Knapsack Problem

Metaheuristic algorithms (natured inspired algorithms) for the 0/1 Knapsack Problem, a NP hard problem where the goal is to select the most optimal items that satisfies the given knapsack weight from a collection of items based on weight profit ratio, measuring their performance and enhancing the most optimal one based on results.

### 🗝 Key Metrics for the Algorithm's Performance

- **Optimality Rate** - how close the algorithms total knapsack value is to the given optimum knapsack value
- **Convergence Speed** - how fast the algorithm finished computing for the optimum knapsack value, measured in time taken, seconds
- **Space Complexity** - the memory taken by the algorithm during its runtime, measured in average memory usage, kilobytes

### 📈 Algorithms Used

- **Harmony Serach Algorithm** - population-based metaheuristic optimization method inspired by the improvisation process of musicians. Just like musicians search for a perfect state of harmony by trying different combinations of pitches, HSA searches for the optimal solution by iteratively generating and adjusting solution candidates.
- **Particle Swarm Algorithm** - a population-based metaheuristic optimization algorithm inspired by the social behavior of bird flocks and fish schools. It searches for optimal solutions by having a group of candidate solutions — called particles — move through the problem space, adjusting their positions based on their own experience and their neighbors' experiences.

### ✨ Enhancement

The best algorithm out of the two is to be enhanced using **Greedy Initialization**, to address a major drawback of Metaheuristic Algorithm of being stuck in local optima — most optimal solution from a local search space — than global optima, the true optimal solution from the whole search scope, with this drawback better initialization from the enhancement would overcome this.

### 📊 Visualization

Using _Jupyter Notebook_, the visualization of convergence speed was demonstrated using line chart in 2 axes, the x-axis being number of iterations and the y-axis being the computed knapsack value of the algorithm. Comparing runs of two algorithms per line chart across different problem instances of the 0/1 knapsack problem.

### 🛠 Technologies Used

- Python
- Jupyter Notebook
- Matplotlib
- NumPy
- Pandas

### 🏃 Running the REPO

1. Clone the repository
2. Install technologies used using pip
3. Run _test.py_

---

### 🐱‍💻 The Team

- [John Pol M. Jalapan](https://github.com/PolJalapan)
- [Jenloke N. Magbojos](https://github.com/Jenloke)
- [Alain Micko C. Moreno](https://github.com/Araniala)

#### Thesis Adviser: [Fatima Marie P. Agdon, MSCS](https://github.com/marieemoiselle)
