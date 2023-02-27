

def generate(nums, n):
    if n == 1:
        if nums[0] != 0:
            return nums
        else:
            return []

    l = []
    for i in range(len(nums)):
        if i == 0:
            l += list(map(lambda g: nums[i] + 10*g, generate(nums[1:], n-1)))
        elif i == len(nums)-1:
            l += list(map(lambda g: nums[i] + 10*g, generate(nums[:i], n-1)))
        else:
            l += list(map(lambda g: nums[i] + 10*g, generate(nums[:i]+nums[i+1:], n-1)))

    if n == 4:
        return list(filter(lambda x: (x % 1000)%2 == 0, l))
    elif n == 5:
        return list(filter(lambda x: (x % 1000)%3 == 0, l))
    elif n == 6:
        return list(filter(lambda x: (x % 1000)%5 == 0, l))
    elif n == 7:
        return list(filter(lambda x: (x % 1000)%7 == 0, l))
    elif n == 8:
        return list(filter(lambda x: (x % 1000)%11 == 0, l))
    elif n == 9:
        return list(filter(lambda x: (x % 1000)%13 == 0, l))
    elif n == 10:
        return list(filter(lambda x: (x % 1000)%17 == 0, l))

    return l

if __name__ == '__main__':
    nums = [i for i in range(10)]
    perms = generate(nums, len(nums))
    print(sum(perms))
