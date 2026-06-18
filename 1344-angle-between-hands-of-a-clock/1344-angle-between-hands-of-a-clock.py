class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour = (hour % 12) * 30 + minutes * 0.5
        minutes = minutes * 6
        angle = abs(hour - minutes)
        return min(angle,360 - angle)