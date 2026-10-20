class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left_pointer = 0
        right_pointer = len(nums) - 1

        while left_pointer <= right_pointer:
            middle = (left_pointer + right_pointer) // 2

            if nums[middle] == target:
                return middle
    
            if target > nums[middle]:
                left_pointer = middle + 1
            else:
                right_pointer = middle - 1
        return left_pointer
        
