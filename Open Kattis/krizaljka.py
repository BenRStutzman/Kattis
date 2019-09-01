def find_letter(A, B):
    for A_index, A_char in enumerate(A):
        for B_index, B_char in enumerate(B):
            if A_char == B_char:
                return A_index, B_index

def main():
    A, B = input().split()

    A_index, B_index = find_letter(A, B)

    for i in range(len(B)):
        if i == B_index:
            print(A)
        else:
            print('.' * A_index + B[i] + '.' * (len(A) - A_index - 1))
    
main()
