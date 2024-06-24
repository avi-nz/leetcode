def problem(nums, target):
    left_pointer = 0
    right_pointer = len(nums) - 1
    while left_pointer < right_pointer:
        current_sum = nums[left_pointer] + nums[right_pointer]

        if current_sum > target:
            right_pointer -= 1
        elif current_sum < target:
            left_pointer += 1
        elif current_sum == target:
            return [left_pointer + 1, right_pointer + 1]

nums = [2,7,11,15]
print(problem(nums, 9))