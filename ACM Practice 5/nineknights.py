import sys

def isValid(lines):
    num_knights = 0
    for line in lines:
        num_knights += line.count('k')
    if num_knights != 9:
        return False

    for line in range(5):
        for col in range(5):
            if lines[line][col] == 'k':
                for combo in [[-2, -1], [-2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2], [2, -1], [2, 1]]:
                    if (line + combo[0] in range(5) and col + combo[1] in range(5)):
                        if lines[line + combo[0]][col + combo[1]] == 'k':
                            #print(line + combo[0], col + combo[1])
                            return False
    return True

def main():
    lines = sys.stdin.read().splitlines()
    if isValid(lines):
        print("valid")
    else:
        print("invalid")
                        
main()
