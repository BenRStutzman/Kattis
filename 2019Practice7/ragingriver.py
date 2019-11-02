import sys

class Graph():
  
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] 
                      for row in range(vertices)]
        self.ROW = len(self.graph)

  
##    def printSolution(self, dist):
##        print ("Vertex tDistance from Source")
##        for node in range(self.V):
##            print (node,"t",dist[node])
##
##
##    def minDistance(self, dist, sptSet):
##      
##            # Initialize minimum distance for next node
##        min = float('inf')
##      
##            # Search not nearest vertex not in the 
##            # shortest path tree
##        for v in range(self.V):
##            if dist[v] < min and sptSet[v] == False:
##                min = dist[v]
##                min_index = v
##        return min_index
##                
##
##    def dijkstra(self, src):
##      
##        dist = [float('inf')] * self.V
##        dist[src] = 0
##        sptSet = [False] * self.V
##      
##        for cout in range(self.V):
##      
##                # Pick the minimum distance vertex from 
##                # the set of vertices not yet processed. 
##                # u is always equal to src in first iteration
##            u = self.minDistance(dist, sptSet)
##      
##                # Put the minimum distance vertex in the 
##                # shortest path tree
##            sptSet[u] = True
##      
##                # Update dist value of the adjacent vertices 
##                # of the picked vertex only if the current 
##                # distance is greater than new distance and
##                # the vertex in not in the shortest path tree
##            for v in range(self.V):
##                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]:
##                    dist[v] = dist[u] + self.graph[u][v]
##      
##        #self.printSolution(dist)

    def BFS(self, s, t, parent):

        # Mark all the vertices as not visited
        visited = [False] * self.ROW

        # Create a queue for BFS
        queue = []

        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True

        # Standard BFS Loop
        while queue:

            # Dequeue a vertex from queue and print it
            u = queue.pop(0)

            # Get all adjacent vertices of the dequeued vertex u
            # If a adjacent has not been visited, then mark it
            # visited and enqueue it
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        # If we reached sink in BFS starting from source, then return
        # true, else false
        return visited[t]

    # Returns the maximum flow from s to t in the given graph
    def FordFulkerson(self, source, sink, mx):

        # This array is filled by BFS and to store path
        parent = [-1] * self.ROW

        max_flow = 0 # There is no flow initially
        many=0

        # Augment the flow while there is path from source to sink
        while self.BFS(source, sink, parent):

            # Find minimum residual capacity of the edges along the
            # path filled by BFS. Or we can say find the maximum flow
            # through the path found.
            path_flow = float("Inf")
            s = sink
            while (s != source):
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            # Add path flow to overall flow
            max_flow += path_flow

            # Update residual capacities of the edges and reverse edges
            # along the path
            v = sink
            while (v != source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
            if (max_flow>=mx):
                return max_flow,many

        return max_flow,many



def main():
    inp = sys.stdin.read().splitlines()
    p = int(inp[0].split()[0])
    r = int(inp[0].split()[1])
    l = int(inp[0].split()[2])
    g = [[0 for i in range(r+2)] for i in range(r+2)]
    for line in inp[1:]:
        a = int(line.split()[0])
        b = int(line.split()[1])
        g[a][b]=1
        g[b][a]=1
    #print(g)
    #print()
    G = Graph(r+2)
    G.graph = g
    source = -1
    sink = -2
    acc,many=G.FordFulkerson(source, sink,p)
    if(acc<p):
        print(p-acc,"people left behind")
    else:
        numb = 0
        for row in G.graph:
            for el in row:
                if (el==2):
                    numb += 1
        print(numb)
        #print(G.graph)
    #G.dijkstra(-2)
    #print(G)
    


main()
