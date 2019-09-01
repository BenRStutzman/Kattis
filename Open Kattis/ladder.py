import sys
import math

[h, v] = [int(num) for num in sys.stdin.read().split()]

v *= math.pi / 180

print(math.ceil(h / math.sin(v)))
