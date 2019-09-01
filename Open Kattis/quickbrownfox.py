import sys

def main():
    inp = sys.stdin.read().splitlines()
    for string in inp[1:]:
        chars = set(string)
        missing = ''
        for char in 'abcdefghijklmnopqrstuvwxyz':
            if not (char in chars or char.upper() in chars):
                missing += char
        if missing:
            print("missing", missing)
        else:
            print("pangram")
main()
