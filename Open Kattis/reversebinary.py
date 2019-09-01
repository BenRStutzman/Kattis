import sys

num = int(sys.stdin.readline())

binary_num = ''

i = 1

while num >= 2 * i:
    i *= 2

while i >= 1:
    if num >= i:
        binary_num += '1'
        num -= i
    else:
        binary_num += '0'
    i /= 2
    

i = 1
reverse_num = 0

for char in binary_num:
    if char == '1':
        reverse_num += i
    i *= 2

print(reverse_num)
