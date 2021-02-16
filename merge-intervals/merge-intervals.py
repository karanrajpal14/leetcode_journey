class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged_intervals = []
        
        """
            First, we need to ensure that the list is sorted based on the
            starting intervals. The decision to merge or not is based on this.
            
            To decide whether we will merge an interval or not, we need to
            compare the ending time of the previous interval with the
            starting time of the current interval.
            
            If this becomes true, it means that an overlap is present and
            we choose the greater of these two values as the ending time of the
            interval thereby merging it.
        """
        
        for interval in sorted(intervals, key=lambda x: x[0]):
            if merged_intervals and interval[0] <= merged_intervals[-1][1]:
                merged_intervals[-1][1] = max(merged_intervals[-1][1], interval[1])
            else:
                merged_intervals.append(interval)
        
        return merged_intervals