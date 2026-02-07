#
# @lc app=leetcode.cn id=54 lang=python
#
# [54] 螺旋矩阵
#
# 用四个边界循环遍历矩阵
# 先从左到右遍历上边界，再从上到下遍历右边界，再从右到左遍历下边界，再从下到上遍历左边界
# @lc code=start
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # 边界判断
        if not matrix or not matrix[0]:
            return []
        # 上边界初始化为第0行
        top = 0
        bottom = len(matrix) - 1 # 下边界初始化为矩阵最后一行
        left = 0 # 左边界初始化为第一列
        right = len(matrix[0]) - 1 # 右边界初始化为最后一列
        res = []

        while top <= bottom and left <= right:
            # 1.先从左到右遍历上边界
            for col in range(left,right + 1): 
                res.append(matrix[top][col])
            top += 1 # 遍历结束后上边界向下收缩
            # 2.从上到下遍历右边界
            if top > bottom: # 判断是否越界
                break
            for row in range(top,bottom + 1):
                res.append(matrix[row][right])
            right -= 1 # 遍历后右边界向左收缩
            # 3.从右到左遍历下边界
            if left > right:
                break
            for col in range(right,left - 1,-1):
                res.append(matrix[bottom][col])
            bottom -= 1 # 遍历后下边界向上收缩
            # 4.最后从下到上遍历左边界
            if top > bottom:
                break
            for row in range(bottom,top - 1,-1):
                res.append(matrix[row][left])
            left += 1 # 遍历完后左边界向右收缩
        
        return res
# 时间复杂度O(mn),所有元素仅遍历一次
# 空间复杂度O(1),除返回数组没有额外空间    
# @lc code=end

