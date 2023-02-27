import math

class Primes:
    def __init__(self):
        self.__primes = [2]

        for i in range(3, 1000):
            for j in self.__primes:
                if i % j == 0:
                    break
                if i % j != 0 and j == self.__primes[-1]:
                    self.__primes.append(i)

    def return_primes(self):
        return self.__primes

    def prime_update(self, number):
        if number < self.__primes[-1]:
            return
        else:
            for i in range(self.__primes[-1] + 1, number + 1):
                for j in self.__primes:
                    if i % j == 0:
                        break
                    if i % j != 0 and j == self.__primes[-1]:
                        self.__primes.append(i)

def factoring(n, primes):
    primes.prime_update(n)

    factors = []

    for p in primes.return_primes():
        if n < p:
            break

        if n % p == 0:
            e = 0
            while n % p == 0:
                e += 1
                n = int(n/p)
            factors.append([p, e])

    return factors


def main():
    primes = Primes()

    n = 500

    factor = []

    for i in range(2000000):
        print(factoring(i, primes))

    while True:
        n += 1
        factor = factoring(n, primes)

        mul = 1

        for f in factor:
            mul *= f[1]

        if mul == 8:
            print(factor)
            return




if __name__ == '__main__':
    main()

