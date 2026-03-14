#
# @lc app=leetcode.cn id=79 lang=python
#
# [79] 单词搜索
#

# @lc code=start
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        n = len(board[0])
        l = len(word)

        def dfs(r,c,index):
            if index == l: # 如果index等于了单词的长度，说明之前的字符都匹配成功了，因此返回True
                return True
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != word[index]: # 该分支判断表示该格子的字符不匹配或者越界了，因此直接返回False
                return False
            
            tmp = board[r][c] # 先记录当前字符，之后回溯需要撤销
            # 直接在原数组上标记，防止创建新数组[m,n]导致空间复杂度过大
            board[r][c] = '#' # 将当前格子标记为访问过了，避免重复访问

            # 继续往四个方向进行DFS
            found = (dfs(r - 1,c,index + 1) or # 向上一格寻找下一个单词
                     dfs(r + 1,c,index + 1) or # 向下一
                     dfs(r,c - 1,index + 1) or # 左
                     dfs(r,c + 1,index + 1)) # 右
            board[r][c] = tmp # 回溯，撤销之前的标记

            return found
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(i,j,0): # 从每个格子开始进行DFS，如果找到了单词就返回True
                    return True
        
        return False # 如果所有格子都尝试过了还没有找到单词，返回False
# 时间复杂度O(m * n * 3^L)，L是单词长度，最坏情况下每个格子都要从最开始调用递归函数，每次递归函数至多3个方向会存活下来继续调用
# 空间复杂度O(L)，递归调用栈的深度最多为单词长度L
        
# @lc code=end

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        n = len(board[0])

        def dfs(r,c,index):
            if index == len(board):
                return True
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != word[index]:
                return False
            
            tmp = board[r][c]
            board[r][c] = '#'

            found = (dfs(r - 1,c,index + 1) or
                     dfs(r + 1,c,index + 1) or 
                     dfs(r,c - 1,index + 1) or
                     dfs(r,c + 1,index + 1))
            
            board[r][c] = tmp

            return found
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 0 and dfs(i,j,0):
                    return True
        
        return False