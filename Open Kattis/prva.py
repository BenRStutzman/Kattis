import sys

def main():
    inp = sys.stdin.read().splitlines()
    R, C = [int(num) for num in inp.pop(0).split()]
    #print(inp)
    words = []
    for row in range(R):
        #print("row:", row)
        col = 0
        while col < C:
            #print("col:", col)
            word = ''
            while col < C and inp[row][col] != '#':
                word += inp[row][col]
                col += 1
            if len(word) > 1:
                words.append(word)
            col += 1
    for col in range(C):
        row = 0
        while row < R:
            word = ''
            while row < R and inp[row][col] != '#':
                word += inp[row][col]
                row += 1
            if len(word) > 1:
                words.append(word)
            row += 1
    #print(words)
    print(sorted(words)[0])

main()
