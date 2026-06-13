class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr = []        
        for i in nums:
            arr.append(i * i)
        arr.sort()

        return arr
