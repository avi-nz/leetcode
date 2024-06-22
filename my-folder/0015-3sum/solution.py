class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []
        tri_list = []

        def k_sum(k, starting_index, target):
            if k != 2:
                for i in range(starting_index, len(nums) - k + 1):
                    if i > starting_index and nums[i] == nums[i - 1]:
                        continue
                    tri_list.append(nums[i])
                    k_sum(k - 1, i + 1, target - nums[i])
                    tri_list.pop()
                return 
            left_pointer = starting_index
            right_pointer = len(nums) - 1
            while left_pointer < right_pointer:
                current_two_sum = nums[left_pointer] + nums[right_pointer]
                if current_two_sum > target:
                    right_pointer -= 1
                elif current_two_sum < target:
                    left_pointer += 1
                elif current_two_sum == target:
                    result.append(tri_list + [nums[left_pointer], nums[right_pointer]])
                    left_pointer += 1
                    while left_pointer < right_pointer and nums[left_pointer] == nums[left_pointer - 1]:
                        left_pointer += 1
        k_sum(3, 0, 0)
        return result

