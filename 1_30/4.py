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


def print_palindromes():
    palindromes = Palindromes()

    for i in range(999, 99, -1):
        print(palindromes.get_palindrome())
        palindromes.one_step_index_cursor()


def main():
    palindromes = Palindromes()

    for i in range(999, 99, -1):
        palindrome = palindromes.get_palindrome()

        for j in range(100, 1000):
            if palindrome % j == 0 and 1000 > int(palindrome/j) >= 100:
                print(str(palindrome)+"="+str(j)+"*"+str(int(palindrome/j)))
                return

        palindromes.one_step_index_cursor()


if __name__ == '__main__':
    main()
