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
        if n == 20:
            print("======")
            print(self.__factoring_list[n])
            print(factors)
            print("======")
        self.__factoring_list[n] = factors
        return factors


def main():
    primes = Primes()
    factoring = Factoring(primes)

    for n in range(1, 2000000):
        if n % 2 == 0:
            left_factor = factoring.factoring(int(n/2), primes)
            right_factor = factoring.factoring(n+1, primes)
        else:
            left_factor = factoring.factoring(int((n+1)/2), primes)
            right_factor = factoring.factoring(n, primes)

        result_factor = []

        i = 0
        j = 0

        while True:
            if i >= len(left_factor):
                for r in right_factor[j:]:
                    result_factor.append(r)
                break

            if j >= len(right_factor):
                for l in left_factor[i:]:
                    result_factor.append(l)
                break
            if left_factor[i][0] < right_factor[j][0]:
                result_factor.append(left_factor[i])
                i += 1
            elif left_factor[i][0] > right_factor[j][0]:
                result_factor.append(right_factor[j])
                j += 1
            else:
                p = left_factor[i][1]
                e = left_factor[i][1] + right_factor[j][1]
                result_factor.append([p, e])
                i += 1
                j += 1

        if math.prod([f[1]+1 for f in result_factor]) > 500:
            print("======")
            print(n, int(n*(n+1)/2), result_factor)
            print("======")
            break
        print(n, int(n*(n+1)/2), result_factor)


if __name__ == '__main__':
    main()

