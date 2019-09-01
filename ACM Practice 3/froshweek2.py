import sys
from collections import deque

def ispal(num):
    return str(num)[:3] == str(num)[5:2:-1]

def main():
    
    [z, q], Z, Q = [[int(num) for num in line.split()] for line in sys.stdin.read().splitlines()]
    Z, Q = deque(sorted(Z, reverse = True)), deque(sorted(Q, reverse = True))

    tasks_completed = 0
    
    while Z:
        task_length = Z.pop()
        while Q:
            int_length = Q.pop()
            if task_length <= int_length:
                tasks_completed += 1
                break

    print(tasks_completed)
    
main()
