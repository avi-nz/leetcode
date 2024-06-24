def problem(nums, target):
    result = []
    nums = sorted(nums)
    for index, number_a in enumerate(nums):
        if index > 0 and number_a == nums[index - 1]:
            continue
        left_pointer = index + 1
        right_pointer = len(nums) - 1

        while left_pointer < right_pointer:
            current_sum = number_a + nums[left_pointer] + nums[right_pointer]

            if current_sum > target:
                right_pointer -= 1
            elif current_sum < target:
                left_pointer += 1
            elif current_sum == target:
                result.append([number_a, nums[left_pointer], nums[right_pointer]])
                left_pointer += 1
                while left_pointer < right_pointer and nums[left_pointer] == nums[left_pointer - 1]:
                    left_pointer += 1
    return result

nums = [-1,0,1,2,-1,-4]
print(problem(nums, 0))

