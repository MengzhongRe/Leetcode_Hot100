#
# @lc app=leetcode.cn id=152 lang=python
#
# [152] 乘积最大子数组
#

# @lc code=start
import copy
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # 所有都初始化为数组的第一个元素
        curr_max = nums[0]  # 以目前数字结尾的连续子数组的最大乘积
        curr_min = nums[0]  # 以目前数字结尾的连续子数组的最小乘积
        ans = nums[0]   # 存储全局最大乘积
        # 从第二个元素开始遍历
        for i in range(1,n):
            num = nums[i]
            # 由于后续curr_max可能会被更新，但是curr_min的更新又依赖于curr_max的旧值
            # 所以需要先存储curr_max的旧值
            temp_max = curr_max
            # 新的最大数或最小数只有可能从这几个中产生！
            curr_max = max(num,temp_max * num,curr_min * num)
            curr_min = min(num,temp_max * num,curr_min * num)
            # 更新全局最大乘积
            ans = max(ans,curr_max)
        return ans
# 时间复杂度O(N),遍历一次数组即可
# 空间复杂度O(1),常数个辅助变量
        
# @lc code=end

