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

def add_to_infect(node, left, matrix, group):
    for neighbor in matrix[node]:
        for next_neighbor in matrix[neighbor]:
            left.discard(next_neighbor)
            if next_neighbor not in group:
                group.add(next_neighbor)
                group = add_to_infect(next_neighbor, left, matrix, group)
    return group

def main():
    inp = sys.stdin.read().splitlines()
    N = int(inp[0].split()[0])

    '''
    matrix = [[0 for i in range(N)] for i in range(N)]
    
    for line in inp[1:]:
        A,B = [int(num) - 1 for num in line.split()]
        matrix[A][B] = 1
        matrix[B][A] = 1
    '''

    matrix = {}
    for line in inp[1:]:
        A, B = [int(num) - 1 for num in line.split()]
        if A in matrix:
            matrix[A].add(B)
        else:
            matrix[A] = {B}
        if B in matrix:
            matrix[B].add(A)
        else:
            matrix[B] = {A}

    #print(matrix)

    #print(time.time()- start_time)

    I = 0
    C = 0
    L = 0

    left = set([i for i in range(N)])
    while left:
        node = left.pop()
        if node in matrix:
            add_to_infect(node, left, matrix, {node})
        I += 1

    if I == N:
        print(0)
        return

    #print(time.time()- start_time)

    left = set([i for i in range(N)])
    while left:
        node = left.pop()
        if node in matrix:
            add_to_comp(node, left, matrix, {node})
        else:
            L += 1
        C += 1

    #print(time.time()- start_time)

    #print(matrix)            
    #print(I)
    #print(C)
    #print(L)
  
    
    if (C - L) * 2 == (I - L):
        print(C)
    else:
        print(C - 1)
    
main()
