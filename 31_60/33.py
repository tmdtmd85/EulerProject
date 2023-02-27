import math

class Node:
    def __init__(self, n, next_node):
        self.n = n
        self.next_node = next_node

class LinkedList:
    def __init__(self, node):
        self.head = node

    def delete(self, k):
        current_node = self.head
        prev_node = None
        while True:
            if current_node == None:
                break
            if current_node.n == k:
                if current_node == self.head:
                    self.head = self.head.next_node
                else:
                    prev_node.next_node = current_node.next_node
            prev_node = current_node
            current_node = current_node.next_node

    def has(self, k):
        current_node = self.head
        while True:
            if current_node == None:
                break
            elif current_node.n == k:
                return True
            else:
                current_node = current_node.next_node
        return False

    def printlist(self):
        current_node = self.head
        if self.head == None:
            return 1
        result = 0
        while True:
            if current_node == None:
                break
            else:
                result = result * 10 + current_node.n
                current_node = current_node.next_node
        return result

def abc():
    for i in range(10, 100):
        for j in range(i+1, 100):
            yield i, j


def yo(n):
    next_node = None
    while True:
        next_node = Node(n % 10, next_node)
        n = int(n/10)
        if n == 0:
            break
    return next_node


if __name__ == '__main__':
    mul_a = mul_b = 1
    for n in abc():
        a = n[0]
        b = n[1]
        numerator = LinkedList(yo(a))
        denominator = LinkedList(yo(b))

        while numerator.has(0) and denominator.has(0):
            numerator.delete(0)
            denominator.delete(0)

        flag = 0
        for i in range(1, 10):
            while numerator.has(i) and denominator.has(i):
                flag = 1
                numerator.delete(i)
                denominator.delete(i)

        if flag == 1 and numerator.printlist()*b == denominator.printlist()*a:
            mul_a *= a
            mul_b *= b
            print("{}/{}".format(a, b))

    g = math.gcd(mul_a, mul_b)

    print("{}/{}".format(int(mul_a/g), int(mul_b/g)))

