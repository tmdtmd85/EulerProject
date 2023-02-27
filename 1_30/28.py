
sum = 0
i = 1
counter = 0
adder = 0
while True:
    print(i)
    sum += i

    if counter % 4 == 0:
        counter = 0
        adder += 2

    if i == 1001*1001:
        break
    i += adder
    counter += 1
print(sum)
