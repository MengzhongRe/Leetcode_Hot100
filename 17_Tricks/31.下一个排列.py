#
# @lc app=leetcode.cn id=31 lang=python
#
# [31] 下一个排列
#

# @lc code=start
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2

        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        if i >= 0:
            j = n - 1
            while j >= 0 and nums[i] >= nums[j]:
                j -= 1
            # 交换nums[i]与nums[j]
            nums[i],nums[j] = nums[j],nums[i]
        
        # 将i之后到末尾的整个降序序列反转为升序序列
        left,right = i + 1,n - 1
        while left < right:
            nums[left],nums[right] = nums[right],nums[left]
            left += 1
            right -= 1
# 时间复杂度O(N),最多两次遍历
# 空间复杂度O(1),原地操作，只用到常数个指针   
# @lc code=end

