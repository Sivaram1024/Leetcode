class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        a = nums[(len(nums) - 1)] - 1
        b = nums[(len(nums) - 2)] - 1

        return a*b