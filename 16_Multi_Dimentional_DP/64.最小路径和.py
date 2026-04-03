#
# @lc app=leetcode.cn id=64 lang=python
#
# [64] 最小路径和
#

# @lc code=start
# 动态规划二维数组版本：dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for j in range(1,n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        for i in range(1,m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        
        return dp[-1][-1]
# @lc code=end
# 一行数组滚动变量版本
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        dp = [0] * n
        dp[0] = grid[0][0]
        for j in range(1,n):
            dp[j] = dp[j - 1] + grid[0][j]
        
        for i in range(1,m):
            dp[0] += grid[i][0]
            for j in range(1,n):
                dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]
        
        return dp[-1]