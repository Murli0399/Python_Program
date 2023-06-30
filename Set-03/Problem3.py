def two_sum(nums, target):
    map = {}

    for i, num in enumerate(nums):
        print(i,num)
        complement = target - num
        if complement in map:
            return [map[complement], i]
        map[num] = i

    return []

nums = [2, 7, 11, 15]
target = 9

indices = two_sum(nums, target)

print(indices)
