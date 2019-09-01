import sys
import math

#sys.stdin = open('test.txt')                                   #Comment this out for the real thing!

S = sys.stdin.read().strip()                                    #Read the number of stars as a string and remove the newline character from the end

print(S + ':')                                                  #Print the first line

S = int(S)                                                      #Change the number of stars into an integer

for i in range(2, math.ceil(S / 2) + 1):                        #Start with a row size of 2 and go up to just over half of the number of stars
    if S % (2 * i - 1) == 0 or (S - i) % (2 * i - 1) == 0:      #Check if you can alternate the size of rows and fit in evenly
        print(str(i) + ',' + str(i - 1))                        #Print the two row sizes if that works
    if S % i == 0:                                              #Check if you can have all the same size rows and fit in evenly
        print(str(i) + ',' + str(i))                            #Print the row size if that works
