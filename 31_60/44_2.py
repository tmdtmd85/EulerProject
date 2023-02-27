import math
from numba import jit

y = lambda x: int(x * (3 * x - 1) / 2)

@jit(nopython=True)
def is_penta(k):
    tmp = (math.sqrt(24*k+1)+1)/6
    return int(tmp) == tmp

@jit(nopython=True)
def main():
    y = lambda x: int(x * (3 * x - 1) / 2)

    n = 0
    while True:
        n += 1
        diff = y(n)
        j = 1
        upper = (2*diff+1)/6
        print(diff)
        while j < upper:
            left = y(j)
            if is_penta(diff+left) and is_penta(diff+2*left):
                right = diff+left
                print(left, right, diff)
                return
            j += 1


if __name__ == '__main__':
    main()


#5482660