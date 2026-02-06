#
# @lc app=leetcode.cn id=238 lang=python
#
# [238] 除了自身以外数组的乘积
#

# @lc code=start
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        answer = [1] * n
        # 左侧乘积遍历
        left_product = 1# 左侧第一个数的左侧乘积就是1
        for i in range(n): # 从左到右遍历数组
            answer[i] = left_product # 先更新左侧元素乘积
            left_product *= nums[i] # 再nums[i]更新左侧乘积，由于包含了nums[i],需供下一个位置元素使用
        
        right_product = 1 # 右侧第一个数的左侧乘积就是1
        for i in range(n-1,-1,-1): # 右侧乘积遍历
            answer[i] *= right_product # 直接把左侧乘积结果与右侧乘积结果相乘得到i位置的结果
            right_product *= nums[i] # 将Nums[i]更新右侧乘积结果供下一个位置使用
        
        return answer
# 时间复杂度O(N) 两次遍历数组无其他
# 空间复杂度O(1) answer作为结果数组不计算在内，只使用了left_product和right_product两个变量 
# @lc code=end

