import sys

[p, q, s] = [int(num) for num in input().split()]

for i in range(1, s + 1):
    if i % p == 0 and i % q == 0:
        print("yes")
        break
else:
    print("no")
