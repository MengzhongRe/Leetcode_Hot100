#
# @lc app=leetcode.cn id=4 lang=python
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            nums1,nums2 = nums2,nums1

        m,n = len(nums1),len(nums2)
        # 由于我们的指标i不是数组的索引，而是我们的切割线（右半部份的第一个）
        # 如果right = m - 1,则i取不到m,即我们排除了把nums1数组的所有元素都划分到左半部份的可能性
        left,right = 0,m
        while left <= right:
            # 中点，二分查找
            i = left + (right - left) // 2
            # 因为是找中位数，所以需要满足左部份数量 = 右，即i + j = (m + n + 1) // 2
            j = (m + n + 1) // 2 - i 
            # 先处理切割后nums1和nums2的左半部份的最大值和右半部份的最小值
            nums1_left_max = float('-inf') if i == 0 else nums1[i - 1]
            nums2_left_max = float('-inf') if j == 0 else nums2[j - 1]

            nums1_right_min = float('inf') if i == m else nums1[i]
            nums2_right_min = float('inf') if j == n else nums2[j]
            # 如果满足以下条件则说明左边的所有值都小于等于右侧的所有值，符合中位数的要求
            if nums1_left_max <= nums2_right_min and nums2_left_max <= nums1_right_min:
                # 根据m + n的奇偶性来判断
                # 偶数，则中位数就是(Lmax + Rmin) / 2.0
                if (m + n) % 2 == 0:
                    return (max(nums1_left_max,nums2_left_max) + min(nums1_right_min,nums2_right_min)) / 2.0
                else: # 奇数，则中位数就是Lmax
                    return max(nums1_left_max,nums2_left_max)
            elif nums1_left_max > nums2_right_min: # 说明nums1向右切太多了，右指针需要向左收缩
                right = i - 1
            else: # 否则就说明向右收缩
                left = i + 1
# 时间复杂度O(logmin(m,n))，我们是在小数组上切割的
# 空间复杂度O(1)，常数个空间
# @lc code=end

