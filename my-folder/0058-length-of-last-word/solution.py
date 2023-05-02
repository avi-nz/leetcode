class Solution:
    def lengthOfLastWord(self, s: str) -> int:
            li = list(s.split(" "))
            print(li)
            last_el = li[-1]
            print(last_el)
            if last_el:
                print("Hellow")
            else:
                x = 1
                while not last_el:
                    last_el = li[-x]
                    x += 1
            last_el_len = len(last_el)
            print(last_el_len)
            return last_el_len
            
