import sys

def main():
    inp = [[int(num) for num in line.split()] for line in sys.stdin.read().splitlines()]
    T = int(inp[0][0])
    for ln in range(2, 2 * T + 1, 2):
        checked = set()
        for ID, card in enumerate(inp[ln]):
            ID += 1
            if ID not in checked:
                loop = {ID}
                cur_card = card
                while cur_card not in loop:
                    loop.add(cur_card)
                    cur_card = inp[ln][cur_card - 1]
                checked = checked.union(loop)
                #print("loop:", loop)
                if len(loop) not in {2 ** i for i in range(11)}:
                    print("Some starve.")
                    break
        else:
            print("All can eat.")

main()
            
        
