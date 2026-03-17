#
# @lc app=leetcode.cn id=74 lang=python
#
# [74] 搜索二维矩阵
#

# @lc code=start

# 将二位数组[m,n]换为虚拟一维数组[m*n]，用二分查找，mid 坐标需要被映射回二维坐标（row,col）
# 关键是我们需要建立一维数组索引到二维矩阵坐标之间的映射关系
# 给定虚拟一维数组索引index,其对应的二维矩阵坐标为
# row = index // n 即索引对列数的商即为其行号
# col = index % n 即索引对列数的模即为其列号
# 这样我们不需要真的将二维数组展平就可以实现对其的二分查找
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # 边界判断
        if not matrix or not matrix[0]:
            return False
        m,n = len(matrix),len(matrix[0])
        # 初始化虚拟一维数组的左右指针
        left,right = 0,m * n -1
        # 不能写作left < right,否则在left == right时，会漏掉最后一个元素的判断
        # 如果最后一个元素就是目标值，会错误返回False
        while left <= right:
            # 防止数值溢出
            mid = left + (right - left) // 2
            row = mid // n # 计算行号
            col = mid % n # 计算列号
            mid_val = matrix[row][col]
            if mid_val == target:
                return True
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1
        # 循环结束都没有返回值，说明没有目标值
        return False
# 时间复杂度O(logmn)
# 空间复杂度O(1)      
# @lc code=end

