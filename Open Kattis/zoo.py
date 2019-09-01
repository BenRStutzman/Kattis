import sys

def main():
    inp = sys.stdin.read().splitlines()
    start_ln = 0
    list_num = 1
    while True:
        if inp[start_ln] == '0':
            break
        N = int(inp[start_ln])
        animals = {}
        for ln in range(start_ln + 1, start_ln + N + 1):
            animal = inp[ln].split()[-1].lower()
            animals[animal] = animals.get(animal, 0) + 1
        print("List %d:" % list_num)
        for animal in sorted(animals):
            print("%s | %d" % (animal, animals[animal]))
        list_num += 1
        start_ln += N + 1

main()
