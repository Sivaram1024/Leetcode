class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        count = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1] + 1:  #checks the numbers are in sequence or not
                break
            count += nums[i]
        while count in nums:
            count += 1
        return count