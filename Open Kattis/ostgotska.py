def main():
    sentence = input().split()
    count = 0
    for word in sentence:
        if "ae" in word:
            count += 1
    if count / len(sentence) >= 0.4:
        print("dae ae ju traeligt va")
    else:
        print("haer talar vi rikssvenska")

main()
