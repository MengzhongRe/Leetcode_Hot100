#
# @lc app=leetcode.cn id=322 lang=python
#
# [322] 零钱兑换
#

# @lc code=start
# 动态规划-完全背包问题：这是一个经典的完全背包问题，背包容量为amount,物品数组为coins,coin可以被重复选取，且求的是
# 组合成amount的最小硬币数量，既然是极值问题，理论上内外层循环遍历顺序均可，由于是完全背包问题，所以需要正序遍历
# 设dp[i][j]为从前i个硬币中coins[:i]选取硬币能够凑出j的最小硬币数量，则考虑第i个硬币，我们有两种选择：1）不选取
# 该硬币，则此时凑出j的最小硬币数为dp[i - 1][j];2)选择该硬币，则此时为dp[i][j - coins[i]] + 1,取二者最小值即可
# 由此推导出一维dp数组dp[j] = min(dp[j],dp[j - coin] + 1),由于更新dp数组时需要考虑的是正上方和左侧数，因此从左到右
# 从上到下遍历即可。由于求的是最小值所以dp数组初始化为全float('inf'),但是dp[0] = 0,因为凑出0元钱只需要0个硬币即可
# 且dp[0]是后续dp数组推导的起始点！最后若dp[n]仍未float('inf')则说明无法凑出amount直接返回-1，否则返回dp[n]
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for j in range(coin,amount + 1):
                dp[j] = min(dp[j],dp[j - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1
# 时间复杂度O(S * N),S是需要凑出的金额数，N是len(coins)，外层循环遍历N次，内层循环最多需要遍历S次，一共是S * N
# 空间复杂度O(S),最多需要S + 1长度的一维滚动数组压缩状态    
# @lc code=end

