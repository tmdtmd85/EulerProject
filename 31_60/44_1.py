

class Penta:
    def __init__(self):
        self.penta = [1]
        self.n = 1

        self.y = lambda x: int(x*(3*x-1)/2)

        self.left = 0
        self.right = 0

    def is_penta(self, k):
        while self.penta[-1] < k:
            self.n += 1
            print(self.n)
            a = self.penta[-1]
            b = self.y(self.n)
            self.penta.append(b)
        if k in self.penta:
            return True
        else:
            return False

def main():
    penta = Penta()

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
            if penta.is_penta(diff+left) and penta.is_penta(diff+2*left):
                right = diff+left
                print(left, right, diff)
                return
            j += 1


if __name__ == '__main__':
    main()





