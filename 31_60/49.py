

class Primes:
    def __init__(self):
        self.__primes = [2]
        self.memory = [0 for _ in range(1000000)]
        self.memory[2] = 1

        for i in range(3, 1000):
            for j in self.__primes:
                if i % j == 0:
                    break
                if i % j != 0 and j == self.__primes[-1]:
                    self.__primes.append(i)
                    self.memory[i] = 1
    def return_primes(self):
        return self.__primes

    def prime_update(self, number):
        if number <= self.__primes[-1]:
            return
        else:
            for i in range(self.__primes[-1] + 1, number):
                for j in self.__primes:
                    if i % j == 0:
                        break
                    if i % j != 0 and j == self.__primes[-1]:
                        self.__primes.append(i)
                        self.memory[i] = 1

    def is_prime(self, n):
        self.prime_update(n)

        if self.memory[n] == 1:
            return True
        else:
            flag = True
            for p in self.__primes:
                if n % p == 0:
                    flag = False
                    break
            if flag:
                self.memory[n] = 1
                return True
            else:
                return False


def gen_perm(data):
        nums = []
        while data != 0:
            nums.append(data % 10)
            data = int(data/10)
        nums.sort(reverse=True)

        result = 0
        for n in nums:
            result = 10 * result + n

        return result


class Node:
    def __init__(self, box, below=None):
        self.data = box.data
        self.below = below

    def add_node(self, box):
        if self.data == box.data:
            pass
        else:
            if self.below == None:
                self.below = Node(box)
            else:
                self.below.add_node(box)


class Group:
    def __init__(self, box, next=None, below=None):
        self.perm = box.perm
        self.next = next
        self.below = Node(box)
        self.count = 1

    def add_node(self, box):
        if self.perm != box.perm:
            if self.next == None:
                self.next = Group(box)
            else:
                self.next.add_node(box)
        else:
            self.count += 1
            self.below.add_node(box)


class Box:
    def __init__(self, data):
        self.perm = gen_perm(data)
        self.data = data


def main():
    primes = Primes()

    primes.prime_update(10000)

    head = Group(Box(0))

    n = 1
    for p in primes.return_primes():
        if 1000 <= p < 10000:
            n += 1
            head.add_node(Box(p))
        if p >= 10000:
            break

    node1 = head
    while node1 != None:
        node2 = node1.below

        if node1.count > 2:
            #print(node1.perm)
            tmp = []
            while node2 != None:
                #print(node2.data, end=' ')
                tmp.append(node2.data)
                node2 = node2.below
            for i in range(len(tmp)):
                for j in range(i+1, len(tmp)):
                    middle = int((tmp[i] + tmp[j])/2)
                    if middle in tmp:
                        print(tmp[i], middle, tmp[j])
            #print('\n')

        node1 = node1.next


if __name__ == '__main__':
    main()
