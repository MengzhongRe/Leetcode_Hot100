#
# @lc app=leetcode.cn id=70 lang=python
#
# [70] 爬楼梯
#

# @lc code=start
# 一维数组动态规划：维护一个长为(n + 1)一维数组,其中dp[i]表示爬到i阶楼梯有多少种方法，则根据题意可知
# 爬到第i层，要么从i - 1层爬一步上来，要么从i - 2层爬两步上来，也就是dp[i] = dp[i - 1] + dp[i - 2]
# 这样递推公式就确定了。
# 初始化：显然爬到第1层只有一种方法，所以dp][1] = 1,而dp[0] = 1，后续再通过递归公式确定
# 遍历方向：我们是从低往高爬的，所以我们从i从小到大遍历，最后到遍历到n从而确定dp[n]
# 答案：根据dp数组定义，dp[n]就代表爬到第n层的方法数量
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 1)
        dp[0],dp[1] = 1,1
        for i in range(2,n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
# 时间复杂度O(N),需要遍历整个数组
# 空间复杂度O(N),需要维护一个和数组等长的dp数组
# @lc code=end
# 动态规划滚动变量优化版：由递推公式；dp[i] = dp[i -1] + dp[i - 2]，在进行动态数组更新时，我们并不需要所有的先前
# 状态，我们仅需要前两个状态，因此我们完全可以不需要先前的其他状态.我们只需要维护两个变量，cur表示当前n层的方法，prev
# 表示上一层的方法，在计算下一层的方法数时，先用一个临时变量存储旧cur值,然后更新cur = prev + cur,然后把prev更新到
# 旧的cur即tmp即可，这样空间复杂度就降低到O(1) 
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        prev,cur = 1,1
        for _ in range(2,n + 1):
            tmp = cur
            cur = prev + cur
            prev = tmp
        return cur
# 时间复杂度O(N)
# 空间复杂度O(1)