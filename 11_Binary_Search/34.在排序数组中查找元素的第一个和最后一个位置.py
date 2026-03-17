#
# @lc app=leetcode.cn id=34 lang=python
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start

# 用两次二分查找，一次找左边界，一次找右边界
# 关键在于while循环nums[mid] == target判断成功后，应该如何操作
# 找左边界时若nums[mid] == target,说明潜在的左边界还在左侧，此时需要收缩右指针即right= mid - 1
# 找右边界时若nums[mid] == target,说明潜在的右边界还在右侧，则收缩左指针left = mid + 1
# 其他和标准二分查找一样，
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 边界判断
        if not nums:
            return [-1,-1]
        # 内部定义函数，可以调用外部函数的参数，不需要额外穿参
        def get_left_border():
            left,right = 0,len(nums) - 1
            # 定义新变量用于存储左边界
            left_border = -1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    left_border = mid
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left_border
        
        def get_right_border():
            left,right = 0,len(nums) - 1
            # 定义新变量用于存储右边界
            right_border = -1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    right_border = mid
                    left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1  
            return right_border
        
        return [get_left_border(),get_right_border()]
# 时间复杂度O（logn）,两次二分查找分别是O(logn)
# 空间复杂度O(1)
# @lc code=end

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 边界判断
        if not nums:
            return [-1,-1]
        
        left,right = 0,len(nums) - 1
        mid = -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                break
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        if nums[mid] != target:
            return [-1,-1]
        
        left1 = left
        left2 = mid
        while left1 <= left2:
            mid_l = left1 + (left2 - left1) // 2
            if nums[mid_l] == target:
                left2 = mid_l - 1
            else:
                left1 = mid_l + 1
        
        right1 = mid
        right2 = right

        while right1 <= right2:
            mid_r = right1 + (right2 - right1) // 2
            if nums[mid_r] == target:
                right1 = mid_r + 1
            else:
                right2 = mid_r - 1
        
        return [left1,right2] 