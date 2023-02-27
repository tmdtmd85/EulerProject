


if __name__ == '__main__':
    max_num = 0
    max_p = 0
    for p in range(3, 1000+1):
        sol_num = 0
        for a in range(1, p):
            if a**2 % (p-a) == 0:
                c = p-a+a**2/(p-a)
                b = p-a-a**2/(p-a)

                b = int(b/2)
                c = int(c/2)

                if a <= b:
                    sol_num += 1
        if max_num < sol_num:
            max_num = sol_num
            max_p = p

    print(max_p, max_num)
