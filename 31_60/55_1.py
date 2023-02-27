from collections import deque


def add(a, b):
    result = deque()
    carry = deque([0])

    while len(a) != 0 and len(b) != 0:
        left = a.pop()
        right = b.pop()
        tmp = carry.pop()

        tmp += left + right

        result.appendleft(tmp % 10)

        tmp = int(tmp/10)

        if tmp == 0:
            carry.appendleft(0)
        while tmp != 0:
            carry.appendleft(tmp % 10)
            tmp = int(tmp/10)
    while len(a) != 0:
        left = a.pop()
        tmp = carry.pop()
        tmp += left
        result.appendleft(tmp % 10)

        tmp = int(tmp / 10)

        if tmp == 0:
            carry.appendleft(0)
        while tmp != 0:
            result.appendleft(tmp % 10)
            tmp = int(tmp / 10)

    while len(b) != 0:
        left = b.pop()
        tmp = carry.pop()
        tmp += left
        result.appendleft(tmp % 10)

        tmp = int(tmp / 10)

        if tmp == 0:
            carry.appendleft(0)
        while tmp != 0:
            result.appendleft(tmp % 10)
            tmp = int(tmp / 10)

    while len(carry) != 0:
        if len(carry) == 1 and carry[0] == 0:
            break
        result.appendleft(carry.pop())

    return result


def is_palin(l):
    i = 0
    j = len(l)-1
    while i < j:
        if l[i] != l[j]:
            return False
        i += 1
        j -= 1
    return True


def is_lych(l):
    for i in range(0, 50):
        l = list(add(l, l[::-1]))
        if is_palin(l):
            print(l)
            return False
    return True


def make_list(k):
    tmp = []

    while k != 0:
        tmp.append(k % 10)
        k = int(k/10)

    return tmp[::-1]


if __name__ == '__main__':
    num = 0
    for i in range(1, 10000):
        if is_lych(make_list(i)):
            num += 1
    print(num)
