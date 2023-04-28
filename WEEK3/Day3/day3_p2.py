'''
BELLMAN FORD ALGORITHM
'''

from sys import maxsize


# The row graph[i] represents i-th edge with three values u, v and w.
def BellmanFord(graph, V, E, src):
    # Initialize infinite for all vertices except source
    dis = [maxsize] * V
    # initialize distance of a source as 0
    dis[src] = 0
    # Relax all edges |v| - 1 times. A simple shortest path from src to any other
    # vertex can have atmost |V| - 1 edge

    for i in range(V - 1):
        for j in range(E):
            if dis[graph[j][0]] + graph[j][2] < dis[graph[j][1]]:
                dis[graph[j][1]] = dis[graph[j][0]] + graph[j][2]

        # check for negative weight cycles
    for i in range(E):
         x = graph[i][0]
         y = graph[i][1]
         weight = graph[i][2]
         if dis[x] != maxsize and dis[x] + weight < dis[y]:
             print("Graph contains negative weights")

    print("Vertex Distance from source")
    for i in range(V):
        print("%d\t\t%d" % (i, dis[i]))


if __name__ == "__main__":
    V = 5  # Number of vertices in the graph
    E = 8  # Number of edges in the graph
    graph = [[0, 1, -1], [0, 2, 4],
             [1, 2, 3], [1, 3, 2],
             [1, 4, 2], [3, 2, 5],
             [3, 1, 1], [4, 3, -3]]
    BellmanFord(graph, V, E, 0)
