#
# @lc app=leetcode.cn id=45 lang=python
#
# [45] 跳跃游戏 II
#

# @lc code=start
# 贪心算法：我们在本题目维护三个滚动变量，times记录已经起跳的次数，max_pos记录如果起跳能够
# 达到的最远距离,end表示当前这一跳所能够达到的最远距离。我们的思路是：遍历数组，根据当前数字
# 更新能够达到的最远距离看max_pos,但是先不更新end和times,也就是先不跳，当且仅当i == end时，也就是目前
# 已经达到了上一跳的最远距离end时，我们才起跳，times += 1,但是我们未必是在i处起跳，而是某一个
# 能够达到当前更新后的max_pos的起跳位置j,使得j + nums[j] == max_pos，此时我们在j起跳。但是我们并不
# 关心j到底是多少，我们只关心这一跳能够达到的最远距离，j + nums[j] = max_pos,此时我们需要更新
# end = max_pos.同时，如果当前这一跳已经能够跳到最后一个元素或以后，就已经找到最小次数了，直接break掉循环
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        max_pos = 0
        times = 0
        end = 0

        for i in range(n - 1):
            # 更新能够达到的最远距离
            max_pos = max(max_pos,i + nums[i])
            # 仅当来到上一跳的边界时，我们才不得不起跳，times += 1
            # 并且我们是在j，使得j + nums[j] = max_pos的位置起跳的
            # 只是我们并不关心我们具体在哪个位置起跳的，我们只关心这新的一跳
            # 的边界在哪里，也就是需要赋值end = max_pos
            if i == end:
                times += 1
                end = max_pos
                # 剪枝：只要当前这一跳已经能够跳到最后一个元素或以后，就已经找到最小次数了
                if end >= n - 1:
                    break
        return times  
# 时间复杂度O(N),最多一次循环
# 空间复杂度O(1)
# @lc code=end

