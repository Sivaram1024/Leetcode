class Solution:
    def calPoints(self, operations: List[str]) -> int:
        arr = []
        for i in operations:
            try:
                val = int(i)
                arr.append(val)
            except ValueError:
                if i == "C":
                    arr.pop()
                elif i == "D":
                    arr.append(arr[-1] * 2)
                elif i == "+":
                    new_sum = arr[-1] + arr[-2]
                    arr.append(new_sum)
        return sum(arr)