class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        ele_sum = 0
        digi_sum = 0
        for i in nums:
            ele_sum += i
            temp = i
            while temp>0:
                digi_sum += temp % 10
                temp //= 10
        return abs(ele_sum - digi_sum)