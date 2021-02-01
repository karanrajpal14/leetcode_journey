import re

class Solution:
    def removeVowels(self, s: str) -> str:
        vowelsStripped = re.findall(r"[^aeiou]", s)
        return "".join(vowelsStripped)