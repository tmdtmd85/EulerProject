

def calc(n):
    sum = 0
    while True:
        sum += (n % 10)**5
        n = int(n/10)
        if n == 0:
            break
    return sum

if __name__ == '__main__':
    summation = 0
    for i in range(2, 1000000):
        if i == calc(i):
            print(i)
            summation += i
    print(summation)

#for i in range(1000000):
