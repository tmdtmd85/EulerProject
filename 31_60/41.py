import math

class Primes:
    def __init__(self):
        self.__primes = [2]
        self.memory = [0 for _ in range(1000000)]
        self.memory[2] = 1

        for i in range(3, 1000):
            for j in self.__primes:
                if i % j == 0:
                    break
                if i % j != 0 and j == self.__primes[-1]:
                    self.__primes.append(i)
                    self.memory[i] = 1
    def return_primes(self):
        return self.__primes

    def prime_update(self, number):
        if math.sqrt(number) <= self.__primes[-1]:
            return
        else:
            for i in range(self.__primes[-1] + 1, int(math.sqrt(number)) + 1):
                for j in self.__primes:
                    if i % j == 0:
                        break
                    if i % j != 0 and j == self.__primes[-1]:
                        self.__primes.append(i)
                        self.memory[i] = 1

    def is_prime(self, n):
        self.prime_update(n)

        if n == 1:
            return False

        if n < 1000000 and self.memory[n] == 1:
            return True
        else:
            flag = True
            for p in self.__primes:
                if n % p == 0:
                    flag = False
                    break
            if flag:
                if n < 1000000:
                    self.memory[n] = 1
                return True
            else:
                return False

def perm(lists):
    if len(lists) == 1:
        return [[lists[0]]]
    else:
        result = []
        for i in range(len(lists)):
            if i == 0:
                for p in perm(lists[1:]):
                    result.append([lists[0]] + p)
            elif i == len(lists) - 1:
                for p in perm(lists[:-1]):
                    result.append([lists[-1]] + p)
            else:
                for p in perm(lists[:i]+lists[i+1:]):
                    result.append([lists[i]]+p)
        return result


if __name__ == '__main__':
    primes = Primes()

    max = 0
    for n in range(1, 10):
        for p in perm([i for i in range(1, n+1)]):
            mul = 0
            for d in p:
                mul = 10*mul + d
            if primes.is_prime(mul):
                if mul > max:
                    max = mul
                print(mul)
    print("=========")
    print(max)
