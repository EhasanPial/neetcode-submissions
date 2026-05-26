class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1 for i in range(n)]
        return self.runDp(0, n, nums, dp)

    def runDp(self, i: int, n: int, nums: List[int], dp: List[int]) -> int:
        if i >= n:
            return 0
        if dp[i] != -1:
            return dp[i]

        dp[i] = max(nums[i] + self.runDp(i + 2, n, nums, dp), self.runDp(i + 1, n, nums, dp))
        return dp[i]
