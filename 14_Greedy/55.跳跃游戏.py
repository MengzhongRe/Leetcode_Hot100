#
# @lc app=leetcode.cn id=55 lang=python
#
# [55] 跳跃游戏
#

# @lc code=start
# 贪心算法：我们只需要维护一个变量cover表示目前能够到达的最远距离即可。具体而言：遍历数组，如果我们能
# 达到当前位置，即cover >= i,我们更新当前能到达的最远距离cover = max(cover,i + nums[i]),遍历
# 过程中，只要cover >= n - 1,就可以停止循环，返回True了，最后就返回cover >= n -1即可。
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        cover = 0

        for i,step in enumerate(nums):
            if cover >= i and cover < n - 1:
                curr_cover = i + step
                cover = max(cover,curr_cover)
            else:
                break

        return cover >= n - 1
# 时间复杂度O(N),只有一次遍历
# 空间复杂度O(1)
# @lc code=end

