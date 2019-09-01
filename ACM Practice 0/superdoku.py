import sys

inp = [[int(num) for num in line.split()] for line in sys.stdin.read().splitlines()]

n, k = inp.pop(0)

print(n, k)

good = True

for line in inp:
    used = set()
    for num in line:
        if num in used:
            good = False
            break
        else:
            used.add(num)
    if not good:
        print("no")
        break

if good:
    for col in range(n):
        used - set()
        for line in inp:
            if line[col] in used:
                good = False
                break
            else:
                used.add(line[col])
        if not good:
            print("no")
            break

#if good:
    
