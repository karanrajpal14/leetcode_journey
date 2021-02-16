class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        
        # Reject invalid input
        if S is None or len(S) == 0:
            return []
        
        # Map of the last known index of every char in the imput string
        last_seen_indices = {char : idx for idx, char in enumerate(S)}
        
        # Two pointer method to keep track of the partition length
        left_ptr = 0
        right_ptr = 0
        
        # List to hold the partition size result
        partitions = []
        
        # Calculate partition size by iterating over the string
        for idx, char in enumerate(S):
            
            # Right pointer always keeps track of the end of a partition
            right_ptr = max(right_ptr, last_seen_indices[char])
            
            """
                When iteratior becomes equal to the right ptr value
                we have reached the end of one partition.
                Then we just have to calculate the size of the partition
                and increment the left pointer to move to the next partition
            """
            if right_ptr == idx:
                part_size = right_ptr - left_ptr + 1
                partitions.append(part_size)
                left_ptr = idx + 1
        
        return partitions
                
            
            