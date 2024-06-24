def problem(nums, target):
    previous_map = {}
    for index, number in enumerate(nums):
        difference = target - number
        if difference in previous_map:
            return [previous_map[difference], index]
        previous_map[number] = index

nums = [2,7,11,15]
print(problem(nums, 9))