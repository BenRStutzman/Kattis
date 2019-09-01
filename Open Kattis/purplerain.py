import sys

sys.stdin = open('test.txt')

rain = sys.stdin.read().strip()
num = len(rain)

best = 0
for char in rain:
    best = 0
    for i in range(rain.index(char),length
