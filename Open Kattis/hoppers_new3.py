import sys
import time

start_time = time.time()

def add_to_comp(node, left, matrix, group):
    for neighbor in matrix[node]:
        left.discard(neighbor)
        if neighbor not in group:
            group.add(neighbor)
            group = add_to_comp(neighbor, left, matrix, group)
    return group

def main():
    inp = sys.stdin.read().splitlines()
    N = int(inp[0].split()[0])

    #print("time-1:", time.time() - start_time)

    matrix = [set() for i in range(N)]
    for line in inp[1:]:
        A, B = [int(num) - 1 for num in line.split()]
        matrix[A].add(B)
        matrix[B].add(A)

    #print(matrix[0])

    #print("time0:", time.time() - start_time)

    i = 0

    
    infects = []
    next_infects = []
    for neighbors in matrix:
        for group in infects:
            if group.intersection(neighbors):
                neighbors = neighbors.union(group)
            else:
                next_infects += group
        

            
    #print(matrix)
    #print(matrix2)

    #print("time1:", time.time()- start_time)

    I = 0
    C = 0
    L = 0

    left = set([i for i in range(N)])
    while left:
        #print(left)
        node = left.pop()
        add_to_comp(node, left, matrix2, {node})
        I += 1
        
    if I == 1:
        print(0)
        return

    #print("time2:", time.time()- start_time)

    left = set([i for i in range(N)])
    while left:
        node = left.pop()
        if matrix[node]:
            add_to_comp(node, left, matrix, {node})
        else:
            L += 1
        C += 1

    #print("time3:", time.time()- start_time)

    #print("matrix: ", matrix)            
    #print("I:", I)
    #print("C:", C)
    #print("L:", L)
    #print("i:", i)
  
    
    if (C - L) * 2 == (I - L):
        print(C)
    else:
        print(C - 1)
    
main()
