class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current_alt = 0
        max_alt = 0
        for i in gain:
            current_alt += i
            if current_alt > max_alt:
                max_alt = current_alt
        return max_alt