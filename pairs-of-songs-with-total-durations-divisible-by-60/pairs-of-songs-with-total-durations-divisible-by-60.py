from collections import defaultdict

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        num_of_pairs = 0
        count = [0] * 60
        
        for t in range(len(time)):
            idx = time[t] % 60
            num_of_pairs += count[(60 - idx) % 60]
            count[idx] += 1
            
        return num_of_pairs