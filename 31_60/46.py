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
        if number <= self.__primes[-1]:
            return
        else:
            for i in range(self.__primes[-1] + 1, number):
                for j in self.__primes:
                    if i % j == 0:
                        break
                    if i % j != 0 and j == self.__primes[-1]:
                        self.__primes.append(i)
                        self.memory[i] = 1

    def is_prime(self, n):
        self.prime_update(n)

        if self.memory[n] == 1:
            return True
        else:
            flag = True
            for p in self.__primes:
                if n % p == 0:
                    flag = False
                    break
            if flag:
                self.memory[n] = 1
                return True
            else:
                return False

    def is_true(self, k):
        flag = True
        self.prime_update(k)
        for p in self.__primes:
            if p >= k:
                break
            if (k-p) % 2 == 0:
                tmp = math.sqrt(int((k-p)/2))

                if int(tmp) == tmp:
                    print(k, p, tmp)
                    flag = False
                    break

        return flag


if __name__ == '__main__':
    primes = Primes()

    n = 1
    while True:
        if not primes.is_prime(n):
            if primes.is_true(n):
                break
        n += 2
    print("======")
    print(n)

