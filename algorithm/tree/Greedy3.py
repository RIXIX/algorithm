class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[::2])

# lesson learned
# [start:end:step]
# sort -> 0 , 2, 6 등 짝수가 작은값이 됨.
# 작은 값들의 최대 합을 나타낼 수 있음.