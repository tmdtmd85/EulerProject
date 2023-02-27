import math
from collections import deque

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

def factoring(k, primes):
    s = set()

    primes.prime_update(k)

    for p in primes.return_primes():
        if k % p == 0:
            s.add(p)

    return s


if __name__ == '__main__':
    primes = Primes()

    deq = deque()

    deq.append(factoring(1, primes))
    deq.append(factoring(2, primes))
    deq.append(factoring(3, primes))
    deq.append(factoring(4, primes))

    n = 5
    while True:
        deq.popleft()
        deq.append(factoring(n, primes))
        if len(deq[0]) == 4 \
                and len(deq[1]) == 4 \
                    and len(deq[2]) == 4 \
                        and len(deq[3]) == 4:
            print(n-3, n-2, n-1, n)
            break
        n += 1




