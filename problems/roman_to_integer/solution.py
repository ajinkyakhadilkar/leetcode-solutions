from enum import Enum

class RomanNumeral(Enum):
    I = 1
    V = 5
    X = 10
    L = 50
    C = 100
    D = 500
    M = 1000

class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        for i in range(0, len(s) - 1):
            if RomanNumeral[s[i]].value < RomanNumeral[s[i+1]].value:
                num -= RomanNumeral[s[i]].value
            else :
                num += RomanNumeral[s[i]].value
        num += RomanNumeral[s[-1]].value
        return num