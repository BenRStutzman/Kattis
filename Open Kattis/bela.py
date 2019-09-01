points = {'A': 11, 'K': 4, 'Q': 3, 'J': 2, 'T': 10, '9': 0, '8': 0, '7': 0}

N, D = input().split()

score = 0

for i in range(4 * int(N)):
    card = input()
    if card[1] == D:
        if card[0] == 'J':
            score += 18
        elif card[0] == '9':
            score += 14
    score += points[card[0]]

print(score)
