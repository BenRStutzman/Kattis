import sys

def main():
    inp = sys.stdin.read().splitlines()
    name1, name2 = inp[0].split()
    if name1[-2:] == 'ex':
        name1 = name1[:-2]
    elif name1[-1] in 'aeiou':
        name1 = name1[:-1]
    print(name1 + 'ex' + name2)

main()
