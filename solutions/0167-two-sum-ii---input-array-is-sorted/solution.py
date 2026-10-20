class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_pointer = 0
        right_pointer = len(numbers) - 1

        while right_pointer > left_pointer:
            current_two_sum = numbers[left_pointer] + numbers[right_pointer]

            if current_two_sum > target:
                right_pointer -= 1
            elif current_two_sum < target:
                left_pointer += 1
            elif current_two_sum == target:
                return [left_pointer + 1, right_pointer + 1]

        
