class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        return self.dfs(0, 0, m, n, dp)

    def dfs(self, i: int, j: int, m: int, n: int, dp: list) -> int:
        if i >= m or j >= n:
            return 0
        if i == m - 1 and j == n - 1:
            return 1
        
        if dp[i][j] != -1:
            return dp[i][j] 

        dp[i][j] = self.dfs(i + 1, j, m, n, dp) + self.dfs(i, j + 1, m, n, dp)

        return dp[i][j]
