
class Collatz:
    def __init__(self):
        self.memory = []

        for i in range(0, 1000000):
            self.memory.append([i, -1])
        self.memory[1][1] = 1
    def calc(self, n):
        tmp = n

        i = 0

        while True:
            if tmp < 1000000 and self.memory[tmp][1] != -1:
                break

            if tmp % 2 == 1:
                tmp = 3 * tmp + 1
            else:
                tmp = int(tmp/2)
            i += 1
        self.memory[n][1] = self.memory[tmp][1] + i

        return self.memory[n]

if __name__ == '__main__':
    collatz = Collatz()
    max_length = 0
    max_value = 0
    for i in range(1, 1000000):
        temp = collatz.calc(i)
        if temp[1] > max_length:
            max_length = temp[1]
            max_value = i
    print(max_length, max_value)
