class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num_set_1 = set(nums1)
        num_set_2 = set(nums2)
        return [num for num in num_set_1 if num in num_set_2]