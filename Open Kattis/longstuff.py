import sys
import time
import random

[left, right] = [int(num) for num in sys.stdin.read().split()]

#print('test')

if False:
    for i in range(0):
        if left == right:
            if left:
                print('Even', 2 * left)
            else:
                print('Not a moose')
        else:
            print('odd', 2 * max(left, right))

for i in range(100):
    time.sleep(0.08)
    print('test case:' , i)
    print('solution found.')
    print('solution:', random.randint(1, 100000))
