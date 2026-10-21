class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previous_numbers = {}
        for index, number in enumerate(nums):
            difference = target - number
            if difference in previous_numbers:
                return [previous_numbers[difference], index]
            previous_numbers[number] = index
