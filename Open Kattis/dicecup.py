M, N = [int(num) for num in input().split()]

outcomes = {i: 0 for i in range(2, M + N + 1)}

for i in range(1, M + 1):
    for j in range(1, N + 1):
        outcomes[i + j] += 1

sorted_outcomes = sorted(outcomes.items(), key = lambda pair: pair[1], reverse = True)

record = sorted_outcomes[0][1]

i = 0

while sorted_outcomes[i][1] == record:
    print(sorted_outcomes[i][0])
    i += 1
