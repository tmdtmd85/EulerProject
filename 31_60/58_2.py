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
    a = lambda k: (2*k+1)**2 - 6*k
    b = lambda k: (2*k+1)**2 - 4*k
    c = lambda k: (2*k+1)**2 - 2*k

    p = 0
    k = 1
    while True:
        if is_prime(a(k)):
            p += 1
        if is_prime(b(k)):
            p += 1
        if is_prime(c(k)):
            p += 1

        print(p / (4*k+1))

        if 10 * p < 4*k+1:
            break
        k += 1


@jit(nopython=True)
def yo():
    a = lambda k: (2*k+1)**2 - 6*k
    b = lambda k: (2*k+1)**2 - 4*k
    c = lambda k: (2*k+1)**2 - 2*k

    p = 0
    t = 0
    while True:
        tmp1 = 15*t+1
        tmp2 = 15*t+2
        tmp3 = 15*t+3
        tmp4 = 15*t+4
        tmp5 = 15*t+5
        tmp6 = 15*t+6
        tmp7 = 15*t+7
        tmp8 = 15*t+8
        tmp9 = 15*t+9
        tmp10 = 15*t+10
        tmp11 = 15*t+11
        tmp12 = 15*t+12
        tmp13 = 15*t+13
        tmp14 = 15*t+14
        tmp15 = 15*t+15

        if is_prime(a(tmp2)):
            p += 1
        if is_prime(a(tmp3)):
            p += 1
        if is_prime(a(tmp5)):
            p += 1
        if is_prime(a(tmp6)):
            p += 1
        if is_prime(a(tmp8)):
            p += 1
        if is_prime(a(tmp9)):
            p += 1
        if is_prime(a(tmp11)):
            p += 1
        if is_prime(a(tmp12)):
            p += 1
        if is_prime(a(tmp14)):
            p += 1
        if is_prime(a(tmp15)):
            p += 1

        if is_prime(b(tmp2)):
            p += 1
        if is_prime(b(tmp3)):
            p += 1
        if is_prime(b(tmp5)):
            p += 1
        if is_prime(b(tmp7)):
            p += 1
        if is_prime(b(tmp8)):
            p += 1
        if is_prime(b(tmp10)):
            p += 1
        if is_prime(b(tmp12)):
            p += 1
        if is_prime(b(tmp13)):
            p += 1
        if is_prime(b(tmp15)):
            p += 1

        if is_prime(c(tmp1)):
            p += 1
        if is_prime(c(tmp3)):
            p += 1
        if is_prime(c(tmp4)):
            p += 1
        if is_prime(c(tmp6)):
            p += 1
        if is_prime(c(tmp7)):
            p += 1
        if is_prime(c(tmp9)):
            p += 1
        if is_prime(c(tmp10)):
            p += 1
        if is_prime(c(tmp12)):
            p += 1
        if is_prime(c(tmp13)):
            p += 1
        if is_prime(c(tmp15)):
            p += 1

        print(p / (60*t+61))

        if p / (60*t+61) < 0.1:
            break

        t += 1


if __name__ == '__main__':
    #yo()
    a = lambda k: (2*k+1)**2 - 6*k
    b = lambda k: (2*k+1)**2 - 4*k
    c = lambda k: (2*k+1)**2 - 2*k

    for k in range(2, 100):
        print(k, a(k), a(k) % 5 == 0)



