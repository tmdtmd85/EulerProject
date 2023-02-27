

def yo(n, lists):
    tmp = []
    while True:
        tmp.append(n % 10)
        n = int(n/10)
        if n == 0:
            break

    for t in tmp[::-1]:
        lists.append(t)


if __name__ == '__main__':
    lists = []
    i = 0
    while True:
        yo(i, lists)
        if len(lists) > 1000000:
            break
        i += 1

    print(lists[1]*lists[10]*lists[100]*lists[1000]*lists[10000]*lists[100000]*lists[1000000])