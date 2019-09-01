import sys

def main():
    
    bought, need = [[int(num) for num in line.split()] for line in sys.stdin.read().splitlines()]

    bought_props = [num / sum(bought) for num in bought]
    need_props = [num / sum(need) for num in need]
    worst_total = float('inf')

    for ing in range(3):
        total = bought_props[ing] * (sum(need) / need[ing])
        if total < worst_total:
            worst_total = total
            lim_ing = ing

    num_parts_used = bought[lim_ing] / need[lim_ing]

    for ing in range(2):
        used = num_parts_used * need[ing]
        print(bought[ing] - used, end = ' ')
    used = num_parts_used * need[2]
    print(bought[2] - used)
            
main()
