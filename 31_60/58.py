import numba


@numba.jit(nopython=True)
def gen_primes():
    primes = [2]
    memory = [0 for i in range(5*10**6)]
    memory[2] = 1
    for i in range(3, 5*10**6):
        for j in primes:
            if i % j == 0:
                break
            if i % j != 0 and j == primes[-1]:
                primes.append(i)
                memory[i] = 1

    return primes, memory


def generate():
    n = 1
    flag = 0
    adder = 2
    while True:
        if flag == 4:
            flag = 0
            adder += 2
        yield n
        flag += 1
        n += adder


if __name__ == '__main__':
    primes, memory = gen_primes()
    n = 1
    p = 0
    for g in generate():
        print(p / n)
        if memory[g] == 1:
            p += 1
        if n > 1 and n % 4 == 1:
            if p / n < 0.1:
                break
        n += 1
    print(p, n)
