name = input()

alphabet = 'qwertyuiopasdfghjklzxcvbnm'

for letter in alphabet:
    new_name = name.replace(letter + letter, letter)
    while len(new_name) < len(name):
        name = new_name
        new_name = name.replace(letter + letter, letter)

print(new_name)
