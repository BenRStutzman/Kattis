import sys

def hash(v, trans, token):
    for char in trans:
        v = (v * 31 + ord(char)) % 1000000007
    return (v * 7 + token) % 1000000007

def next_block(prev_hash):
    trans = 'a'
    token = 1000000000
    h = hash(prev_hash, trans, 0)
    token = 1000000007 - h
    if token < (1000000000 - 10000000):
        token += 10000000
    else:
        token -= 10000007
    h = hash(prev_hash, trans, token)
    return h, trans, token

def main():
    inp = sys.stdin.read().splitlines()
    prev_hash = int(inp[0])
    for i in range(2):
        h, trans, token = next_block(prev_hash)
        print(trans, token)
        prev_hash = h


main()
