
thousand = {1000: len("one thousand".replace(' ',''))}
hundred = {100: len("hundred")}
ten = {10: len("ten"), 11: len("eleven"), 12: len("twelve"), 13: len("thirteen"), 14: len("fourteen"), 15: len("fifteen"), 16: len("sixteen"), 17: len("seventeen"), 18: len("eighteen"), 19: len("nineteen"),
    20: len("twenty"), 30: len("thirty"), 40: len("forty"), 50: len("fifty"), 60: len("sixty"), 70: len("seventy"), 80: len("eighty"), 90: len("ninety")}
one = {0: 0, 1: len("one"), 2: len("two"), 3: len("three"), 4: len("four"), 5: len("five"), 6: len("six"), 7: len("seven"), 8: len("eight"), 9: len("nine")}

_and = len("and")

def count(n):
    sum = 0
    if n / 1000 >= 1:
        sum += thousand[1000]
        n %= 1000
    if n / 100 >= 1:
        sum += one[int(n/100)]
        sum += hundred[100]
        n %= 100
        if n > 0:
            sum += _and
    if n >= 20:
        sum += ten[int(n/10)*10]
        n %= 10
        sum += one[n]
    else:
        if n / 10 >= 1:
            sum += ten[n]
        else:
            sum += one[n]
    return sum


if __name__ == '__main__':
    summation = 0
    for i in range(1, 1000 + 1):
        summation += count(i)
    print(summation)
