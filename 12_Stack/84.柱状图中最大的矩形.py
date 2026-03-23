#
# @lc app=leetcode.cn id=84 lang=python
#
# [84] 柱状图中最大的矩形
#

# @lc code=start

# 单调栈寻找每个栈的左右边界：我们的想法是以每个数组索引i的高度heights[i]为潜在大矩形的高度，这个时候我们要求两侧的小矩形高度
# 至少要和heights[i]一样高才能成为大矩形，因此我们找那些比heights[i]矮的heights[j]，也就是该索引的左右边界了。这其实就是739
# 每日温度的升级版，每日温度是只找右边界，且是比它高的，这个则是左右边界都找，而且找比它矮的。我们考虑用单调栈来处理，同时在原数组
# 的首尾加上0的哨兵元素，方便处理当原数组是完全单调递增时无法弹栈清算的特殊条件。

# 核心操作在于先初始化一个栈，按顺序遍历原数组索引，若索引对应高度小于栈顶对应高度，则表明其是栈顶元素的右边界，我们弹出栈顶元素
# 以该索引对应高度计算大矩形的面积，我们已经找到右边界，还需要找到左边界，大矩形的宽度就能确定了。事实上，弹出栈顶元素后的新栈顶
# 索引就是该大矩形的左边界：1）首先该索引对应高度一定比原栈顶索引高度小，因为如果前者比后者大，则后者加入栈前就会把前者pop出栈
# 并且该索引高度一定是比原先索引高度小的左侧第一个，因为原先索引进栈时会先把所有比它高的索引都pop掉，最后剩下那个左边界了
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # 原数组首尾加上哨兵0，防止原数组递增情况下，无法进行清算
        heights = [0] + heights + [0]
        n = len(heights)
        max_area = 0
        stack = [0] # 初始化单调栈，先把数组首位烧饼索引0加入栈中
        # 因为第一个哨兵已经加入了，所以直接从1开始遍历，一直到最后一位n - 1
        for i in range(1,n):
            # 如果挑战者比栈顶高度小，则说明其是栈顶的右边界
            while heights[i] < heights[stack[-1]]:
                # 此时，取出栈顶元素，以其高度为大矩形高度进行清算
                cur_height = heights[stack.pop()]
                # 左边界就是pop掉后新栈顶索引
                left_index = stack[-1]
                # 大矩形宽度就是右边界 - 左边界 - 1
                cur_width = i - left_index - 1
                # 更新面积最大值
                max_area = max(max_area,cur_height * cur_width)
                # 清算完毕后，或挑战者比栈顶高时，直接入栈，后续进行清算（计算其矩形面积）
            stack.append(i)
        return max_area
# 时间复杂度O(N)，每个元素入栈出栈一次
# 空间复杂度O(N)
# @lc code=end

