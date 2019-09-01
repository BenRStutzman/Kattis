def main():
        string = input()
        length = len(string) // 2

        part_1 = string[:length]
        part_2 = string[length:]

        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        rotate = sum([alpha.index(char) for char in part_1])
        part_1 = ''.join([alpha[(alpha.index(char) + rotate) % 26] for char in part_1])

        rotate = sum([alpha.index(char) for char in part_2])
        part_2 = ''.join([alpha[(alpha.index(char) + rotate) % 26] for char in part_2])

        message = ''.join([alpha[(alpha.index(part_1[i]) + alpha.index(part_2[i])) % 26] for i in range(length)])

        print(message)

main()
