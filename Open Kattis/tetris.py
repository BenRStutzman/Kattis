import sys

def check_fits(columns, edges, C):
    count = 0
    for edge in edges:
        for i in range(C + 1 - len(edge)):
            start = columns[i] - edge[0]
            for j in range(1, len(edge)):
                if columns[i + j] - edge[j] != start:
                    break
            else:
                count += 1
    return count

def main():

    edges = [[[0], [0, 0, 0, 0]], [[0, 0]], [[0, 0, 1], [1, 0]], [[1, 0, 0], [0, 1]],
                [[0, 0, 0], [1, 0], [0, 1], [1, 0, 1]], [[0, 0, 0], [0, 0], [2, 0],
                [0, 1, 1]], [[0, 0, 0], [0, 0], [0, 2], [1, 1, 0]]]

    
    inp = [[int(num) for num in line.split()] for line in sys.stdin.read().splitlines()]
    C, P = inp[0]
    print(check_fits(inp[1], edges[P - 1], C))

main()
    
    
