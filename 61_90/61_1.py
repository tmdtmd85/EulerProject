import sys
import copy


def triangle(n):
    return int(n*(n+1)/2)


def square(n):
    return int(n*n)


def pentagonal(n):
    return int(n*(3*n-1)/2)


def hexagonal(n):
    return int(n*(2*n-1))


def heptagonal(n):
    return int(n*(5*n-3)/2)


def octagonal(n):
    return int(n*(3*n-2))


class Tree:
    def __init__(self, seed):
        self.children = seed

    def add(self, value):
        for child in self.children:
            child.add(value, 1, child.value[1])

    def print_tree(self):
        self.children[0].print_node()


class Node:
    def __init__(self, value, possible, parent):
        self.value = value
        self.children = []
        self.possible = possible
        self.parent = parent

    def add(self, value, k, head):
        if self.possible[value[3]] == 1:
            if self.value[2] == value[1] and self.possible[value[3]] == 1:
                possible = copy.deepcopy(self.possible)
                possible[value[3]] = 0
                self.children.append(Node(value, possible, self))
                if k == 5 and head == value[2]:
                    print("=========")
                    print(value)
                    self._print_node(value[0])
            else:
                for child in self.children:
                    child.add(value, k+1, head)

    def print_node(self):
        print(self.value)
        if len(self.children) > 0:
            self.children[0].print_node()

    def _print_node(self, summation):
        if self.parent != None:
            print(self.value)
            self.parent._print_node(summation+self.value[0])
        else:
            print(self.value)
            summation += self.value[0]
            print(summation)
            sys.exit()


def main():
    temp = []
    functions = [triangle,
                 square,
                 pentagonal,
                 hexagonal,
                 heptagonal,
                 octagonal]

    s = 3
    for f in functions:
        n = 1
        while True:
            tmp = f(n)
            if 1000 <= tmp < 10000:
                temp.append((tmp, int(tmp / 100), tmp % 100, s))
            elif 10000 <= tmp:
                break
            n += 1
        s += 1
    print(temp)

    possible = [0 for _ in range(9)]
    possible[3] = 1
    possible[4] = 1
    possible[5] = 1
    possible[6] = 1
    possible[7] = 1
    possible[8] = 1
    print(possible)

    seed = []

    for t in temp:
        _possible = copy.deepcopy(possible)
        _possible[t[3]] = 0
        seed.append(Node(t, _possible, None))

    tree = Tree(seed)

    for _ in range(6):
        for t in temp:
            tree.add(t)


if __name__ == '__main__':
    main()

