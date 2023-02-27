import math
import sys

class Order:
    def __init__(self):
        pass

    def return_pair(self, e, number, k):
        if k > 1:
            _e = e
            yo = []
            while True:
                tmp = self.return_pair(_e, number/(_e+1), k - 1)
                if tmp == None or tmp == []:
                    break
                for t in tmp:
                    if _e <= t[0]:
                        yo.append([_e]+t)
                _e += 1

            return yo

        if k == 1:
            _e = max(1, math.floor(number - 1) + 1)
            if _e >= e:
                return [[_e]]


def main():
    order = Order()

    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]

    minimum = sys.maxsize
    minimum_pair = []
    for n in range(1, 10):
        pairs = order.return_pair(1, 500, n)

        for pair in pairs:
            result = math.prod([primes[i] ** pair[n-1-i] for i in range(n)])

            tmp = math.sqrt(1+8*result)

            if int(tmp) == tmp and tmp % 2 == 1:
                print((-1+tmp)/2)

            if result < minimum:
                minimum_pair = pair[::-1]
                minimum = result
    print(minimum, minimum_pair)


if __name__ == '__main__':
    main()
