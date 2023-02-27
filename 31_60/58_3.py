from numba import jit


@jit(nopython=True)
def is_con(a, d, r, n):
    tmp1 = 1
    for _ in range(d):
        tmp1 *= a
        tmp1 %= n

    tmp2 = tmp1
    for _ in range(r):
        tmp2 *= tmp2
        tmp2 %= n

    return not (tmp1 != 1 and tmp2 != n - 1)


@jit(nopython=True)
def is_prime(n):
    if n < 2047:
        l = [2]
    elif n < 1373653:
        l = [2, 3]
    elif n < 9080191:
        l = [31, 73]
    elif n < 25326001:
        l = [2, 3, 5]
    elif n < 3215031751:
        l = [2, 3, 5, 7]
    elif n < 4759123141:
        l = [2, 7, 61]
    elif n < 1122004669633:
        l = [2, 13, 23, 1662803]
    elif n < 2152302898747:
        l = [2, 3, 5, 7, 11]
    elif n < 3474749660383:
        l = [2, 3, 5, 7, 11, 13]
    elif n < 341550071728321:
        l = [2, 3, 5, 7, 11, 13, 17]

    d = n-1

    s = 0
    while d % 2 == 0:
        s += 1
        d = int(d/2)

    flag = False
    for a in l:
        for r in range(0, s):
            if is_con(a, d, r, n):
                flag = True
    return flag


@jit(nopython=True)
def main():
    a = 3
    b = 5
    c = 7

    p = 0
    k = 1
    while True:
        if is_prime(a):
            p += 1
        if is_prime(b):
            p += 1
        if is_prime(c):
            p += 1

        print(p / (4*k+1))

        if 10 * p < 4*k+1:
            break
        k += 1
        a += 8*k-6
        b += 8*k-4
        c += 8*k-2


if __name__ == '__main__':
    main()
