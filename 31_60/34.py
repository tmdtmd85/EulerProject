import math

def yo(n):
    lists = []
    while True:
        lists.append(n % 10)
        n = int(n/10)
        if n == 0:
            break
    return lists[::-1]

if __name__ == '__main__':
    summation = 0
    for n in range(3, 10**7):
        if sum([math.factorial(y) for y in yo(n)]) == n:
            summation += n
    print(summation)
    