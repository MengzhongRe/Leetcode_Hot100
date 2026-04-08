#
# @lc app=leetcode.cn id=287 lang=python
#
# [287] 寻找重复数
#

# @lc code=start
# 快慢指针判链表环
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 第一阶段：快慢指针找相遇点
        slow,fast = 0,0
        while True:
            slow = nums[slow]   # 慢指针走一步
            fast = nums[nums[fast]] # 快指针走两步
            if slow == fast:    # 必定会相遇，因为有环
                break
        # 第二阶段：寻找入环点（重复数字）
        slow = 0    # 慢指针回到起点
        while slow != fast:     
            slow = nums[slow]
            fast = nums[fast]
        
        return slow # 相遇即为重复元素


# @lc code=end

