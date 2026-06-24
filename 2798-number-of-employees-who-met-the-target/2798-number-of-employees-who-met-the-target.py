class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        target_hrs = 0
        for i in hours:
            if i >= target:
                target_hrs += 1
        return target_hrs