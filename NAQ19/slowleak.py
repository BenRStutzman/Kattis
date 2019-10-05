import sys

class Graph():
  
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] 
                      for row in range(vertices)]
  
    def printSolution(self, dist):
        print("Vertex Distance from Source")
        for node in range(self.V):
            print(node,"t",dist[node])
  
    # A utility function to find the vertex with 
    # minimum distance value, from the set of vertices 
    # not yet included in shortest path tree
    def minDistance(self, dist, sptSet):
  
        # Initialize minimum distance for next node
        minimum = 2 ** 31
  
        # Search not nearest vertex not in the 
        # shortest path tree
        for v in range(self.V):
            if dist[v] < minimum and sptSet[v] == False:
                minimum = dist[v]
                min_index = v
  
        return min_index

    # Function that implements Dijkstra's single source 
    # shortest path algorithm for a graph represented 
    # using adjacency matrix representation
    def dijkstra(self, src):
  
        dist = [2 ** 31] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
  
        for cout in range(self.V):
  
            # Pick the minimum distance vertex from 
            # the set of vertices not yet processed. 
            # u is always equal to src in first iteration
            u = self.minDistance(dist, sptSet)
  
            # Put the minimum distance vertex in the 
            # shortest path tree
            sptSet[u] = True
  
            # Update dist value of the adjacent vertices 
            # of the picked vertex only if the current 
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]:dist[v] = dist[u] + self.graph[u][v]

        return dist
        #self.printSolution(dist)


def main():
    inp = sys.stdin.read().splitlines()
    n, m, t, d = [int(num) for num in inp[0].split()]
    stations = [int(num) for num in inp[1]. split()]
    edges = [[int(num) for num in line.split()] for line in inp[2:]]
    #print(nodes)

    g  = Graph(n)
    for edge in edges:
        #print(edge)
        g.graph[edge[0] - 1][edge[1] - 1] = edge[2]
        g.graph[edge[1] - 1][edge[0] - 1] = edge[2]
    #print(g.graph)
    
    dists = g.dijkstra(0);
    print(dists)

            
            
    
    
main()
