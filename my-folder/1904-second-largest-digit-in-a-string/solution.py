class Solution:
    def secondHighest(self, s: str) -> int:
        large = -1
        second = -1
        for i in s:
            if i.isalpha():
                continue
            if int(i) == large:
                continue
            if int(i) > large:
                second = large
                large = int(i)
                continue 
            if int(i) > second:
                second = int(i)
        return second

        

        
