from sys import stdin, stdout
import time

def is_weak(node, graph, N):
    neighbors = [i for i in range(N) if graph[node][i]]
    #print(neighbors)
    for neighbor1 in neighbors:
        for neighbor2 in neighbors:
            if graph[neighbor1][neighbor2]:
                return False
    return True


start_time = time.time()
def main():
    inp = stdin.read().splitlines()
    out = []

    line = 0
    while inp[line] != "-1":
        weak = []
        N = int(inp[line])
        #print("N:", N)
        graph = [[int(num) for num in line.split()] for line in inp[line + 1:line + 1 + N]]
        #print("graph:", graph)

        for node in range(N):
            if is_weak(node, graph, N):
                weak.append(node)
                #print(weak)
            
        out.append(" ".join([str(num) for num in weak]))
        #print(out)
        
        line += N + 1

    stdout.write("\n".join(out))

main()

#print()
#print(time.time() - start_time)
