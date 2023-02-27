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