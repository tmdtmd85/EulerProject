from numba import jit
import math
import time


@jit(nopython=True)
def generate():
    primes = [2]
    memory = [0 for _ in range(1000000)]
    memory[2] = 1

    for i in range(3, 1000000):
        for j in primes:
            if i % j == 0:
                break
            if i % j != 0 and j == primes[-1]:
                primes.append(i)
                memory[i] = 1

    return primes, memory


def glue(a, b):
    c = 1
    while c <= a:
        c *= 10
    return b*c+a


maximum = 1000


def yo(primes, memory, i, k):
    global maximum

    if k == 1:
        for p in primes[i:]:
            yield [p]
    else:
        for p in primes[i:]:
            for y in yo(primes, memory, i, k-1):
                flag = True
                for _y in y:
                    if not (memory[glue(p, _y)] == 1 and memory[glue(_y, p)] == 1):
                        flag = False
                        break
                if flag:
                    yield [p] + y
            i += 1


def main():
    primes, memory = generate()

    global maximum

    minimum = 10000
    minimum_l = []
    for y in yo(primes[:150], memory, 0, 4):
        print(y)
        if sum(y) < minimum:
            minimum = sum(y)
            minimum_l = y
    print(minimum, minimum_l)

    for y in yo(primes[:150], memory, 0, 3):
        print(y)
        if sum(y) < minimum:
            minimum = sum(y)
            minimum_l = y
    print(minimum, minimum_l)


if __name__ == '__main__':
    main()
