class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_list = nums1 + nums2
        merged_list.sort()

        left_pointer = 0
        right_pointer = len(merged_list) - 1

        while left_pointer <= right_pointer:
            if left_pointer == right_pointer:
                return (merged_list[left_pointer])
            elif left_pointer == right_pointer - 1:
                right_plus_left_pointers = merged_list[left_pointer] + merged_list[right_pointer]
                return right_plus_left_pointers / 2
            else:
                left_pointer += 1
                right_pointer -= 1
