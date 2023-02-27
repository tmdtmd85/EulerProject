

HighCard = 0
OnePair = 1
TwoPairs = 2
ThreeOfAKind = 3
Straight = 4
Flush = 5
FullHouse = 6
FourOfAKind = 7
StraightFlush = 8
RoyalFlush = 9


def high_card(c, ref):
    tmp = []
    for i in c:
        tmp += i
    tmp.sort()
    if tmp[0] == 1:
        ref[0] = 14
        return True
    else:
        ref[0] = tmp[-1]
        return True


def is_one_pair(c, ref):
    for i in c:
        if len(i) == 2:
            ref[0] = i[0]
            return True
    ref[0] = -1
    return False


def is_two_pairs(c, ref):
    c.sort(key=lambda x: len(x))
    if len(c[-1]) == 2 and len(c[-2]) == 2:
        if min(c[-1][0], c[-2][0]) == 1:
            ref[0] = 14
            return True
        else:
            ref[0] = max(c[-1][0], c[-2][0])
            return True
    ref[0] = -1
    return False


def is_three_of_a_kind(c, ref):
    tmp = []
    for i in c:
        tmp += i
    tmp.sort()

    prev = tmp[0]
    flag = 1
    for t in tmp[1:]:
        if t != prev:
            if flag == 3:
                ref[0] = prev
                return True
            else:
                flag = 1
            prev = t
        else:
            flag += 1

    if flag == 3:
        ref[0] = prev
        return True
    else:
        ref[0] = -1
        return False


def is_straight(c, ref):
    tmp = []
    for i in c:
        tmp += i
    tmp.sort()

    if tmp[0] + 1 == tmp[1] and \
        tmp[1] + 1 == tmp[2] and \
            tmp[2] + 1 == tmp[3] and \
                tmp[3] + 1 == tmp[4]:
        if tmp[0] == 1:
            ref[0] = 14
            return True
        else:
            ref[0] = tmp[4]
            return True
    ref[0] = -1
    return False


def is_flush(c, ref):
    for i in c:
        if len(i) == 5:
            if min(i) == 1:
                ref[0] = 14
                return True
            else:
                ref[0] = max(i)
                return True
    ref[0] = -1
    return False


def is_full_house(c, ref):
    tmp = []

    for i in c:
        tmp += i
    tmp.sort()
    if tmp[0] == tmp[1] and tmp[3] == tmp[4] and (tmp[2] == tmp[1] or tmp[2] == tmp[3]):
        if tmp[2] == 1:
            ref[0] = 14
            return True
        else:
            ref[0] = tmp[2]
            return True
    else:
        ref[0] = -1
        return False


def is_four_of_a_kind(c, ref):
    for i in c:
        if len(i) == 4:
            ref[0] = i[0]
            return True
    ref[0] = -1
    return False


def is_straight_flush(c, ref):
    for i in c:
        if len(i) == 5 \
            and i[0] + 1 == i[1] \
                and i[1] + 1 == i[2] \
                    and i[2] + 1 == i[3] \
                        and i[3] + 1 == i[4]:
            ref[0] = i[4]
            return True
    ref[0] = -1
    return False


def is_royal_flush(c, ref):
    for i in c:
        if len(i) == 5 \
            and i[0] == 1 \
                and i[0] == 10 \
                    and i[1] == 11 \
                        and i[2] == 12 \
                            and i[3] == 13:
            ref[0] = 14
            return True
    ref[0] = -1
    return False


def yo(c, tmp, k):
    if c[0].isdigit():
        tmp[k].append(int(c[0]))
    else:
        if c[0] == 'A':
            tmp[k].append(1)
        elif c[0] == 'T':
            tmp[k].append(10)
        elif c[0] == 'J':
            tmp[k].append(11)
        elif c[0] == 'Q':
            tmp[k].append(12)
        elif c[0] == 'K':
            tmp[k].append(13)


def to(card):
    tmp = [[] for _ in range(4)]
    for c in card:
        if c[1] == 'S':
            yo(c, tmp, 0)
        elif c[1] == 'H':
            yo(c, tmp, 1)
        elif c[1] == 'D':
            yo(c, tmp, 2)
        elif c[1] == 'C':
            yo(c, tmp, 3)

    [tmp[i].sort() for i in range(4)]

    return tmp


def card(tmp, ref):
    if is_royal_flush(tmp, ref):
        return RoyalFlush
    elif is_straight_flush(tmp, ref):
        return StraightFlush
    elif is_four_of_a_kind(tmp, ref):
        return FourOfAKind
    elif is_full_house(tmp, ref):
        return FullHouse
    elif is_flush(tmp, ref):
        return Flush
    elif is_straight(tmp, ref):
        return Straight
    elif is_three_of_a_kind(tmp, ref):
        return ThreeOfAKind
    elif is_two_pairs(tmp, ref):
        return TwoPairs
    elif is_one_pair(tmp, ref):
        return OnePair
    else:
        return high_card(tmp, ref)


def hand(one, two):
    left = to(one)
    right = to(two)

    left_ref = [0]
    right_ref = [0]

    left_card = card(left, left_ref)
    right_card = card(right, right_ref)

    if left_card > right_card:
        return 1
    elif left_card < right_card:
        return 0
    else:
        print(left_card, right_card)
        if left_ref[0] > right_ref[0]:
            return 1
        elif left_ref[0] < right_ref[0]:
            return 0
        else:
            print("------")


if __name__ == '__main__':
    '''with open("poker.txt") as f:
        num1 = 0
        num2 = 0
        for l in f.readlines():
            tmp = l.strip('\n').split(' ')
            if hand(tmp[:5], tmp[5:]) == 1:
                num1 += 1
            else:
                num2 += 1
        print(num1, num2)'''

    print(hand(['5H', '5C', '6S', '7S', 'KD'], ['2C', '3S', '8S', '8D', 'TD']))
    print(hand(['5D', '8C', '9S', 'JS', 'AC'], ['2C', '5C', '7D', '8S', 'QH']))
    print(hand(['2D', '9C', 'AS', 'AH', 'AC'], ['3D', '6D', '7D', 'TD', 'QD']))
    print(hand(['4D', '6S', '9H', 'QH', 'QC'], ['3D', '6D', '7H', 'QD', 'QS']))
    print(hand(['2H', '2D', '4C', '4D', '4S'], ['3C', '3D', '3S', '9S', '9D']))


