def main():
    needed, have = [int(num) for num in input().split()]

    print("Dr. Chaz", end = ' ')

    extra = have - needed

    plural = 's' if abs(extra) > 1 else ''

    if extra > 0:
        print("will have %d piece%s of chicken left over!" % (extra, plural))
    else:
        print("needs %d more piece%s of chicken!" % (-extra, plural))     
            
main()
