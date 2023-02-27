
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

def yo(p, primes):
    mul = 1
    tmp = p
    flag = True
    while True:
        if not primes.is_prime(tmp):
            flag = False
            break
        tmp = int(tmp/10)
        if tmp == 0:
            break
        mul *= 10
    while True:
        if mul == 1:
            break
        if not primes.is_prime(p % mul):
            flag = False
            break
        mul = int(mul/10)

    return flag



if __name__ == '__main__':
    primes = Primes()

    lists = []
    n = 0

    k = 1

    while True:
        for p in range(1000*(k-1)+10, 1000*k+10):
            if yo(p, primes):
                lists.append(p)
                print(p)
                n += 1
        if n == 11:
            break
        else:
            k += 1
    print(sum(lists))

