
def func(k, mod):
    num = 1
    for _ in range(k):
        num *= k
        num %= mod
    return num

if __name__ == '__main__':
    sum = 0
    for i in range(1, 1001):
        sum += func(i, 10**10)
    print(sum % 10**10)
