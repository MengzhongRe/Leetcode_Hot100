#
# @lc app=leetcode.cn id=994 lang=python
#
# [994] 腐烂的橘子
#

# @lc code=start

# 广度优先搜索：用双端队列记录每轮腐烂的橘子坐标
from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 边界判断:若网格为空则直接返回0
        if not grid or not grid[0]:
            return 0
        m,n = len(grid),len(grid[0]) # 获取行列数
        total_time = 0 # 初始化结果变量

        queue = deque() # 初始化双端队列
        for i in range(m):# 遍历网格
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i,j)) # 将最开始就腐烂的橘子坐标加入队列
        
        while queue: # 只要还有没有处理的刚腐烂的橘子
            current_len = len(queue) # 获取当前层的腐烂橘子数，确保每一轮只处理上一轮的腐烂橘子，这是实现分钟计数的关键
            has_rot = False # 记录当前层有无新橘子腐烂，防止因本层无新橘子腐烂而错误计数
            for _ in range(current_len): # 遍历当前轮次腐烂的橘子
                x,y = queue.popleft() # 取出当前轮次腐烂橘子的坐标
                for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]: # 遍历该橘子四个方向上的坐标
                    nx = x + dx
                    ny = y + dy
                    # 检查四个方向是否有边界内的新鲜橘子
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2 # 如果有则该橘子腐烂
                        queue.append((nx,ny)) # 同时把新一轮次腐烂的橘子加入到队列中，我们下一次轮次（分钟）再处理刚刚腐烂的橘子
                        if not has_rot: # 记录本轮次有无腐烂
                            has_rot = True
            if has_rot: # 仅当本轮次有新橘子腐烂时才计数
                total_time += 1
        
        for i in range(m): # 最后再遍历一遍网格，如果还有新橘子则返回-1，否则返回已计数结果
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        
        return total_time
# 时间复杂度O(mn)，需访问所有单元格三次
# 空间复杂度O(mn)，最坏情况下左右橘子均腐烂则一开始遍历完所有橘子坐标都会被加入到队列中     
# @lc code=end

from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        m,n = len(grid),len(grid[0])
        fresh_count = 0
        queue = deque()
        # 1.第一轮遍历：将一开始腐烂的橘子加入到队列第一层，并统计新橘子的数量
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh_count += 1
                if grid[i][j] == 2:
                    queue.append((i,j))
        # 剪枝策略：如果根本没有新橘子，则直接返回0，防止后续遍历队列损耗时间以及计数错误
        if fresh_count == 0:
            return 0
        
        total_time = 0
        # 剪枝：仅当队列中还有未处理的刚腐烂的橘子并且还有新橘子时才处理
        while queue and fresh_count > 0:
            current_len = len(queue) # 记录当前轮次的腐烂橘子数量，其实就是上一轮被感染的橘子数量，这是实现分钟计数的核心
            has_rot = False # 记录当前分钟（轮次）是否有新橘子腐烂
            for _ in range(current_len):
                x,y = queue.popleft() # 取出当前感染源
                for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh_count -= 1
                        queue.append((nx,ny))
                        if not has_rot:
                            has_rot = True
            if has_rot:
                total_time += 1
        
        return total_time if fresh_count == 0 else -1
# 时间复杂度O(mn),每个橘子最多入队一次出队一次
# 空间复杂度O(mn),全部都是腐烂橘子时，会在第一次遍历时入队           

            


        


