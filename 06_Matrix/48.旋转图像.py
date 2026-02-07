#
# @lc app=leetcode.cn id=48 lang=python
#
# [48] 旋转图像
#

# @lc code=start
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # 1.先转置矩阵，只遍历矩阵上三角区域（j > i）,避免元素被重复交换导致无效
        for i in range(n): # O(n**2)
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        # 2.再把每行反转，这里直接用Python内置函数reverse()
        for i in range(n): # O(n**2)
            matrix[i].reverse()

# 时间复杂度O(n**2)
# 空间复杂度O(1)      
# @lc code=end

