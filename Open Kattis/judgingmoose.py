import sys

[left, right] = [int(num) for num in sys.stdin.read().split()]

#print('test')

if left == right:
    if left:
        print('Even', 2 * left)
    else:
        print('Not a moose')
else:
    print('odd', 2 * max(left, right))

