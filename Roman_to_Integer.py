class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {"I": 1, "V": 5, "X": 10, "L":50, "C":100, "D":500, "M": 1000, " ": 0}
        total = 0
        s += " "
        i=0
        while i < len(s):
            if s[i] == "C" and (s[i+1] == "D" or s[i+1] == "M"):
                total += (romans[s[i+1]] - romans[s[i]])
                i+=2
            elif s[i] == "X" and (s[i+1] == "L" or s[i+1] == "C"):
                total += (romans[s[i+1]] - romans[s[i]])
                i+=2
            elif s[i] == "I" and (s[i+1] == "X" or s[i+1] == "V"):
                total += (romans[s[i+1]] - romans[s[i]])
                i+=2
            else:
                total += romans[s[i]]
                i+=1
        return total



s = input("Give me a roman numeral: ")


print(Solution().romanToInt(s))
