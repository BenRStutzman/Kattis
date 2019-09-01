N = int(input())

numerator = 0

results = [int(num) for num in input().split()]
for result in results:
    if result >= 0:
        numerator += result
    else:
        N -= 1

print(numerator / N)
