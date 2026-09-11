class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        count = 0
        for num in range(100,999,2):
            num_str = str(num)
            is_valid = True

            for char in num_str:
                if num_str.count(char) > digits.count(int(char)):
                    is_valid = False
            if is_valid:
                count += 1
        return count