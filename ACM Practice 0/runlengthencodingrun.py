import sys

[X, message] = input().split()

if X == 'E':
    encoded = ''
    last_char = message[0]
    counter = 1
    for char in message[1:]:
        if char == last_char:
            counter += 1
        else:
            encoded += (last_char + str(counter))
            last_char = char
            counter = 1
    encoded += last_char + str(counter)
    print(encoded)
else:
    decoded = ''
    for i in range(0, len(message), 2):
        decoded += message[i] * int(message[i+1])
    print(decoded)
