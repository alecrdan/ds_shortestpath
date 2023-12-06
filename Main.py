from Graph import Graph
import os.path
import sys


# Get the file
filename = input("Enter a file: ").strip()
if not os.path.isfile(filename):
    print(filename, "does not exist")
    sys.exit()

# Take input for two vertices (integer indexes)
try:
    start_vertex, end_vertex = map(int, input(
        "Enter two vertices (space-separated): ").split())
except:
    print("Please use the proper format")
    print(" e.g. 1 3 ")
    sys.exit(1)

inputFile = open(filename, "r")
lines = inputFile.readlines()
inputFile.close()


# Read the vertices and print
num_vertices = int(lines[0])
print("Number of vertices:", num_vertices)

vertices = list(range(num_vertices))
edges = []

for line in lines[1:]:
    tokens = [int(x) for x in line.split()]

    starting_vertex = tokens[0]
    for adjacent_vertex in tokens[1:]:
        edges.append([starting_vertex, adjacent_vertex])


# Call graph constructor and print edges
graph = Graph(vertices, edges)

# Print Edges
print("Edges in the graph:", graph.getEdges())

# Call bfs function
path_tree = graph.bfs(start_vertex)

# Print the path
if path_tree:
    path = path_tree.getPath(end_vertex)
    if path:
        print(f"Path from {start_vertex} to {end_vertex}: {path}")
    else:
        print(f"No path found from {start_vertex} to {end_vertex}")
else:
    print("Invalid starting vertex")
