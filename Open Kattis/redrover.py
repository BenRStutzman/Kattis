def main():
    direcs = input()
    N = len(direcs)
    max_saved = 0
    for macro_len in range(2, N // 2 + 1):
        for macro_start in range(N - macro_len + 1):
            num_saved = direcs.count(direcs[macro_start:macro_start + macro_len]) * (macro_len - 1) - macro_len
            if num_saved > max_saved:
                max_saved = num_saved

    print(N - max_saved)
        
main()
