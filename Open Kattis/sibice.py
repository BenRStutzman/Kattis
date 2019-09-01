import sys
import math

[num, box_length, box_width] = [int(num) for num in sys.stdin.readline().split()]

diag = box_length**2 + box_width**2

for i in range(num):
    match_length = int(sys.stdin.readline())
    if match_length**2 <= diag:
        print("DA")
    else:
        print("NE")
