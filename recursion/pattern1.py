def pattern(n):
    if n==1:
        print('* ' * 1)
        return
    print('* '*n)
    pattern(n-1)


def normalpattern(n):
    if n==1:
        print('* ' * 1)
        return
    normalpattern(n-1)
    print('* '*n)


normalpattern(5)