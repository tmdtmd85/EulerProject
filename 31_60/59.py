

def generate():
    for i in range(ord('a'), ord('z')+1):
        for j in range(ord('a'), ord('z') + 1):
            for k in range(ord('a'), ord('z') + 1):
                yield i, j, k


def main():
    with open("p059_cipher.txt") as f:
        l = [int(code) for code in f.readline().split(',')]

    with open("words.txt") as f:
        words = [word.strip('\n') for word in f.readlines()]

    for g in generate():
        print(g)

        i = 0
        length = len(l)
        text = ""
        text_code = []
        while i < length:
            tmp = l[i:i+3]

            for t in range(3):
                ch_code = g[t] ^ tmp[t]
                text += chr(ch_code)
                text_code.append(ch_code)
            i += 3

        for word in words:
            if len(word) > 6 and word in text:
                print(word, text)
                print(sum(text_code))
                return

if __name__ == '__main__':
    main()