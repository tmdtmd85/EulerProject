import math

def yo(n, memory):
    while True:
        memory[n % 10] += 1
        n = int(n/10)

        if n == 0:
            break

if __name__ == '__main__':
    maxval = 0
    for n in range(2, 10):
        tmp = [i for i in range(1, n+1)]

        len = int(9/n)

        for k in range(1, 10**len):
            memory = [0 for _ in range(10)]
            for t in tmp:
                yo(t*k, memory)

            if sum(memory[1:]) == 9 and not 0 in memory[1:]:
                print("=========")
                temp = 0
                for t in tmp:
                    print(str(k)+"*"+str(t)+"="+str(t*k))
                    temp = temp*10**int(math.log10(t*k)+1)+t*k
                if temp > maxval:
                    maxval = temp
                print(temp)

    print("---------")
    print(maxval)