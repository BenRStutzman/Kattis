f = open('hoppers.in', mode = 'w')

N = 200

f.write(str(N) + "\n")
for i in range(1, N//2 + 1):
    for j in range(1, N//2 + 1):
        f.write(str(i) + " " + str(j) + "\n")
for i in range(N//2 + 1, N + 1):
    for j in range(N//2 + 1, N + 1):
        f.write(str(i) + " " + str(j) + "\n")

f.close()
        
