import sys

def main():
    encoded, keyword = sys.stdin.read().splitlines()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    decoded = ''
    for i, char in enumerate(encoded):
        keyword += alpha[(alpha.index(char) - alpha.index(keyword[i])) % 26]

    print(keyword[len(keyword) - len(encoded):])
        
main()
