import sys

def main():

    inp = sys.stdin.read().splitlines()
    N = int(inp[0])
    pushes = {int(num) for num in inp[1].split()}
    cleanups = 0

    for day in range(1, 367):
        dirtiness = sum({day - push for push in pushes if push < day})
        if dirtiness >= 20:
            #print("Push on day", day - 1)
            cleanups += 1
            pushes = pushes.difference({push for push in pushes if push < day})

    if pushes:
        #print("Push on day", day - 1)
        cleanups += 1

    print(cleanups)            

main()
