#
# @lc app=leetcode.cn id=240 lang=python
#
# [240] 搜索二维矩阵 II
#

# @lc code=start
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
        
        rows = len(matrix)
        cols = len(matrix[0])
        # 从右上角元素开始搜索比较  
        row = 0
        col = cols - 1
        # 整个过程中row 只会向下收缩，col只会向左收缩，因此有如下边界判断
        while row < rows and col >= 0:
            current = matrix[row][col] # 获取当前值
            if current == target: # 若当前值==目标值，则直接返回True
                return True
            elif current < target: # 若当前值小于目标值，则说明目标值一定再下面的行
                row += 1
            else: # 若当前值大于目标值，则说明目标值一定在改列左侧的列（因为从上到下列的值是增大的，该元素是最上面的列，下面的元素只会更大）
                col -= 1
        
        return False
# 时间复杂度O(m+n),最多遍历到左下角，也就是最多走m + n步
# 空间复杂度O(1)
# @lc code=end

