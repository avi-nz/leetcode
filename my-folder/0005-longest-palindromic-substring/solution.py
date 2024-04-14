class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]

        for i in range(len(s)):
            check_1 = expand(i, i)
            if len(check_1) > len(result):
                result = check_1
            check_2 = expand(i, i+1)
            if len(check_2) > len(result):
                result = check_2
        return result
            


        
