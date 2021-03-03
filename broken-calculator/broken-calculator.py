class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        """
        Intuition:
        
        We look at this problem in reverse to be greedy
        about our solution.
        
        If Y < X, then doubling is useless.
        All we can do is decrement and to determine by how much,
        we just subtract Y from X.
        
        If Y > X, then we need to consider both operations.
        Until Y > X, we can repeatedly half our value and track
        how many times this happens. This is essentially our doubling count.
        
        Once Y becomes lesser than X, then our previous condition is applied.
        Only difference is that we need to add the doubling count to the diff
        b/x X and Y
        """
        
        res = 0
        
        while Y > X:
            res += 1
            
            if Y % 2 == 0:
                Y //= 2
            else:
                Y += 1
        
        return res + (X - Y)