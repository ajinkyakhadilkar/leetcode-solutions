from enum import Enum

class Solution:
    def romanToInt(self, s: str) -> int:
        romanNumeral = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        num = 0
        for i in range(0, len(s) - 1):
            if romanNumeral[s[i]] < romanNumeral[s[i+1]]:
                num -= romanNumeral[s[i]]
            else :
                num += romanNumeral[s[i]]
        num += romanNumeral[s[-1]]
        return num

