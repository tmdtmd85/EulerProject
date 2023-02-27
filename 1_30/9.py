


def main():
    for a in range(1, 999):
        if (a ** 2) % (1000 - a) == 0:
            c = 1000 - a + int(a**2 / (1000 - a))
            b = 1000 - a - int(a**2 / (1000 - a))

            if b % 2 == 0 and c % 2 == 0:
                b = int(b / 2)
                c = int(c / 2)

            if a < b < c:
                print(a, b, c)
                print(a*b*c)

if __name__ == '__main__':
    main()