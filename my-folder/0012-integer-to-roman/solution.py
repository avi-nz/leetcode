class Solution:
    def intToRoman(self, num: int) -> str:
        answer = ""
        numbers_to_roman = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M",
        }
        L = dict(reversed(list(numbers_to_roman.items())))
        x = list(L.items())
        for key, value in x:
            if num // key:
                counter = num // key
                answer += (counter * value)
                num = num % key 
        return answer
                
            

        
