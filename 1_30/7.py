class Primes:
    def __init__(self):
        self.__primes = []
        self.__n = 0

    def return_prime(self):
        if self.__n == 0:
            self.__primes.append(2)
            self.__n += 1
            return 2

        for i in range(self.__primes[-1] + 1, 2 * self.__primes[-1]):
            for j in self.__primes:
                if i % j == 0:
                    break
                if i % j != 0 and j == self.__primes[-1]:
                    self.__primes.append(i)
                    self.__n += 1
                    return i

    def get_n(self):
        return self.__n


def main():
    primes = Primes()
    for i in range(0, 10001):
        print(str(primes.get_n() + 1), str(primes.return_prime()))


if __name__ == '__main__':
    main()