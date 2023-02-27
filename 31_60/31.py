

def main(lists, number):
    if lists == []:
        return []
    i = 0
    ways = []
    while True:
        tmp = number - i * lists[0]
        if tmp == 0:
            ways += [[i]]
            break
        elif tmp < 0:
            break
        else:
            ways += [[i] + r for r in main(lists[1:], tmp)]
            i += 1
    return ways


if __name__ == '__main__':
    print(len(main([1,2,5,10,20,50,100,200], 200)))