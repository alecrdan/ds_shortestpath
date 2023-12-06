Author: Alec Daniels
Date: December 6, 2023

# Graph Traversal with BFS Algorithm

This Python script is designed to perform graph traversal using the Breadth-First Search (BFS) algorithm. It utilizes a custom `Graph` class to represent a graph and find the shortest path between two vertices.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

No specific installation is required.

### Usage

1. **Clone the Repository**
   _bash_
   git clone https://github.com/your/repository.git
   cd graph-traversal-bfs

2. **Follow the Instructions**
   - You will be prompted to enter the filename containing graph data. Ensure the file exists in the same directory or provide the full path.
   - Enter two vertices (integer indexes) between which you want to find the shortest path.

## Input File Format

The script expects an input file with the following format:

<number of vertices>
<vertex_1> <connected_vertex_1> <connected_vertex_2> ...
<vertex_2> <connected_vertex_1> <connected_vertex_2> ...

- The first line contains the total number of vertices in the graph.
- Subsequent lines contain vertex information followed by connected vertices.

## Output

- The script will output the total number of vertices in the provided graph.
- It will display the edges present in the graph.
- If a valid starting vertex is provided, it will find the shortest path using BFS between the specified vertices and display the path if found.

## Example

Consider an input file named `graph_data.txt`:

```
5
0 1 2
1 0 2 3
2 0 1 4
3 1 4
4 2 3
```

- Running the script and providing `graph_data.txt` as input would prompt for two vertices.
- Entering `0 4` would output:
  ```
  Number of vertices: 5
  Edges in the graph: [(0, 1), (0, 2), (1, 0), (1, 2), (1, 3), (2, 0), (2, 1), (2, 4), (3, 1), (3, 4), (4, 2), (4, 3)]
  Path from 0 to 4: [0, 2, 4]
  ```

---
