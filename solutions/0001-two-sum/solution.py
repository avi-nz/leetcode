class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previous_map = {}
        for index, number in enumerate(nums):
            difference = target - number
            if difference in previous_map:
                return [previous_map[difference], index]
            previous_map[number] = index
