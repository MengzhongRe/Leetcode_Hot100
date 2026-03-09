# 经典BFS问题解题总结（岛屿数量 + 腐烂的橘子）
## 一、岛屿数量（numIslands）
### 1. 解题思路
核心是**通过BFS遍历连通区域**，将所有相连的陆地（'1'）标记为已访问（改为'0'），每启动一次BFS代表发现一个新岛屿，最终统计BFS的启动次数即为岛屿数量。
- 遍历网格的每个单元格；
- 遇到未访问的陆地（'1'）时，岛屿计数+1，并启动BFS；
- BFS中遍历当前陆地的上下左右四个方向，将相连的陆地标记为已访问，避免重复计数。

### 2. 优化过程
| 阶段 | 问题 | 优化方案 |
|------|------|----------|
| 基础版 | 相邻陆地未及时标记，导致重复入队、死循环 | 入队相邻陆地时立即标记为'0'，避免重复处理 |
| 效率优化 | 使用列表pop(0)实现队列，时间复杂度高 | 改用deque的popleft()，将出队操作从O(n)优化为O(1) |
| 空间优化 | 额外维护visited数组记录访问状态 | 直接修改原网格（标记为'0'），节省O(m×n)空间 |

### 3. 核心代码
```python
from collections import deque

class Solution(object):
    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        count = 0

        def bfs(i, j):
            queue = deque()
            queue.append((i, j))
            grid[i][j] = '0'  # 入队即标记，避免重复
            
            while queue:
                x, y = queue.popleft()
                # 遍历上下左右四个方向
                for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '1':
                        queue.append((nx, ny))
                        grid[nx][ny] = '0'  # 核心优化：及时标记

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    bfs(i, j)
        
        return count
```

### 4. 复杂度分析
- **时间复杂度**：O(m×n)。每个单元格仅被访问一次（标记为'0'后不再处理），m为行数，n为列数。
- **空间复杂度**：O(min(m,n))。BFS队列的最大长度由网格短边长度决定（全陆地网格的扩散层最大长度为短边），最坏情况为O(m×n)（保守上界）。

## 二、腐烂的橘子（orangesRotting）
### 1. 解题思路
核心是**分层BFS模拟时间扩散**，每一层BFS对应一分钟的腐烂过程，统计扩散的层数即为总时间；若最终仍有新鲜橘子未腐烂，返回-1。
- 初始化：收集所有初始腐烂橘子的坐标入队，统计新鲜橘子数量；
- 分层BFS：每一轮处理当前所有腐烂橘子，将其四周的新鲜橘子标记为腐烂并加入下一轮队列；
- 剪枝+结果判断：无新鲜橘子时直接返回0；最终根据新鲜橘子剩余数量判断返回时间或-1。

### 2. 优化过程
| 阶段 | 问题 | 优化方案 |
|------|------|----------|
| 基础版 | 时间多算1（初始腐烂橘子无扩散仍计数） | 新增has_rot标记，仅当本轮有橘子腐烂时计时 |
| 效率优化 | 最后遍历网格检查新鲜橘子，多一轮O(m×n)遍历 | 维护fresh_count计数器，直接通过计数器判断结果 |
| 逻辑精简 | has_rot标记冗余 | 利用while循环条件（fresh_count>0），每轮处理完直接计时，简化逻辑 |
| 边界优化 | 空网格/无新鲜橘子场景处理不及时 | 提前剪枝，直接返回0，避免无效BFS |

### 3. 核心代码
```python
from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        fresh_count = 0
        queue = deque()

        # 初始化：收集腐烂橘子+统计新鲜橘子
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh_count += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))
        
        # 剪枝：无新鲜橘子直接返回0
        if fresh_count == 0:
            return 0
        
        total_time = 0
        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        # 分层BFS：每一层对应一分钟
        while queue and fresh_count > 0:
            current_len = len(queue)
            for _ in range(current_len):
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh_count -= 1
                        queue.append((nx, ny))
            total_time += 1
        
        return total_time if fresh_count == 0 else -1
```

### 4. 复杂度分析
- **时间复杂度**：O(m×n)。初始化遍历网格（O(m×n)）+ BFS遍历所有单元格（O(m×n)），总复杂度为线性。
- **空间复杂度**：O(m×n)。最坏情况下（全是腐烂橘子），队列存储所有单元格坐标，无额外空间消耗。

## 三、通用总结
### 1. BFS核心模板（适用于网格类连通性问题）
```python
# 1. 初始化队列+边界判断
if not grid or not grid[0]:
    return 目标值
m, n = len(grid), len(grid[0])
queue = deque()

# 2. 预处理（收集初始节点/统计关键值）
for i in range(m):
    for j in range(n):
        预处理逻辑（如收集初始腐烂橘子、统计新鲜橘子）

# 3. 分层BFS核心
directions = [(-1,0),(1,0),(0,-1),(0,1)]  # 四方向遍历
while queue:
    current_len = len(queue)
    for _ in range(current_len):
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0 <= nx < m and 0 <= ny < n and 合法条件（如未访问/新鲜橘子）:
                标记/修改状态
                queue.append((nx, ny))
    时间/计数更新

# 4. 结果判断
return 最终结果
```

### 2. 关键优化点
1. **及时标记**：入队时立即标记节点状态，避免重复入队（核心避坑点）；
2. **分层处理**：通过current_len控制每轮处理的节点数，实现“按层遍历”（适配时间/步数统计）；
3. **剪枝策略**：提前处理边界场景（如无新鲜橘子、空网格），减少无效计算；
4. **空间复用**：直接修改原网格代替额外的visited数组，节省空间。

### 3. 复杂度共性
- 时间复杂度：均为O(m×n)，网格类BFS问题的理论下界（需遍历所有单元格）；
- 空间复杂度：均由队列存储量决定，岛屿问题为O(min(m,n))（精准上界），腐烂橘子为O(m×n)（最坏情况）。