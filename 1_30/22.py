
def calc_line(line, pos):
    sum = 0
    for c in line:
        sum += ord(c) - ord("A") + 1
    return sum * pos

if __name__ == '__main__':
    f = open("names.txt", "r")
    line = f.read()

    lines = sorted([line.replace('"', '') for line in line.split(",")])

    summation = 0

    for i in range(len(lines)):
        summation += calc_line(lines[i], i+1)
    print(summation)



