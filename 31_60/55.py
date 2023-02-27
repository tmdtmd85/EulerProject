from collections import deque

def is_palin(k):
    deq = deque()

    print(k)

    tmp = k
    while tmp != 0:
        print(tmp % 10)
        deq.appendleft(tmp % 10)
        tmp = int(tmp/10)
        print(tmp)

    print(deq)

    while len(deq) > 1:
        left = deq.popleft()
        right = deq.pop()
        print(left, right)
        if left != right:
            return False
    return True


def is_lych(k):
    for i in range(0, 54):
        if is_palin(k):
            print(k, i)
            return True

        tmp1 = k
        tmp2 = 0
        while tmp1 != 0:
            tmp2 = tmp2 * 10 + int(tmp1 % 10)
            tmp1 = int(tmp1/10)

        print(k, end=' ')
        k += tmp2
        print(tmp2, k)
    return False


if __name__ == '__main__':
    print(is_palin(4668731596684224866951378664))

