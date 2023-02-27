
class Penta:
    def __init__(self):
        self.penta = [1]
        self.n = 1

        self.y = lambda x: int(x*(3*x-1)/2)

        self.mini = 2**31-1
        self.diff = 0

        self.left = 0
        self.right = 0

    def is_penta(self, k):
        while self.penta[-1] < k:
            self.n += 1
            a = self.penta[-1]
            b = self.y(self.n)
            self.penta.append(b)
            self.diff = b - a
        if k in self.penta:
            return True
        else:
            return False

    def update(self, k):
        while self.n-1 < k:
            self.is_penta(self.penta[-1]+1)

        for p in self.penta[:k]:
            if self.is_penta(p + self.penta[k]):
                tmp = self.penta[k] - p
                if self.is_penta(tmp) and tmp < self.mini:
                    self.mini = tmp
                    self.left = p
                    self.right = self.penta[k]
                    print(self.mini, self.left, self.right)
        if self.mini < self.diff:
            return False
        else:
            return True


if __name__ == '__main__':
    penta = Penta()

    n = 0
    while penta.update(n):
        n += 1

    print(penta.penta)

