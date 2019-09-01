import sys

[L, D, X] = [int(num) for num in sys.stdin.readlines()]

min_summer = D
max_summer = L

for i in range(L, D + 1):
    sum = 0
    for char in str(i):
        sum += int(char)
    if sum == X:
        if i < min_summer:
            min_summer = i
        elif i > max_summer:
            max_summer = i

print(min_summer)
print(max_summer)
