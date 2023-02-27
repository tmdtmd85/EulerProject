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


def yo(k):
    if k == 1:
        for i in [1,3,7,9]:
            yield [str(i)]
    else:
        for i in [1,3,7,9]:
            for j in yo(k-1):
                yield [str(i)] + j

if __name__ == '__main__':
    primes = Primes()
    summation = 0
    for n in range(2, 6+1):
        for y in yo(n):
            tmp = y
            flag = True
            for i in range(n):
                tmp = tmp[1:] + [tmp[0]]
                if primes.is_prime(int(''.join(tmp))) == False:
                    flag = False
            if flag == True:
                summation += 1
            print(y)
    print(summation+4)




