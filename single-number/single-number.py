from collections import defaultdict

"""
    Approach:
    First, we must count the frequency of occurrences
    of each integer in the array. We can do this by
    making use of defaultdict collection.
    We then iterate over each number incrementing their
    count.
    
    Once we have this, we must find the element that
    has a count of 1. Again, we iterative over the
    freq dict we just created and once we find the
    element that has a value of 1, we return it's key.
    
    Time Complexity: O(n+n) => O(2n) => O(n)
    Space Complexity: O(n+n) => O(2n) => O(n)
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        
        for num in nums:
            freq[num] += 1
        
        for key, value in freq.items():
            if value == 1:
                return key