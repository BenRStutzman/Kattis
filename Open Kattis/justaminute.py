import sys

def main():
    inp = [[int(num) for num in line.split()] for line in sys.stdin.read().splitlines()]
    realsecs = 0
    fakesecs = 0
    for mins, secs in inp[1:]:
        realsecs += mins * 60
        fakesecs += secs

    avg = fakesecs / realsecs
    if avg <= 1:
        print("measurement error")
    else:
        print(avg)
       

main()
