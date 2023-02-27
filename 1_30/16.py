

number = [1]
cursor = 0

for i in range(1000):
    for n in range(cursor + 1):
        number[n] *= 2

    for n in range(cursor):
        number[n+1] += int(number[n] / 10)
        number[n] %= 10
    if int(number[cursor]/10) >= 1:
        number.append(int(number[cursor]/10))
        number[cursor] %= 10
        cursor += 1
    print(i+1, number[::-1])

print(sum(number))




