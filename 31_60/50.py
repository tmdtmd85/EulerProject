from numba import jit


@jit(nopython=True)
def gen_primes():
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


@jit(nopython=True)
def main():
    primes, memory = gen_primes()

    length = len(primes)
    for i in range(1100, 1, -1):
        print(i)
        for j in range(length-i+1):
            tmp = sum(primes[j:j+i])
            if tmp < 1000000 and memory[tmp] == 1:
                print(tmp, i)
                return


if __name__ == '__main__':
    main()
