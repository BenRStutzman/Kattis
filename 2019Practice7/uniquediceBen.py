import sys

def general(die):
    [[a1, a2], [b1, b2], [c1, c2]] = die
    flips = 0
    if a1 == a2 or b1 == b2 or c1 == c2:
        return sorted([sorted(pair) for pair in die])
    if a1 > a2:
        flips += 1
    if b1 > b2:
        flips += 1
    if c1 > c2:
        flips += 1
    die = [sorted(pair) for pair in die]
    if die[0] == die[1] or die[0] == die[2] or die[1] == die[2]:
        return sorted(die)
    if die[0] > die[1]:
        flips += 1
    if die[1] > die[2]:
        flips += 1
    if die[0] > die[2]:
        flips += 1
    die = sorted(die)
    if flips % 2:
        die[2] = die[2][::-1]
    return sorted(die)

def main():
    inp = sys.stdin.read().splitlines()
    N = int(inp[0])
    dice = []
    for line in range(1, N + 1):
        die = []
        for pair in range(3):
            die.append([inp[line][pair * 4], inp[line][pair * 4 + 2]])
        dice.append(die)
    uniques = {}
    for die in dice:
        die = general(die)
        die = "".join(die[0]) + "".join(die[1]) + "".join(die[2])
        uniques[die] = uniques.get(die, 0) + 1
    print(max(uniques.values()))


    
        

    
main()
