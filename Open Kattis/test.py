from sys import stdin, stdout
import time


start_time = time.time()
def main():
    inp = stdin.read().splitlines()
    out = []
    
    for line in inp:
        print(line)

    #stdout.write("\n".join(out))

main()

print(time.time() - start_time)
