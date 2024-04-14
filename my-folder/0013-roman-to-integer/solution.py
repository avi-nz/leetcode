class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        letter_to_numbers = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        s_list = list(s)
        for letter in range(len(s)):
            if letter < (len(s) - 1) and letter_to_numbers[s[letter]] < letter_to_numbers[s[letter + 1]]:
                result -= letter_to_numbers[s[letter]]
            else:
                result += letter_to_numbers[s[letter]]
        return result

        
