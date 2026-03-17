#
# @lc app=leetcode.cn id=35 lang=python
#
# [35] 搜索插入位置
#

# @lc code=start

# 双指针二分查找
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 初始化左右指针
        left,right = 0,len(nums) - 1

        # 对区间[left,right]（闭区间）进行搜索
        # 不能写作left < right,因为在最后left == right时会漏掉对最后一个数的判断
        while left <= right: 
            # 不写mid = (left + right) // 2，防止left和right过大导致数值溢出
            # 由于right - left 一定比right小所以一定不会溢出
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target: # 如果目标值在右半区
                left = mid + 1 # 必须 + 1，防止死循环
            else:
                right = mid - 1 # 必须 - 1防止死循环
        
        # 当循环结束依然没有返回时说明没有找到该元素，我们需要返回插入位置
        # left == right,即mid = left = right有两种情况
        # 1.target < nums[mid],目标值在右半区，所以插入位置就是mid,执行right = mid - 1,left不动，所以left = mid
        # 2.target > nums[mid],目标值在右半区，所以插入位置是mid + 1,执行left = mid + 1符合条件
        # 所以无论什么时候，直接返回left
        return left
# 时间复杂度O(logn)
# 空间复杂度O(1)     
# @lc code=end

