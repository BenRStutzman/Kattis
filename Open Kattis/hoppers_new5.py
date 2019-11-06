import sys
import time
import queue

start_time = time.time()

def add_to_comp(node, left, matrix, group):
    for neighbor in matrix[node]:
        #print(group)
        left.discard(neighbor)
        if neighbor not in group:
            group.add(neighbor)
            group = add_to_comp(neighbor, left, matrix, group)
    return group

def find_odd(matrix, node, N):
    color_arr = [-1] * N
    color_arr[node] = 1

    q = queue.Queue()
    q.put(node)

    while (not q.empty()):

        u = q.get()
        neighbors = matrix[u]

        for v in range(N):
            if v in neighbors and color_arr[v] == -1:
                color_arr[v] = 1 - color_arr[u]
                q.put(v)
            elif v in neighbors and color_arr[v] == color_arr[u]:
                return True
    return False

    

def main():
    inp = sys.stdin.read().splitlines()
    N = int(inp[0].split()[0])

    #print("time-1:", time.time() - start_time)

    matrix = [set() for i in range(N)]
    
    for line in inp[1:]:
        A, B = [int(num) - 1 for num in line.split()]
        matrix[A].add(B)
        matrix[B].add(A)

    #print("Time2:", time.time() - start_time)


    left = set([i for i in range(N)])
    comps = []
    while left:
        node = left.pop()
        comps.append(add_to_comp(node, left, matrix, {node}).pop())

    #print("time2:", time.time() - start_time)

    for comp in comps:
        if find_odd(matrix, comp, N):
            print(len(comps) - 1)
            return
        
    print(len(comps))
    
main()

#print("time3:", time.time()- start_time)
