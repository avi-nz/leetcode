class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current_best_string = set()
        left = 0
        result = 0
        for right in s:
            while right in current_best_string:
                current_best_string.remove(s[left])
                left += 1
            current_best_string.add(right)
            result = max(result, len(current_best_string))
        return result


            

