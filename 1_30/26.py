

if __name__ == '__main__':
    max_i = 0
    max_len = 0
    max_frac = []
    for i in range(2, 1000):
        cursor = 0
        a = [0]
        b = [1]
        while True:
            r = (b[cursor] * 10) % i
            if r in b:
                b.append(r)
                a.append(int(b[cursor] * 10 / i))
                cursor += 1
                if a[cursor] == 0:
                    a.pop()
                    cursor -= 1
                if cursor - b.index(r) > max_len:
                    max_len = cursor - b.index(r)
                    max_i = i
                    max_frac = a
                break
            b.append(r)
            a.append(int(b[cursor]*10/i))
            cursor += 1
    print(max_i, max_len, max_frac)
