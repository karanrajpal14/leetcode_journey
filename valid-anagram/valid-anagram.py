from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Sanitization
        s = s.replace(" ", "").lower()
        t = t.replace(" ", "").lower()
        
        # Edge case check
        if len(s) != len(t):
            return False
        
        # Approach 1 - From scratch
        
        
        # count = {}
        
        # for char in s:
        #     if char in count:
        #         count[char] += 1
        #     else:
        #         count[char] = 1
        
        # for char in t:
        #     if char in count:
        #         count[char] -= 1
        #     else:
        #         count[char] = 1
        
        # for i in count:
        #     if count[i] != 0:
        #         return False
                
        # return True
        
        
        # Approach 2 - Using Counter
        
        # return Counter(s) == Counter(t)
        
        
        # Approach 3 - Sorting both strings
        
        return sorted(s) == sorted(t)