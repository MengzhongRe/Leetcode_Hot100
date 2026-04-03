#
# @lc app=leetcode.cn id=32 lang=python
#
# [32] 最长有效括号
#

# @lc code=start
# 动态规划：
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 边界判断：如果字符串s为空，则没有有效括号，返回0
        if not s:
            return 0
        n = len(s)
        dp = [0] * n 

        for i in range(1,n):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
                elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '(':
                    dp[i] = dp[i - 1] + 2 + (dp[i - dp[i - 1] - 2] if i - dp[i - 1] >= 2 else 0)
                                    
        return max(dp) 
# 时间复杂度O(N)
# 空间复杂度O(N)  
# @lc code=end