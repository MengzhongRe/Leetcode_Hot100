#
# @lc app=leetcode.cn id=739 lang=python
#
# [739] 每日温度
#

# @lc code=start

# 通过单调栈记录那些还没有找到答案，也就是后面比其温度高的日子的 「索引」，当找到比栈顶的温度
# 更高的温度的时候，弹出栈顶，然后进行清算，也就是计算 答案 = 当前索引 - 旧索引
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        ans = [0] * n # 初始化结果数组，全为0（如果找不到答案就是0）
        stack = [] # 初始化单调栈，用于记录未找到答案的索引
        # 遍历温度数组的索引
        for i in range(n):
            current_temp = temperatures[i]
            # 只要栈不为空，且当前的温度比栈顶的温度高，则说明找到了其答案
            while stack and current_temp > temperatures[stack[-1]]:
                # 则我们弹出栈顶的索引
                prev_index = stack.pop()
                # 清算：计算先前索引位置的答案，即当前索引 - 先前索引
                ans[prev_index] = i - prev_index
            # 无论弹出栈与否，都把当前索引弹出栈中（因为当前温度一定没有找到答案）
            stack.append(i)
        return ans
# 时间复杂度O(N),所有元素最多入栈一次，出栈一次，忽略其他常数项操作
# 空间复杂度O(N),栈最高为N      
# @lc code=end

