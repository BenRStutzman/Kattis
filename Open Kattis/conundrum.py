string = input()

days = 0
name = "PER"

for index, char in enumerate(string):
    if char != name[index % 3]:
        days += 1

print(days)
