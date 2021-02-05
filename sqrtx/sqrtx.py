class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        low = 2
        high = x // 2
        
        while low <= high:
            mid = (low + high) // 2
            sq = mid ** 2
        
            if sq < x:
                low = mid + 1
            elif sq > x:
                high = mid - 1
            else:
                return mid
        
        return high