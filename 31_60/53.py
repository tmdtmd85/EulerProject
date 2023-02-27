from math import comb


def main():
    num = 0
    for n in range(1, 101):
        for r in range(0, n+1):
            if comb(n, r) > 1000000:
                num += 1
    print(num)


if __name__ == '__main__':
    main()
