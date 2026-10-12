class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = 0
        candite = None
        for num in nums:
            if count == 0:
                candite = num
            
            if num == candite:
                count += 1
            else:
                count -= 1
        return candite