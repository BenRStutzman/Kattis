import sys

names = sys.stdin.read().split('-')

short = ''

for name in names:
    short += name[0]

print(short)
