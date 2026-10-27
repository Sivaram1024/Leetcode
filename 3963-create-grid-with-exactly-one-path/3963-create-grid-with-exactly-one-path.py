class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = [['#']* n for i in range(m)]
        ans = ['.'*n]

        for i in range(m-1):
            ans.append('#' * (n-1) + '.')
        return ans