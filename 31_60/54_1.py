
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


def is_high_card(tmp1, tmp2, ref):
    if tmp2[1] >0:
        ref[0] = 14
        return True
    else:
        for i in range(len(tmp2)-1, 0, -1):
            if tmp2[i] > 0:
                ref[0] = i
                return True
    ref[0] = -1
    return False


def is_one_pair(tmp1, tmp2, ref):
    for i in range(1, len(tmp2)):
        if tmp2[i] == 2:
            if i == 1:
                ref[0] = 14
            else:
                ref[0] = i
            return True
    ref[0] = -1
    return False


def is_two_pairs(tmp1, tmp2, ref):
    flag = 0
    ref[0] = -1
    for i in range(1, len(tmp2)):
        if tmp2[i] == 2:
            flag += 1
            if i == 1:
                ref[0] = max(ref[0], 14)
            else:
                ref[0] = max(ref[0], i)
    if flag == 2:
        return True
    return False


def is_three_of_a_kind(tmp1, tmp2, ref):
    for i in range(1, len(tmp2)):
        if tmp2[i] == 3:
            if i == 1:
                ref[0] = 14
            else:
                ref[0] = i

            return True
    ref[0] = -1
    return False


def is_straight(tmp1, tmp2, ref):
    for i in range(1, len(tmp2)-4):
        if tmp2[i] == 1:
            if tmp2[i+1] == 1 and \
                tmp2[i+2] == 1 and \
                    tmp2[i+3] == 1 and \
                        tmp2[i+4] == 1:
                if i == 1:
                    ref[0] = 14
                else:
                    ref[0] = i+4
                return True
    ref[0] = -1
    return False


def is_flush(tmp1, tmp2, ref):
    for i in tmp1:
        if len(i) == 5:
            if min(i) == 1:
                ref[0] = 14
            else:
                ref[0] = max(i)
            return True
    ref[0] = -1
    return False


def is_full_house(tmp1, tmp2, ref):
    flag = 0
    ref[0] = -1
    for i in range(1, len(tmp2)):
        if tmp2[i] == 2:
            flag += 1
            break
    for i in range(1, len(tmp2)):
        if tmp2[i] == 3:
            flag += 1
            if i == 1:
                ref[0] = 14
            else:
                ref[0] = i
            break

    if flag == 2:
        return True
    else:
        return False


def is_four_of_a_kind(tmp1, tmp2, ref):
    for i in range(1, len(tmp2)):
        if tmp2[i] == 4:
            if i == 1:
                ref[0] = 14
            else:
                ref[0] = i
            return True
        else:
            ref[0] = -1
            return False


def is_straight_flush(tmp1, tmp2, ref):
    for i in tmp1:
        if len(i) == 5 and \
            i[0] + 1 == i[1] and \
                i[1] + 1 == i[2] and \
                    i[2] + 1 == i[3] and \
                        i[3] + 1 == i[4]:
            if i[0] == 1:
                ref[0] = 14
            else:
                ref[0] = max(i)
            return True
    ref[0] = -1
    return False


def is_royal_flush(tmp1, tmp2, ref):
    for i in tmp1:
        if len(i) == 5 and \
            i[0] == 1 and \
                i[1] == 10 and \
                    i[2] == 11 and \
                        i[3] == 12 and \
                            i[4] == 13:
            ref[0] = 14
            return True
    ref[0] = -1
    return False


def hand(tmp1, tmp2):
    ref = [0]
    if is_royal_flush(tmp1, tmp2, ref):
        return RoyalFlush, ref[0]
    elif is_straight_flush(tmp1, tmp2, ref):
        return StraightFlush, ref[0]
    elif is_four_of_a_kind(tmp1, tmp2, ref):
        return FourOfAKind, ref[0]
    elif is_full_house(tmp1, tmp2, ref):
        return FullHouse, ref[0]
    elif is_flush(tmp1, tmp2, ref):
        return Flush, ref[0]
    elif is_straight(tmp1, tmp2, ref):
        return Straight, ref[0]
    elif is_three_of_a_kind(tmp1, tmp2, ref):
        return ThreeOfAKind, ref[0]
    elif is_two_pairs(tmp1, tmp2, ref):
        return TwoPairs, ref[0]
    elif is_one_pair(tmp1, tmp2, ref):
        return OnePair, ref[0]
    elif is_high_card(tmp1, tmp2, ref):
        return HighCard, ref[0]


def yo(c, tmp1, k, tmp2):
    if c[0].isdigit():
        tmp1[k].append(int(c[0]))
        tmp2[int(c[0])] += 1
    else:
        if c[0] == 'A':
            tmp1[k].append(1)
            tmp2[1] += 1
        elif c[0] == 'T':
            tmp1[k].append(10)
            tmp2[10] += 1
        elif c[0] == 'J':
            tmp1[k].append(11)
            tmp2[11] += 1
        elif c[0] == 'Q':
            tmp1[k].append(12)
            tmp2[12] += 1
        elif c[0] == 'K':
            tmp1[k].append(13)
            tmp2[13] += 1


def preproc(hand):
    tmp1 = [[] for _ in range(4)]
    tmp2 = [0 for _ in range(14)]
    for card in hand:
        if card[1] == 'S':
            yo(card, tmp1, 0, tmp2)
        elif card[1] == 'H':
            yo(card, tmp1, 1, tmp2)
        elif card[1] == 'D':
            yo(card, tmp1, 2, tmp2)
        elif card[1] == 'C':
            yo(card, tmp1, 3, tmp2)

    [tmp1[i].sort() for i in range(4)]

    return tmp1, tmp2


if __name__ == '__main__':
    with open("poker.txt") as f:
        num1 = 0
        num2 = 0
        for l in f.readlines():
            tmp = l.strip('\n').split(' ')

            left_tmp1, left_tmp2 = preproc(tmp[:5])
            left = hand(left_tmp1, left_tmp2)

            right_tmp1, right_tmp2 = preproc(tmp[5:])
            right = hand(right_tmp1, right_tmp2)

            if left[0] > right[0]:
                num1 += 1
                print("Player 1 win!!")
            elif left[0] < right[0]:
                num2 += 1
                print("Player 2 win!!")
            else:
                if left[1] > right[1]:
                    num1 += 1
                    print("Player 1 win!!")
                elif left[1] < right[1]:
                    num2 += 1
                    print("Player 2 win!!")
                else:
                    if left_tmp2[1] != 0 and right_tmp2[1] == 0:
                        num1 += 1
                        print("Player 1 win!!")
                    elif left_tmp2[1] == 0 and right_tmp2[1] != 0:
                        num2 += 1
                        print("Player 2 win!!")
                    else:
                        for i in range(13, 0, -1):
                            if left_tmp2[i] != 0 and right_tmp2[i] == 0:
                                num1 += 1
                                print("Player 1 win!!")
                                break
                            elif left_tmp2[i] == 0 and right_tmp2[i] != 0:
                                num2 += 1
                                print("Player 2 win!!")
                                break

    print(num1, num2)
