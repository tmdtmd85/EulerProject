

class tri:
    def __init__(self):
        self.tri_list = [1]
        self.n = 0

    def is_tri(self, k):
        while self.tri_list[self.n] < k:
            self.n += 1
            self.tri_list.append(int(self.n*(self.n+1)/2))

        if k in self.tri_list:
            return True
        else:
            return False


def value(ch):
    return ord(ch)-ord('A') + 1


def word_val(w):
    val = 0
    for ch in w:
        val += value(ch)
    return val


if __name__ == '__main__':
    with open("words.txt") as f:
        words = f.readlines()[0]

        words = list(map(lambda w: word_val(w.strip('"')), words.split(',')))

    t = tri()

    print(list(map(lambda w: t.is_tri(w), words)).count(True))
