import sys
import time

start_time = time.time()

def add_to_comp(node, left, matrix, group):
    for neighbor in matrix[node]:
        #print(group)
        left.discard(neighbor)
        if neighbor not in group:
            group.add(neighbor)
            group = add_to_comp(neighbor, left, matrix, group)
    return group

def find_odd(matrix, path):
    for neighbor in matrix[path[-1]]:
        if neighbor in path:
            if (len(path) - path.index(neighbor)) % 2:
                return True
        else:
            if find_odd(matrix, path + [neighbor]):
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

    #print(matrix[0])

    #print("time0:", time.time() - start_time)        

            
    #print(matrix)
    #print(matrix2)

    #print("time1:", time.time()- start_time)

    #print(matrix)

    left = set([i for i in range(N)])
    comps = []
    while left:
        node = left.pop()
        comps.append(add_to_comp(node, left, matrix, {node}))

    #print(comps)

    for comp in comps:
        if find_odd(matrix, [comp.pop()]):
            print(len(comps) - 1)
            return
        
    print(len(comps))

    #print("time3:", time.time()- start_time)
    
main()
