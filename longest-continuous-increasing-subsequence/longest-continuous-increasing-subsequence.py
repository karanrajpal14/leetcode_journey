class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        length = 0
        left = 0
        right = 0
        
        """
        The idea is to implement the sliding window technique.
        While iterating through the array, we continue "growing" the window
        until the current element is lesser than the previous. When we find a
        smaller or equal value, we reset the window.
        
        We also maintain the length of the window
        and only update it if we find a longer subsequence.
        """
        
        while right < len(nums):
            if right and nums[right] <= nums[right - 1]:
                left = right
            length = max(length, right - left + 1)
            right += 1
        
        return length