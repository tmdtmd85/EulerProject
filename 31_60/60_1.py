from numba import jit


@jit(nopython=True)
def generate():
    primes = [2]
    memory = [0 for _ in range(1000000)]
    memory[2] = 1

    for i in range(3, 1000000):
        for j in primes:
            if i % j == 0:
                break
            if i % j != 0 and j == primes[-1]:
                primes.append(i)
                memory[i] = 1

    return primes, memory


def partition(primes, i, memory, n, k):
    if k == 1:
        if memory[n] == 1 and primes[i] <= n:
            yield [n]
    else:
        for p in primes[i:]:
            if n < p:
                break
            for _p in partition(primes, i, memory, n - p, k - 1):
                yield [p] + _p
            i += 1


def gen_ind(end):
    for i in range(0, end):
        for j in range(i+1, end):
            yield i, j


def ro(l):
    pass


def glue(a, b):
    c = 1
    while c <= a:
        c *= 10
    return b*c+a


def main():
    primes, memory = generate()
    for _p in partition(primes, 0, memory, 792, 4):
        flag = True
        for g in gen_ind(4):
            if memory[glue(_p[g[0]], _p[g[1]])] == 0:
                flag = False
            if memory[glue(_p[g[1]], _p[g[0]])] == 0:
                flag = False
        if flag:
            print(_p)
            break

    '''a = 10
    b = 432
    print(glue(b, a))'''


if __name__ == '__main__':
    main()

