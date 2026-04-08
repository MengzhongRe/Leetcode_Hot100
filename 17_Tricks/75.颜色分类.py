#
# @lc app=leetcode.cn id=75 lang=python
#
# [75] 颜色分类
#

# @lc code=start
# 荷兰国旗问题：三指针法
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left,curr,right = 0,0,len(nums) - 1

        while curr <= right:
            if nums[curr] == 0:
                nums[left],nums[curr] = nums[curr],nums[left]
                left += 1
                curr += 1
            elif nums[curr] == 1:
                curr += 1
            else:
                nums[curr],nums[right] = nums[right],nums[curr]
                right -= 1
# @lc code=end

