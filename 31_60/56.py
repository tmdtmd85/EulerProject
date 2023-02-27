from collections import deque
import copy


def add(a, b):
    result = deque()
    carry = deque([0])

    while len(a) != 0 and len(b) != 0:
        left = a.pop()
        right = b.pop()
        if len(carry) != 0:
            tmp = carry.pop()
        else:
            tmp = 0

        tmp += left + right

        result.appendleft(tmp % 10)

        tmp = int(tmp/10)

        while tmp != 0:
            carry.appendleft(tmp % 10)
            tmp = int(tmp/10)
    while len(a) != 0:
        left = a.pop()
        if len(carry) != 0:
            tmp = carry.pop()
        else:
            tmp = 0
        tmp += left
        result.appendleft(tmp % 10)

        tmp = int(tmp / 10)

        while tmp != 0:
            result.appendleft(tmp % 10)
            tmp = int(tmp / 10)

    while len(b) != 0:
        right = b.pop()
        if len(carry) != 0:
            tmp = carry.pop()
        else:
            tmp = 0
        tmp += right
        result.appendleft(tmp % 10)

        tmp = int(tmp / 10)

        while tmp != 0:
            result.appendleft(tmp % 10)
            tmp = int(tmp / 10)

    while len(carry) != 0:
        if len(carry) == 1 and carry[0] == 0:
            break
        result.appendleft(carry.pop())

    return result


def one_mul(l, k):
    l = copy.deepcopy(l)
    carry = deque([0])
    result = deque()
    while len(l) != 0:
        tmp = l.pop()
        tmp *= k
        tmp += carry.pop()
        result.appendleft(tmp % 10)

        tmp = int(tmp/10)

        if tmp == 0:
            carry.appendleft(0)
        while tmp != 0:
            carry.appendleft(tmp % 10)
            tmp = int(tmp/10)
    while len(carry) != 0:
        if len(carry) == 1 and carry[0] == 0:
            break
        result.appendleft(carry.pop())
    return result


def mul(a, b):
    result = [0]
    i = 0
    for k in b[::-1]:
        tmp = list(one_mul(a, k))
        tmp.extend([0 for _ in range(i)])
        result = list(add(result, tmp))
        i += 1

    return result


def make_list(k):
    tmp = []

    while k != 0:
        tmp.append(k % 10)
        k = int(k/10)

    return tmp[::-1]


if __name__ == '__main__':
    max_sum = 0
    for i in range(1, 100):
        tmp = make_list(i)
        for j in range(1, 100):
            result = make_list(1)
            for _ in range(j):
                result = mul(result, tmp)
            print("{}^{}".format(i, j), result)
            summation = sum(result)
            if summation > max_sum:
                max_sum = summation
    print(max_sum)
