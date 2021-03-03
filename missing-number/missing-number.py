class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        Intuition:
        
        If the number wasn't missing, the array have n
        consecutive numbers from [0, n]. This sum subtracted
        by the sum of the incoming array should give us our answer
        
        sum of n consec numbers = (n / 2) * [2a + (n-1)d]
        a is the first num which is always zero
        d is the difference between each num which is always 1
        formula reduced to sn = (n/2) * (n-1)
        """
        ln = len(nums) + 1
        ap_sum = int((ln / 2) * (ln - 1))
        
        return ap_sum - sum(nums)
        