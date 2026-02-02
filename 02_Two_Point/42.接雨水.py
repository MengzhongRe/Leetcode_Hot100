#
# @lc app=leetcode.cn id=42 lang=python
#
# [42] 接雨水
#

# @lc code=start
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        left = 0
        right = len(height) - 1
        left_max = height[0]
        right_max = height[-1]
        res = 0

        while left < right:
            left_max = max(left_max,height[left])
            right_max = max(right_max,height[right])

            if left_max < right_max:
                res += left_max - height[left]
                left += 1
            else:
                res += right_max - height[right]
                right -= 1
        
        return res
# 时间复杂度:O(N),因为每个i被且仅被一个指针遍历一次
# 空间复杂度:O(1),只使用了常数个变量        
# @lc code=end

