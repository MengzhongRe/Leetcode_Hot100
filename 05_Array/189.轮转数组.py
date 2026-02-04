#
# @lc app=leetcode.cn id=189 lang=python
#
# [189] 轮转数组
#

# @lc code=start
# 三次反转方法:数组向右旋转 k 位，等价于将数组末尾的 k 个元素移动到开头。我们可以通过三次反转实现：
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n # 当 k > n 时，例如k = 10,n = 7,本质上等于k为3 

        def reverse(left,right):
            while left < right:
                nums[left],nums[right] = nums[right],nums[left]
                right -= 1
                left += 1
        
        reverse(0,n-1) # O(N):1.反转整个数组：将末尾的 k 个元素整体移到数组最前面，但顺序是反的。
        reverse(0,k-1) # O(k):2.反转前 k 个元素：把这 k 个元素的顺序恢复正常。
        reverse(k,n-1) # O(n-k):3.反转后 n-k 个元素：把剩下的元素顺序也恢复正常。

# 时间复杂度O(N)
# 空间复杂度O(1) 原地修改
# @lc code=end

# 辅助数组方法
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n # 当 k > n 时，例如k = 10,n = 7,本质上等于k为3
        copyed_nums = [0] * n # 创建辅助数组
        # O(N)
        for i in range(n):
            copyed_nums[(i + k) % n] = nums[i]
        nums[:] = copyed_nums # python修改列表必须用切片赋值