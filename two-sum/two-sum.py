class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, num in enumerate(nums):
            num2 = target - num
            if num2 in d.keys():
                return [i, d.get(num2)]
            else: d[num] = i