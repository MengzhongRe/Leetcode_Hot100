#
# @lc app=leetcode.cn id=1143 lang=python
#
# [1143] 最长公共子序列
#

# @lc code=start

# 动态规划：dp[i][j]表示s1前i个字符的子串与前j个s2的字符子串的最长公共子序列的长度
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        m,n = len(text1),len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1,m + 1):
            for j in range(1,n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j],dp[i][j -1])
        
        return dp[-1][-1]
# 时间复杂度o(m * n)
# 时间复杂度O(m * n)
# @lc code=end

# 两行滚动数组优化
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        # 始终让空间复杂度取决于较短的字符串，极致省内存
        if len(text1) < len(text2):
            text1,text2 = text2,text1
        m,n = len(text1),len(text2)

        prev = [0] * (n + 1)
        curr = [0] * (n + 1)
        for i in range(1,m + 1):
            for j in range(1,n + 1):
                if text1[i - 1] == text2[j - 1]:
                    curr[j] = prev[j - 1] + 1
                else:
                    curr[j] = max(prev[j],curr[j - 1])
            prev,curr = curr,prev
        
        return prev[-1]
# 时间复杂度o(m * n)
# 时间复杂度O(min(m,n))
# 
# 一行滚动数组优化    
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        # 始终让空间复杂度取决于较短的字符串
        if len(text1) < len(text2):
            text1,text2 = text2,text1
        
        m,n = len(text1),len(text2)
        dp = [0] * (n + 1)
        
        for i in range(1,m + 1):
            # 每开启新的一行，最初的“左上角”（也就是上一行的 dp[0]）总是 0
            left_up = dp[0]
            for j in range(1,n + 1):
                # 【关键动作】：在覆盖 dp[j] 之前，先把它暂存下来！
                # 现在的 dp[j] 是上一行的旧值（正上方）
                # 等到下一次循环算 j+1 时，它就变成了 j+1 的左上角！
                next_left_up = dp[j]
                if text1[i - 1] == text2[j - 1]:
                    # 匹配成功：依赖刚才传过来的“左上角”
                    dp[j] = left_up + 1
                else:
                    # 匹配失败：依赖正左方(dp[j-1]) 和 正上方(原本的dp[j])
                    dp[j] = max(dp[j],dp[j - 1])
                # 【接力传递】：把当前暂存下来的 temp 交给下一轮去当“左上角”
                left_up = next_left_up
        return dp[-1]
# 时间复杂度O(m * n)
# 空间复杂度o(min(M,N))
