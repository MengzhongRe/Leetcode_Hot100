#
# @lc app=leetcode.cn id=62 lang=python
#
# [62] 不同路径
#

# @lc code=start
# 动态规划：
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # 初始化二维m行n列的dp数组
        dp = [[0] * n for _ in range(m)]
        for j in range(n):
            dp[0][j] = 1
        for i in range(m):
            dp[i][0] = 1
        
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        return dp[-1][-1]    
# @lc code=end
# 两行滚动变量版本
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        prev = [1] * n
       
        for i in range(1,m):
            curr = [0] * n
            curr[0] = 1
            for j in range(1,n):
                curr[j] = prev[j] + curr[j - 1]
            prev = curr
        return prev[-1]
# 一维滚动变量优化
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [1] * n
        for i in range(1,m):
            for j in range(1,n):
                dp[j] = dp[j] + dp[j - 1]
        return dp[-1]