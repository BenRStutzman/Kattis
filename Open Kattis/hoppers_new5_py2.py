import sys
import time
import Queue

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

    q = Queue.Queue()
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
    inp = [[int(num) - 1 for num in line.split()] for line in sys.stdin.read().splitlines()]
    N = inp[0][0] + 1

    #print("time-1:", time.time() - start_time)

    matrix = [set() for i in range(N)]
    
    for A, B in inp[1:]:
        matrix[A].add(B)
        matrix[B].add(A)

    #print("Time2:", time.time() - start_time)


    left = set([i for i in range(N)])
    comps = []
    C = 0
    while left:
        node = left.pop()
        comps.append(add_to_comp(node, left, matrix, {node}).pop())
        C += 1

    #print("time2:", time.time() - start_time)

    for comp in comps:
        if find_odd(matrix, comp, N):
            print C - 1
            return
        
    print C 
    
main()

#print("time3:", time.time()- start_time)
