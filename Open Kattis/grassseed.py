cost = float(input())
N = int(input())

total_footage = 0

for i in range(N):
    [length, width] = [float(num) for num in input().split()]
    total_footage += length * width

print(total_footage * cost)
