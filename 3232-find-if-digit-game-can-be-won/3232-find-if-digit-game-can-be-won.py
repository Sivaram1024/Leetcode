class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        x = 0
        y = 0
        for i in nums:
            if i < 10:
                x += i
            else:
                y += i
        return x != y
