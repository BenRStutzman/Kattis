import sys

def main():
    inp = sys.stdin.read().splitlines()

    to_morse = {'A': ".-", 'B': "-...", 'C': "-.-.", 'D': "-..", 'E': '.', 'F': "..-.",
                'G': "--.", 'H': "....", 'I': "..", 'J': ".---", 'K': "-.-", 'L': ".-..",
                'M': "--", 'N': "-.", 'O': "---", 'P': ".--.", 'Q': "--.-",
                'R': ".-.", 'S': "...", 'T': '-', 'U': "..-", 'V': "...-",
                'W': ".--", 'X': "-..-", 'Y': "-.--", 'Z': "--..", '_': "..--",
                ',': ".-.-", '.': "---.", '?': "----"}
    to_english = {value: key for key, value in to_morse.items()}

    for message in inp:
        morse = ''
        decoded = ''
        lengths = []
        for char in message:
            morse_char = to_morse[char]
            morse += morse_char
            lengths.append(len(morse_char))
        
        i = 0
        while i < len(morse):
            length = lengths.pop()
            decoded += to_english[morse[i:i + length]]
            i += length

        print(decoded)

main()
