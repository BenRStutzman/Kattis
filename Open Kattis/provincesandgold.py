import sys

def main():
    inp = [int(num) for num in input().split()]
    total = 3 * inp[0] + 2 * inp[1] + inp[2]
    
    if total >= 8: print("Province or ", end = "")
    elif total >= 5: print("Duchy or ", end = "")
    elif total >= 2: print("Estate or ", end = "")

    if total >= 6: print("Gold")
    elif total >= 3: print("Silver")
    else: print("Copper")

main()
