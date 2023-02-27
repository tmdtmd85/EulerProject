import math

def summation(k, total):
    return int(k * (int(total/k) * (int(total/k) + 1)) / 2)

class Composite:
    def __init__(self, primes):
        self.primes = primes
        self.queue = []

        i = 0
        sign = 1
        for p in primes:
            self.queue.append((p, i, sign))
            i += 1

    def return_composite(self):
        if len(self.queue) == 0:
            return None

        tmp = self.queue.pop(0)
        for i in range(tmp[1]+1, len(self.primes)):
            sign = tmp[2] * -1
            self.queue.append((tmp[0] * self.primes[i], i, sign))

        return tmp[0], tmp[2]

    def is_empty(self):
        return len(self.queue)

def main():
    number = 2000000
    total = int(math.sqrt(number))

    number_list = [[i, 1] for i in range(total + 1)]

    prime_list = []

    sum = summation(1, number) - 1

    for n in number_list[2:]:
        if n[1] == 1:
            p = n[0]
            prime_list.append(p)
            for i in range(2, int(total/p) + 1):
                number_list[p*i][1] -= 1

            tmp = summation(p, number) - p
            sum -= tmp

            composite = Composite(prime_list[:-1])

            while composite.is_empty() != 0:
                tmp, sign = composite.return_composite()
                for i in range(1, int(total / (p * tmp)) + 1):
                    number_list[p * tmp * i][1] += sign
                sum += sign * summation(p * tmp, number)
        if n[1] == 0:
            continue
        print(n)
    print("=======")
    print(sum)
    print("=======")
    print(prime_list)

if __name__ == '__main__':
    main()