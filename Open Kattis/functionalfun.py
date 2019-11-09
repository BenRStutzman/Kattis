import sys

def main():

    inp = [line.split() for line in sys.stdin.read().splitlines()]
    line = 0
    while line < len(inp):
        function = True
        injective = True
        domain, codomain, N = inp[line : line + 3]
        #print(domain, codomain, N)
        N = int(N[0])
        domain = set(domain[1:])
        codomain = set(codomain[1:])
        mappings = {}
        line += 3
        for i in range(line, line + N):
            x, y = inp[i][0], inp[i][2]
            if x in mappings:
                if mappings[x] != y:
                    print("not a function")
                    function = False
                    break
            else:
                mappings[x] = y
                if y in codomain:
                    codomain.remove(y)
                else:
                    injective = False
        line += N
        if function:
            surjective = not codomain
            if surjective:
                if injective:
                    print("bijective")
                else:
                    print("surjective")
            else:
                if injective:
                    print("injective")
                else:
                    print("neither injective nor surjective")


main()
