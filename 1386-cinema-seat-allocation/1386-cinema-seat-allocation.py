class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reserved = defaultdict(set)
        for row, seat in reservedSeats:
            if 2<= seat <= 9:
                reserved[row].add(seat)

        ans = (n - len(reserved)) * 2

        for row, seats in reserved.items():
            left = not ({2,3,4,5} & seats)
            right = not ({6,7,8,9} & seats)
            mid = not ({4,5,6,7} & seats)

            if left and right:
                ans += 2
            elif left or right or mid:
                ans += 1
        return ans