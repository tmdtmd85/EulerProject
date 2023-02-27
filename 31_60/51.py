from numba import jit

@jit(nopython=True)
def gen_primes(k):
    primes = [2]
    for i in range(3, 10**k):
        for j in primes:
            if i % j == 0:
                break
            if i % j != 0 and j == primes[-1]:
                primes.append(i)

    return [p for p in primes if 10**k > p >= 10**(k-1)]


def main():
    k = 5
    while True:
        flag = False
        ro = []

        primes = gen_primes(k)

        groups = []

        groups.append([primes, 0, int((10**k - 1)/9)])

        for n in range(k):
            temp = []
            for g in groups:
                tmp = [[] for _ in range(10)]
                for p in g[0]:
                    index = int(p / 10**n) % 10
                    tmp[index].append(p)

                for j in range(10):
                    if len(tmp[j]) >= 8:
                        temp.append([tmp[j], g[1] + j*10**n, g[2] - 10**n])

            groups.extend(temp)

        for g in groups:
            l = []
            for p in g[0]:
                if (p - g[1]) % g[2] == 0:
                    l.append(p)

            if len(l) == 8:
                ro.append(l)
                flag = True

        if flag == True:
            for r in ro:
                print(r)
            return
        k += 1

if __name__ == '__main__':
    main()
