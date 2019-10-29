import sys

def main():
    inp = sys.stdin.read().splitlines()
    N = int(inp[0].split()[0])
    comp = []
    next_comp = []
    infects = []
    next_infects = []
    matrix = [[0 for i in range(N)] for i in range(N)]
    
    for line in inp[1:]:
        A,B = [int(num)-1 for num in line.split()]
        matrix[A][B] = 1
        matrix[B][A] = 1
        
    for node in range(N):
        neighbors = set([i for i in range(N) if matrix[node][i]])
        neighbors_and_me = neighbors.copy().union({node})
        if neighbors:
        #neighbors.append({node})
            for group in infects:
                if group.intersection(neighbors):
                    neighbors = neighbors.union(group)
                else:
                    next_infects.append(group)
            next_infects.append(neighbors)
        else:
            next_infects.append({node})
        infects = next_infects.copy()
        next_infects = []
        for group in comp:
            if group.intersection(neighbors_and_me):
                neighbors_and_me = neighbors_and_me.union(group)
            else:
                next_comp.append(group)
        next_comp.append(neighbors_and_me)
        comp = next_comp.copy()
        next_comp = []

    L = sum([1 for group in comp if len(group) == 1])
    #print(L)

    C = len(comp)
    I = len(infects)
    if (C - L) * 2 == (I - L):
        print(C)
    else:
        print(C - 1)
    
    '''
    print(matrix)            
    print(infects)
    print("\n\n")
    print(comp)
    links = len(comp) - 1
    '''
    
    
main()
