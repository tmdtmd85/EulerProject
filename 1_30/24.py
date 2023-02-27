import math

def find(digits, order):
    number = len(digits)
    if number == 1 and order == 1:
        return digits
    if order <= math.factorial(number):
        for i in range(number):
            if i == 0:
                result = find(digits[1:], order)
            elif i == number - 1:
                result = find(digits[:number-1], order)
            else:
                result = find(digits[:i]+digits[i+1:], order)

            if len(result) == 0:
                order -= math.factorial(number-1)
                continue
            else:
                return [digits[i]] + result
    else:
        return []

if __name__ == '__main__':
    final = find([i for i in range(10)], 1000000)
    print(final)
    final = [str(f) for f in final]
    print(''.join(final))
