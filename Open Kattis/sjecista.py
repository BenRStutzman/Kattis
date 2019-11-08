import sys

def main():
    N = int(sys.stdin.read().strip())
    verts = 0
    for i in range(1, N - 2):
        verts += i * (N - 2 - i)
    print(verts * N // 4)

main()
    
    
