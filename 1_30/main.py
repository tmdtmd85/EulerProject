# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class Primes:
    def __init__(self):
        self.__number_cursor = 999
        self.__index_cursor = 0

        self.__primes = [2]

        for i in range(3, 1000):
            for j in self.__primes:
                if i % j == 0:
                    break
                if i % j != 0 and j == self.__primes[-1]:
                    self.__primes.append(i)

        self.__primes = self.__primes[::-1]

    def get_number_cursor(self):
        return self.__number_cursor

    def one_step_number_cursor(self):
        if self.__number_cursor == 100:
            return
        self.__number_cursor -= 1
        if self.__primes[self.__index_cursor] > self.__number_cursor:
            self.__index_cursor += 1

    def return_primes(self):
        return self.__primes[:self.__index_cursor]

    def return_residue(self):
        return self.__primes[self.__index_cursor:]


class Palindromes:
    def __init__(self):
        self.__palindromes = []
        self.__index_cursor = 0
        for i in range(999, 99, -1):
            palindrome = 1000 * i
            palindrome += int(i / 100)
            i %= 100
            palindrome += 10 * int(i / 10)
            i %= 10
            palindrome += 100 * i
            self.__palindromes.append(palindrome)
        self.__palindromes_len = len(self.__palindromes)

    def get_palindrome(self):
        return self.__palindromes[self.__index_cursor]

    def one_step_index_cursor(self):
        if not self.__index_cursor == self.__palindromes_len - 1:
            self.__index_cursor += 1

def print_primes():
    primes = Primes()

    for i in range(0, 900):
        print(primes.get_number_cursor())
        print(primes.return_primes())
        print(primes.return_residue())
        primes.one_step_number_cursor()



def print_palindromes():
    palindromes = Palindromes()

    for i in range(999, 99, -1):
        print(palindromes.get_palindrome())
        palindromes.one_step_index_cursor()

def main():
    palindromes = Palindromes()

    primes = Primes()

    find = 0

    for i in range(999, 99, -1):
        palindrome = palindromes.get_palindrome()

        for p in primes.return_primes():
            if palindrome % p == 0:
                find = 1
                print(palindrome, p)

        if not find:
            factors = []
            tmp = 0
            for p in primes.return_residue():
                if palindrome % p == 0:
                    factors.append(p)

            print(palindrome)
            print(factors)

            queue = [palindrome]

            while len(queue) != 0:
                tmp = queue.pop(0)

                if 1000 > tmp > primes.get_number_cursor() and 1000 > int(palindrome/tmp) >= 100:
                    print(tmp, int(palindrome/tmp))
                    return

                for f in factors:
                    if tmp % f == 0:
                        queue.append(int(tmp/f))

        primes.one_step_number_cursor()
        palindromes.one_step_index_cursor()
        find = 0


if __name__ == '__main__':
    main()

