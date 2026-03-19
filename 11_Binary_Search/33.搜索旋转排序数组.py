#
# @lc app=leetcode.cn id=33 lang=python
#
# [33] 搜索旋转排序数组
#

# @lc code=start
# 解法一：先通过一次while二分查找找出旋转点（左侧）k，此时（0，k）是严格升序数组，（k+1,n - 1）
# 也是严格升序数组，此时对两边分别调用二分查找汇总结果即可
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if n == 1: # 主逻辑不能判断n为1的情况，因此必须独立判断
            if nums[0] == target:
                return 0
            else:
                return -1

        left,right = 0,n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid + 1]:# 判断当前mid是否是左侧旋转点
                break # 如果是直接break掉循环
            if nums[mid] > nums[n - 1]: # 
                left = mid + 1
            else:
                right = mid - 1

        def binary_search(left,right):
            while left <= right:
                mid_n = left + (right - left) // 2
                if nums[mid_n] == target:
                    return mid_n
                if nums[mid_n] < target:
                    left = mid_n + 1
                else:
                    right = mid_n - 1
            return -1

        res1 = binary_search(0,mid)
        return res1 if res1 != -1 else binary_search(mid + 1,n - 1) 
# 时间复杂度O(log)，两次二分查找，2log(n)
# 空间复杂度O(1)    
# @lc code=end

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        left,right = 0,n - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target: # 先判断当前点是不是目标值
                return mid
            if nums[left] <= nums[mid]: # 左半边是严格升序
                # 既然左半边是升序，看看target在不在这个范围内
                if nums[left] <= target < nums[mid]: # 在左半边，收缩右边界
                    right = mid - 1
                else: # 不在左半边，则只有肯能在右边，收缩左边界
                    left = mid + 1
            else: # 左边不是升序，则右半边一定是升序的
                if nums[mid] < target <= nums[right]: # 在右边
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1
# 时间复杂度O(logn),一次二分查找

