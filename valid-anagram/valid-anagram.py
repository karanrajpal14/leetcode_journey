class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Approach 1 - From scratch
        s = s.replace(" ", "").lower()
        t = t.replace(" ", "").lower()
        
        if len(s) != len(t):
            return False
        
        count = {}
        
        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        
        for char in t:
            if char in count:
                count[char] -= 1
            else:
                count[char] = 1
        
        for i in count:
            if count[i] != 0:
                return False
                
        return True