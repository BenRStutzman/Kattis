import sys

N = int(sys.stdin.readline())
winning_schools = []

for i in range(N):
    [school, team] = sys.stdin.readline().split()
    if school not in winning_schools:
        print(school, team)
        winning_schools.append(school)
        if len(winning_schools) == 12:
            break
