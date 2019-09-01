import sys

[N, message] = sys.stdin.read().splitlines()
message = message.split()
N = int(N)

for i in range(N):
    if message[i] != "mumble":
        if int(message[i]) != i + 1:
            print("something is fishy")
            break
else:
    print("makes sense")
