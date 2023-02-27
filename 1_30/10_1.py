import math


class Primes:
    def __init__(self):
        self.__primes = [2]
        sum = 2
        for i in range(3, 2000000):
            for j in self.__primes:
                if i % j == 0:
                    break
                if i % j != 0 and j == self.__primes[-1]:
                    self.__primes.append(i)
                    sum += i
                    print(i)
        print(sum)
    def return_primes(self):
        return self.__primes

if __name__ == '__main__':
    primes = Primes()

