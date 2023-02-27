import math
from numba import jit

@jit(nopython=True)
def is_tri(k):
    tmp = (math.sqrt(8*k+1)-1)/2
    return int(tmp) == tmp

@jit(nopython=True)
def is_penta(k):
    tmp = (math.sqrt(24*k+1)+1)/6
    return int(tmp) == tmp

@jit(nopython=True)
def is_hex(k):
    tmp = (math.sqrt(8*k+1)+1)/4
    return int(tmp) == tmp

@jit(nopython=True)
def main():
    y = lambda x: int(x * (x + 1) / 2)
    n = 1
    while True:
        tmp = y(n)
        if is_tri(tmp) and is_penta(tmp):
            if n > 40755:
                print("======")
                print(tmp)
                break
        n += 1

if __name__ == "__main__":
    main()