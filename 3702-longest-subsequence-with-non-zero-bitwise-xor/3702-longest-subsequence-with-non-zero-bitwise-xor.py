class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        total = 0
        zero = False

        for x in nums:
            total ^= x
            if x!= 0:
                zero = True

        if total != 0:
            return len(nums)
        elif zero:
            return len(nums) - 1
        else:
            return 0