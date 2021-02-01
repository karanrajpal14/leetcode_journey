import re

class Solution:
    def removeVowels(self, s: str) -> str:
        # approach 1
        # vowelsStripped = re.findall(r"[^aeiou]", s)
        # return "".join(vowelsStripped)
        
        # Approach 2        
        # vowelsStripped = []
        # for char in s:
        #   if char not in ['a', 'e', 'i', 'o', 'u']:
        #       vowelsStripped.append(char)
                
        # return "".join(vowelsStripped)
        
        
        # Approach 3
        vowelSet = set()
        vowelSet.add('a')
        vowelSet.add('e')
        vowelSet.add('i')
        vowelSet.add('o')
        vowelSet.add('u')
        
        vowelsStripped = ""
        for char in s:
            if char not in vowelSet:
                vowelsStripped += char
        
        return vowelsStripped