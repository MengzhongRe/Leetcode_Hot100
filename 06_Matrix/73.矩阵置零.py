#
# @lc app=leetcode.cn id=73 lang=python
#
# [73] 矩阵置零
#

# @lc code=start
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        row0 = False # 用于标记首行是否有0
        col0 = False # 用于标记首列是否有0
        # 遍历首行看看有没有0
        for j in range(n): #O(n)
            if matrix[0][j] == 0:
                row0 = True
                break
        # 遍历首列看看是否存在0
        for i in range(m): # O(m)
            if matrix[i][0] == 0:
                col0 = True
                break
        # 遍历矩阵所有元素(i,j) 看看是否为0
        # 若为0，则将相应的行首和列首都标记为0
        for i in range(1,m): # O(mn)
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        # 再遍历矩阵所有元素，只要该元素所在的行首标记为0，或所在列首标记为0，则表明该位置（i,j）需重置为0
        for i in range(1,m): # O(mn)
            for j in range(1,n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        # 检查row0是否为True,若是则需要将首行都重置为0
        if row0: # O(n)
            for j in range(n):
                matrix[0][j] = 0
        # 检查col0是否为True,若是则需要将首列都重置为0
        if col0: # O(m)
            for i in range(m):
                matrix[i][0] = 0
# 时间复杂度O(mn)
# 空间复杂度O(1)

# @lc code=end
# 暴力破解法，直接将为0的(i,j)元祖加入到标记当中，然后第二次遍历将相应的行与列重置为0
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        flags = []

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    flags.append((i,j))
        
        for i,j in flags:
            # 先改变所在行为0
            for k in range(n):
                matrix[i][k] = 0
             # 再改变所在列为0
            for k in range(m):
                matrix[k][j] = 0
# 时间复杂度O(mn)
# 最坏空间复杂度O(mn)        

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        rows = set()
        cols = set()

        # 第一次遍历若整个矩阵matrix[i][j] == 0,则说明第i行，第j列需要为0，则把i,j分别加入到相应的rows和cols当中
        for i in range(m):
            for j in range(n): # O(mn)
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        
        # 第二次遍历矩阵(i,j)只要i或j在相应的标记中，就把该元素置0
        for i in range(m):
            for j in range(n): # O(mn)
                if i in rows or j in cols:
                    matrix[i][j] = 0
# 时间复杂度O(mn)
# 空间复杂度O(m + n)   