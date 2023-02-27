import math

def main():
    a = 1
    b = 1

    i = 3
    while True:
        c = a + b
        a = b
        b = c
        if 999 <= math.log10(c) < 1000:
            print(i, c)
            break
        i += 1

if __name__ == '__main__':
    main()