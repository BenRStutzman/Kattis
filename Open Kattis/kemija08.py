message = input().strip()

char = 0

while char < len(message):
    if message[char] in {'a', 'e', 'i', 'o', 'u'}:
        message = message[:char + 1] + message[char + 3:]
    char += 1

print(message)
