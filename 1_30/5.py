def gcd(a, b):
    if a < b:
        tmp = a
        a = b
        b = tmp

    while b != 0:
        n = a % b
        a = b
        b = n

    return a


def main():
    mul = 1
    for i in range(1, 20 + 1):
        mul = int(mul * i / gcd(mul, i))
    print(mul)


if __name__ == '__main__':
    main()