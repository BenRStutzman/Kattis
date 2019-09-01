import sys

def main():
    john, doc = sys.stdin.read().splitlines()
    if len(john) >= len(doc):
        print("go")
    else:
        print("no")

main()
