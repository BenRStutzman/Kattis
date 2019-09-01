import sys

def main():

    inp = sys.stdin.read().splitlines()
    N = int(inp[0])

    for ln in range(1, 2 * N + 1, 2):
        str1, str2 = inp[ln], inp[ln + 1]
        diffs = ''
        for char in range(len(str1)):
            if str1[char] == str2[char]:
                diffs += '.'
            else:
                diffs += '*'
        print(str1)
        print(str2)
        print(diffs, end = "\n\n")
            
main()
