import math
import copy

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


class Factoring:
    def __init__(self, primes):
        self.__factoring_list = [[], [], [[2, 1]]] + [[] for _ in range(2000000)]
        self.__primes = primes

    def get_factroing_list(self):
        return self.__factoring_list

    def factoring(self, n, primes):
        primes.prime_update(n)
        factors = []

        if len(self.__factoring_list[n]) > 0:
            return self.__factoring_list[n]

        for p in primes.return_primes():
            if n < p:
                break

            if n % p == 0:
                if n == p:
                    factors = [[p, 1]]
                else:
                    tmp = copy.deepcopy(self.factoring(int(n/p), primes))
                    find = 0
                    for i in range(len(tmp)):
                        if tmp[i][0] == p:
                            tmp[i][1] += 1
                            find = 1
                    if find == 0:
                        factors = [[p, 1]] + tmp
                    elif find == 1:
                        factors = tmp
                    break
        self.__factoring_list[n] = factors
        return factors



def main():
    primes = Primes()
    factoring = Factoring(primes)

    summation = 0
    for i in range(2, 10000):
        factor = factoring.factoring(i, primes)

        mul1 = 1
        for f in factor:
            mul1 *= (f[0] ** (f[1] + 1) - 1) / (f[0] - 1)
        mul1 -= i
        mul1 = int(mul1)

        factor = factoring.factoring(mul1, primes)

        mul2 = 1
        for f in factor:
            mul2 *= (f[0] ** (f[1] + 1) - 1) / (f[0] - 1)
        mul2 -= mul1
        mul2 = int(mul2)

        if mul2 == i and mul1 != i:
            summation += i
    print(summation)



if __name__ == '__main__':
    main()
