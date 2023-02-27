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

    tmp = []

    for p in primes.return_primes():
        if p <= 1000:
            tmp.append(p)
            tmp.append(-p)
        else:
            break
    print(tmp)


    a = 0
    b = 0
    f = lambda n : n**2 + a*n + b

    max_a = 0
    max_b = 0
    max_len = 0
    for a in range(-999, 999+1):
        for b in tmp:
            i = 0
            while True:
                factor = factoring.factoring(f(i), primes)
                if len(factor) == 0 or not len(factor) == 1 and factor[0][1] == 1:
                    break
                i += 1
            if max_len < i-1:
                max_len = i - 1
                max_a = a
                max_b = b

    print(max_len, max_a, max_b, max_a*max_b)




if __name__ == '__main__':
    main()
