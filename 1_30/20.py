import math

def digits_sum(n):
    summation = 0
    while True:
        summation += n % 10
        n = n/10
        if n == 0:
            break
    return summation
if __name__ == '__main__':
    summation = [1]
    tmp = 0
    for i in range(1, 100+1):
        for j in range(len(summation)):
            summation[j] = summation[j] * i + tmp
            tmp = int(summation[j] / 10)
            summation[j] %= 10

        if tmp > 0:
            while True:
                summation.append(int(tmp % 10))
                tmp = int(tmp/10)
                if tmp == 0:
                    break
    print(sum(summation))

