import sys

def next_hash(prev_hash, trans, token):
    return (7 * ((31 * prev_hash + ord(trans)) % 1000000007)) % 1000000007

def new_block(prev_hash):
    choices = 'abcdefghijklmnopqrstuv'
    i = 0
    h = next_hash(prev_hash, choices[i], 0)
    while h < 8:
        print('again')
        i += 1
        h = next_hash(prev_hash, choices[i], 0)
    t = 1000000007 - h
    if t < 10000000:
        t += 10000000
    else:
        t -= 10000000
    return choices[i], t, h

def main():
    inp = sys.stdin.read().splitlines()
    #print(inp)
    N = int(inp[0])
    for i in range(2):
        trans, token, h = new_block(N)
        print(trans, token)
        print(next_hash(h, trans, token))
        N = h
    
main()
