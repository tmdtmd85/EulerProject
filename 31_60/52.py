from numba import jit


@jit(nopython=True)
def arrange(k):
    tmp = []
    while k != 0:
        tmp.append(k % 10)
        k = int(k/10)
    tmp.sort(reverse=True)

    temp = 0
    for t in tmp:
        temp = temp * 10 + t
    return temp


@jit(nopython=True)
def main():
    n = 1
    while True:
        s = set()
        for i in range(1, 7):
            s.add(arrange(n*i))

        if len(s) == 1:
            print(n)
            break
        n += 1


if __name__ == '__main__':
    main()
