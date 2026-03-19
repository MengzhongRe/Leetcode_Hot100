
#
# @lc app=leetcode.cn id=153 lang=python
#
# [153] 寻找旋转排序数组中的最小值
#

# @lc code=start
# 我们通过一次二分查找(logn)去找数组旋转后的升序序列的最后一个值，例如[4,5,6,7,0,1,2],则7是数组旋转后的
# 升序序列的最后一个值
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        # 【边界与特例处理】
        # 如果数组只有一个元素，或者数组根本没有旋转（完全严格升序），
        # 那么首元素就是全局最小值，直接返回。
        if n == 1 or nums[0] < nums[n - 1]: 
            return nums[0]
        
        left, right = 0, n - 1
        
        # 【二分查找寻找“悬崖点”】
        while left <= right:
            mid = left + (right - left) // 2
            
            # 核心判断 1：定位“悬崖”（突变点）
            # 在一个由升序数组旋转得来的序列中，唯一会出现前一个数大于后一个数的地方，
            # 就是原数组首尾相接的那个“断层”。找到了断层，下一个元素就是最小值。
            if nums[mid] > nums[mid + 1]: 
                return nums[mid + 1]
                
            # 核心判断 2：二分区间收缩
            # 如果 mid 位置的值严格大于数组末尾的值，
            # 说明从 left 到 mid 这一段是正常的升序区间，“悬崖”必定在 mid 的右侧。
            elif nums[mid] > nums[n - 1]: 
                left = mid + 1
                
            # 否则，说明 mid 落在了旋转后的右半段升序区间，
            # 那么真正的最小值（悬崖底）一定在 mid 的左侧。
            else: 
                right = mid - 1
                
        return -1 # 理论上不会走到这里，仅作防守性返回
# 时间复杂度O(logn)，一次二分查找
# 空间复杂度O(1)
# @lc code=end

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left,right = 0,len(nums) - 1

        while left < right: # 不能写left == right，因为最后会进入right = mid,然后left == right进入死循环 
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]: # 如果该值大于右侧值，说明最小值在右侧（且不包含mid）
                left = mid + 1
            else: # 否则，在左侧，但是有可能包含mid
                right = mid
        # 循环结束最后left == right，就是最小值
        return nums[left]
# 时间复杂度O(logn)
# 空间复杂度O(1)