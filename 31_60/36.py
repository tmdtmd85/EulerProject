from collections import deque

def yo():
    for n in range(1, 1000):
        mul = 0
        tmp1 = n
        tmp2 = int(n / 10)
        while True:
            mul = 10 * mul + (n % 10)
            tmp1 *= 10
            tmp2 *= 10
            n = int(n/10)
            if n == 0:
                break
        yield mul+tmp1
        yield mul+tmp2


if __name__ == '__main__':
    summation = 0
    for y in yo():
        tmp = y
        deq = deque()
        while True:
            deq.append(y % 2)
            y = int(y/2)
            if y == 0:
                break
        flag = True
        while True:
            if len(deq) == 1 or len(deq) == 0:
                break
            if deq.popleft() != deq.pop():
                flag = False
                break
        if flag:
            print(tmp)
            summation += tmp
    print(summation)


