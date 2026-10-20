class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        left_pointer = 0
        right_pointer = len(height) - 1

        while left_pointer < right_pointer:
            max_height = min(height[left_pointer], height[right_pointer])
            max_area = (right_pointer - left_pointer) * max_height
            result = max(result, max_area)

            if height[left_pointer] < height[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1
        return result

