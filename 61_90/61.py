from numba import jit


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
def generate():
    primes = [2]

    for i in range(3, 1000000):
        for j in primes:
            if i % j == 0:
                break
            if i % j != 0 and j == primes[-1]:
                primes.append(i)
    return primes


def triangle(n):
    return int(n*(n+1)/2)


def square(n):
    return int(n*n)


def pentagonal(n):
    return int(n*(3*n-1)/2)


def hexagonal(n):
    return int(n*(2*n-1))


def heptagonal(n):
    return int(n*(5*n-3)/2)


def octagonal(n):
    return int(n*(3*n-2))


def main():
    functions = [triangle,
                 square,
                 pentagonal,
                 hexagonal,
                 heptagonal,
                 octagonal]

    k = 0
    for f in functions:
        n = 1
        while True:
            tmp = f(n)
            if 1000 <= tmp < 10000:
                #print(tmp)
                k += 1
            elif 10000 <= tmp:
                break
            n += 1
    print(k)


if __name__ == '__main__':
    main()

