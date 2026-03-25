#
# @lc app=leetcode.cn id=121 lang=python
#
# [121] 买卖股票的最佳时机
#

# @lc code=start

# 贪心算法：我们维护两个滚动变量，一次遍历即可。min_price用于记录遍历过程中的最低价max_profit用于记录
# 直到今天的能获取的最大利润。每到新的一天，我们计算price - min_price的价格，即如果按照历史最低价买入，当天售出
# 可以获得的利润，然后和旧的max_profit取最大值即可，遍历结束即为答案。
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            max_profit = max(max_profit,price - min_price)
            min_price = min(min_price,price)
        return max_profit
# 时间复杂度O(N),遍历一次即可
# 空间复杂度O(1),常数个变量
# @lc code=end

