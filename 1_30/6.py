def diff(n):
    square_sum = int(n * (n + 1) * (2 * n + 1) / 6)
    sum_square = int(n * (n + 1) / 2) ** 2

    return sum_square - square_sum

def main():
    print(diff(100))

if __name__ == '__main__':
    main()