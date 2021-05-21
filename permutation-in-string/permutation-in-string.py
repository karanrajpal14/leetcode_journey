class Solution:
# Approach 1: Sliding window with ascii value sum check
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         s1_val = sum([ord(s) for s in s1])
#         end = len(s1)
        
#         for i in range(len(s2)):
#             substr = s2[i:i+end]
#             s2_val = sum([ord(s) for s in substr])
#             if s1_val == s2_val:
#                 return True
# Approach 2: Counter with dict check
    from collections import Counter
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_cnt = Counter(s1)
        right = len(s1)
        
        for i in range(len(s2)):
            substr_cnt = Counter(s2[i:i+right])
            if s1_cnt == substr_cnt:
                return True