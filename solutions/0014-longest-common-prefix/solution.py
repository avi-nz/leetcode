class Solution:
    def longestCommonPrefix(self, s: List[str]) -> str:
        result = ""
        s = sorted(s)
        # first word in the list
        first = s[0]
        # last work in the list
        last = s[-1]
        # for loop that runs for the length of the shortest word in the list
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return result
            else:
                result += first[i]
        return result
            
