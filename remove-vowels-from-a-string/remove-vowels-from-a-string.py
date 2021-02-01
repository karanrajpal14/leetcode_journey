import re

class Solution:
    def removeVowels(self, s: str) -> str:
        # old approach
        # vowelsStripped = re.findall(r"[^aeiou]", s)
        # return "".join(vowelsStripped)
        
        vowelsStripped = []
        for char in s:
            if char not in ['a', 'e', 'i', 'o', 'u']:
                vowelsStripped.append(char)
                
        return "".join(vowelsStripped)