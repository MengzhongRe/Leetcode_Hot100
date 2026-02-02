#
# @lc app=leetcode.cn id=283 lang=python
#
# [283] 移动零
#

# @lc code=start
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1:
            return nums
        
        slow,fast = 0,0
        while fast < n:
            if nums[fast] != 0:
                nums[slow],nums[fast] = nums[fast],nums[slow]
                slow += 1
            fast += 1
        
        return nums

# 时间复杂度:O(N),其中N是数组的长度。我们只需要对数组进行一次遍历。
# 空间复杂度:O(1),我们只需要常数的空间存放    
# @lc code=end

