from numba import jit
import numpy as np

import math


@jit(nopython=True)
def fastExponentiation(a, x, n):    # a^x mod n
    y = 1
    while x > 0:
        if x & 1 == 1:         # 지수의 LSB가 1인지 확인
            y = (a * y) % n     # Multiply Operation
        a = (a * a) % n         # Square Operation
        x = x >> 1
    return y



@jit(nopython=True)
def is_con(a, d, r, n):
    tmp1 = fastExponentiation(a, d, n)

    tmp2 = tmp1
    for _ in range(r):
        tmp2 *= tmp2
        tmp2 %= n

    return not (tmp1 != 1 and tmp2 != n - 1)


@jit(nopython=True)
def _is_prime(n):
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True


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
    else:
        raise Exception("Error!")

    d = n-1

    s = 0
    while d % 2 == 0:
        s += 1
        d = int(d/2)

    for a in l:
        flag = 1
        for r in range(0, s):
            if is_con(a, d, r, n):
                flag = 0
                break
        if flag == 1:
            return False
    return True


@jit(nopython=True)
def is_ign(k, t, l):
    for i in l:
        if k % i[1] == i[0]:
            l.append((int(t/i[0]), k))
            return True
    return False


@jit(nopython=True)
def main():
    a = 3
    b = 5
    c = 7

    l_a = [(np.ulonglong(x), np.ulonglong(x)) for x in range(0)]
    l_b = [(np.ulonglong(x), np.ulonglong(x)) for x in range(0)]
    l_c = [(np.ulonglong(x), np.ulonglong(x)) for x in range(0)]

    p = 0
    k = 1
    while True:
        if is_prime(a):
            p += 1

        if is_prime(b):
            p += 1

        if is_prime(c):
            p += 1

        l_a.append((k, a))
        l_c.append((a-k, a))

        l_b.append((k, b))
        l_b.append((b-k, b))

        l_c.append((k, c))
        l_a.append((c-k, c))

        print(p / (4*k+1))

        if 10 * p < 4*k+1:
            print("=========")
            print(2*k+1)
            break
        k += 1
        a += 8*k-6
        b += 8*k-4
        c += 8*k-2


if __name__ == '__main__':
    main()

