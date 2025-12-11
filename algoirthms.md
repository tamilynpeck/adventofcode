Advent of Code (AoC) is a fantastic way to practice your algorithmic skills. While the problems vary widely, there are several key algorithms, data structures, and concepts that appear frequently. Knowing these will significantly improve your efficiency and ability to solve tougher problems.

Here are the essential algorithms and concepts you should be familiar with for Advent of Code:

### 1. 🗺️ Graph Algorithms & Traversals

Many AoC puzzles can be modeled as graphs (like mazes, grids, or interconnected systems).

- **Breadth-First Search (BFS):**
  - **Purpose:** Finding the **shortest path** (in terms of steps/edges) from a starting point to an end point. Excellent for mazes, minimum-step problems, and finding the shortest number of moves.
- **Depth-First Search (DFS):**
  - **Purpose:** Exploring all possible paths or visiting every node. Useful for complex pathfinding, checking connectivity, and many tree/grid traversals. Often used recursively.
- **Dijkstra's Algorithm / A\* Search:**
  - **Purpose:** Finding the **lowest-cost path** in a graph where edges have different weights/costs. Crucial for problems like minimum-risk pathfinding (AoC Day 15 is a classic example). A\* is an optimized version that uses a heuristic to guide the search.

### 2. 🌳 Tree Structures & Dynamic Programming

- **Recursion & Memoization (Dynamic Programming):**
  - **Purpose:** Breaking down a large problem into smaller, overlapping subproblems.
  - **When to Use:** Problems involving sequences, arrangements, or calculating a value based on previous results (e.g., counting valid paths, maximizing a score). **Memoization** (caching results) is vital to prevent exponential complexity.
- **Tree/Trie Traversal:**
  - **Purpose:** Handling hierarchical data or large sets of strings/numbers where common prefixes are important.

### 3. 🔢 Common Algorithmic Patterns

- **Sorting and Searching:**
  - Standard sorting algorithms (merge sort, quicksort, etc.) and knowing how to use your language's built-in sort efficiently.
  - **Binary Search:** Essential for quickly finding an element or solution within a large, sorted range.
- **Greedy Algorithms:**
  - **Purpose:** Making the locally optimal choice at each step with the hope of finding a global optimum. This doesn't always work, but it's a fast solution for certain specific problems (like scheduling or coin exchange).
- **Two Pointers / Sliding Window:**
  - **Purpose:** Efficiently processing sequences (arrays/strings). The **Sliding Window** technique is great for finding the longest/shortest subarray/substring that satisfies a condition.

### 4. 🔗 Data Structures You Must Master

The right data structure can turn an $\mathcal{O}(N^2)$ solution into an $\mathcal{O}(N)$ solution.

- **Hash Maps / Dictionaries / Sets:**
  - **Why:** For $\mathcal{O}(1)$ average time complexity lookups, insertions, and deletions. Absolutely critical for counting frequencies, tracking seen items, and mapping data.
- **Priority Queues (Heaps):**
  - **Why:** Essential for implementing Dijkstra's algorithm efficiently. They allow for $\mathcal{O}(\log N)$ insertion and $\mathcal{O}(\log N)$ retrieval of the minimum (or maximum) element.

### 5. 🔬 Math & Logic (The AoC 'Spice')

Many problems aren't about complex computer science algorithms but about clever mathematical observation.

- **Number Theory:**
  - **GCD (Greatest Common Divisor) & LCM (Least Common Multiple):** Crucial for loop/cycle finding problems (often in Day 8/20+).
  - **Prime Factorization:** Used in resource allocation or complex division problems.
- **Combinatorics:**
  - **Permutations and Combinations:** Knowing how to generate them or calculate their count.
- **Simulation and State Management:**
  - Many puzzles are about simply simulating a complex system. Knowing how to efficiently represent the **state** of the system and detect **cycles** (when the system enters a previously seen state) is key to solving puzzles that run for billions of iterations.

---

### 💡 Strategy for AoC

For any given problem:

1.  **Read Carefully:** Identify the inputs, outputs, and constraints.
2.  **Identify the Core Concept:** Is it a shortest path problem (BFS/Dijkstra)? A counting problem (Dynamic Programming)? A mapping/lookup problem (Hash Maps)?
3.  **Analyze Complexity:** Check if your initial idea will run in time. If the input size $N$ is up to $10^5$, you usually need an $\mathcal{O}(N \log N)$ or $\mathcal{O}(N)$ solution. If $N$ is small ($\le 20$), you might get away with an $\mathcal{O}(2^N)$ or $\mathcal{O}(N!)$ solution.
