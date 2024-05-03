class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_list = nums1 + nums2
        merged_list.sort()
        if len(merged_list) % 2 == 0:
            middle_index = (len(merged_list) - 1)/2
            middle_index_plus_one = middle_index + 1
            x = ((merged_list[int(middle_index_plus_one)]) + (merged_list[int(middle_index)])) / 2
            return x

        else:
            middle_index = (len(merged_list) - 1)/2
            return merged_list[int(middle_index)]


        
        
