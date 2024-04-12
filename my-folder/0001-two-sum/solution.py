class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for num in range(len(nums) - 1):
            for n in range(num + 1, len(nums)):
                if nums[num] + nums[n] == target:
                    return num, n

            
