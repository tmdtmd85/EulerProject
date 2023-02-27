from numba import jit


@jit(nopython=True)
def generate():
    primes = [2]
    memory = [0 for _ in range(100000)]
    memory[2] = 1

    for i in range(3, 100000):
        for j in primes:
            if i % j == 0:
                break
            if i % j != 0 and j == primes[-1]:
                primes.append(i)
                memory[i] = 1

    return primes, memory


def yo(start, end, k):
    if k == 1:
        for i in range(start, end + 1):
            yield [i]
    #print(n, end=' ')
    else:
        for i in range(start, end + 1):
            for y in yo(i, end, k-1):
                yield [i] + y


def main():
    for y in yo(0, 2, 3):
        print(y)


if __name__ == '__main__':
    main()
