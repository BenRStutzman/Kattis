f = open("communicationssatellite2.in", 'w')

f.write("2000\n")
for i in range(2000):
    f.write("%d %d %d\n" % (i * 3, 1, 1))

f.close()
