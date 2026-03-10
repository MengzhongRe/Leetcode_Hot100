# 经典图论问题解题总结（岛屿数量 + 腐烂的橘子）
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

---

## 🏷️ 1. LeetCode 207: 课程表 (Medium)
> **面试本质考点**：有向图的成环检测、拓扑排序 (Kahn 算法 / BFS)、图的物理存储（邻接表）

### 💡 详细解题思路
这道题是解决所有“任务依赖”、“包解析”、“流水线调度”问题的祖师爷。
核心思想是将问题转化为**有向图**：课程是“节点”，先修关系是“有向边”（如 `A -> B` 代表学完 A 才能解锁 B）。“能不能学完”等价于“**图中有没有死循环（环）**”。

我们采用 **BFS（广度优先搜索）+ 入度表** 的经典拓扑排序算法：
1. **核心概念提取（入度）**：
   * **入度（In-degree）**：指向当前节点的边数。在物理意义上，代表**“这门课还有几门前置课没修完”**。入度为 0，代表门槛彻底解除，可以立刻上课。
2. **第一步：建立账本（建图与统计）**：
   * 用 `indegrees` 数组记录每个节点的入度。
   * 用 `adjacency`（哈希表套列表 `defaultdict(list)`）记录每个节点“学完后能解锁哪些后续节点”。
3. **第二步：寻找突破口（初始化队列）**：
   * 遍历入度数组，把所有一开始入度就为 0 的节点（毫无门槛的基础课）扔进 BFS 队列。
4. **第三步：层层剥洋葱（BFS 核心传播逻辑）**：
   * 从队列里弹出一门课（代表学完了），**已学课程总数 + 1**。
   * 顺藤摸瓜，找到这门课能解锁的所有后续课程，把它们的**入度统统减 1**。
   * **灵魂判断**：如果某门后续课减完 1 之后，入度刚好变成 0 了！说明它的所有前置条件都满足了，立刻把它也推进队列！
5. **第四步：结算验收**：
   * 如果图中有环，环里的节点入度永远减不到 0，永远进不了队列。
   * 最终对比：`已学课程总数 == 给定总课程数`。相等则无环，不等则有环。

### 💻 核心代码 (Python)
```python
from collections import deque, defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # 1. 初始化数据结构
        indegrees = [0] * numCourses              # 记录每门课的入度（门槛数）
        adjacency = defaultdict(list)             # 邻接表：记录 学完先修课 -> 能解锁的后续课
        
        # 2. 填充入度表和邻接表
        for cur, pre in prerequisites:
            indegrees[cur] += 1                   # 目标课 cur 的前置门槛 + 1
            adjacency[pre].append(cur)            # 记录 pre 学完后能解锁 cur
            
        # 3. 把所有入度为 0 的节点（突破口）放入队列
        # 队列中存放的永远是“当前可以直接上的课”
        queue = deque([i for i in range(numCourses) if indegrees[i] == 0])
        
        learned_count = 0 # 记录成功修完的课程总数
        
        # 4. 开始 BFS 拓扑排序
        while queue:
            # 学完一门课
            pre = queue.popleft()
            learned_count += 1
            
            # 消除这门课的后续影响（给后续课程降门槛）
            for cur in adjacency[pre]:
                indegrees[cur] -= 1               # 后续课程的前置条件 - 1
                if indegrees[cur] == 0:           # 门槛清零！可以上这门课了！
                    queue.append(cur)
                    
        # 5. 判断有没有因为“死锁(环)”导致漏上的课
        return learned_count == numCourses
```

### ⏱️ 详细复杂度分析
* **时间复杂度**：$\mathcal{O}(V + E)$。$V$ 是课程数（节点），$E$ 是先修关系数（边）。
  * 初始化入度表和邻接表需要遍历所有边，耗时 $O(E)$。
  * 寻找入度为 0 的节点需要遍历所有节点，耗时 $O(V)$。
  * BFS 过程中，每个节点最多入队出队一次 $O(V)$，每条边（每个先修关系）最多被顺藤摸瓜访问一次 $O(E)$。
  * 故总时间为 $O(V + E)$。
* **空间复杂度**：$\mathcal{O}(V + E)$。
  * 邻接表 `adjacency` 按需存储了所有的节点和边，严格占用 $O(V + E)$。
  * 入度数组 `indegrees` 占用 $O(V)$。
  * 队列 `queue` 最坏情况下（所有课都没先修要求）会同时存放所有节点，占用 $O(V)$。

---

## 🏷️ 2. LeetCode 208: 实现 Trie (前缀树) (Medium)
> **面试本质考点**：面向对象设计、树形结构变种、空间换时间思想、大模型分词器（Tokenization）底层映射

### 💡 详细解题思路
前缀树（Trie，字典树）的核心奥义是**“按字符拆分路径，共享公共前缀”**。
在普通哈希表中，`"app"` 和 `"apple"` 是两个毫无关联的独立字符串，而在前缀树中，它们共享了前 3 个字符节点的内存空间。

1. **节点设计 (TrieNode)**：
   * 每一个节点本身不直接存字符，而是存一个**哈希表 `children`**（键是字符，值是连向的下一个节点）。
   * 必须有一个**布尔值 `is_end`**。因为 `"app"` 和 `"apple"` 路径重叠，当我们走到第二个 `p` 时，必须靠 `is_end == True` 才能知道 `"app"` 曾作为一个完整的单词被插入过，而不仅仅是 `"apple"` 的垫脚石。
2. **插入单词 (insert)**：
   * 从根节点出发，遍历单词的每个字符。如果字符不在当前节点的 `children` 字典中，就原地新建一个 `TrieNode`。
   * 一路往下走，遍历完最后一个字符后，在停下来的那个节点打上 `is_end = True` 的“完结钢印”。
3. **查找单词 (search)**：
   * 顺藤摸瓜往下走。如果中途某个字符对应的路断了（不在 `children` 里），直接返回 `False`。
   * 如果顺利走完了全长，**必须检查最后停下的节点的 `is_end`**。如果是 `True`，说明不仅有这个前缀，而且它是个完整单词。
4. **查找前缀 (startsWith)**：
   * 逻辑和 `search` 完全一样，唯一的区别是：只要没断路、能顺利走完传入的前缀字符串，**不用管 `is_end` 是什么**，直接返回 `True`！

### 💻 核心代码 (Python)
```python
class TrieNode:
    def __init__(self):
        # children: 记录当前节点连向的所有子节点。字符 -> TrieNode
        self.children = {}    
        # is_end: 标记是否在此节点结束了一个完整的单词
        self.is_end = False   

class Trie:
    def __init__(self):
        # 树的根节点，一个空壳，所有单词都从这里出发
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            # 遇到没有踩过的路，就铺砖（新建节点）
            if char not in node.children:
                node.children[char] = TrieNode()
            # 顺着路径往下走
            node = node.children[char]
        # 单词查完了，在最后一个节点盖上"单词完结"的钢印
        node.is_end = True    

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            # 走到半路发现路断了，说明树里压根没这个词
            if char not in node.children:
                return False
            node = node.children[char]
        # 路走通了，但必须验证这是一个“完整单词”还是一半的“前缀”
        return node.is_end    

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        # 只要路没断，能把 prefix 走完，就说明一定有以它开头的词！
        return True           
```

### ⏱️ 详细复杂度分析
* **时间复杂度**：**全部操作均为 $\mathcal{O}(L)$**。（$L$ 为操作的字符串长度）。
  * 极其震撼的性能！无论你的前缀树里存了十个词还是一百万个词，你想查 `"apple"` 在不在，永远只需要执行 5 次哈希表查找。**查询时间与词库的总大小 $N$ 绝对无关**，彻底碾压了需要遍历的传统数据结构。
* **空间复杂度**：最坏情况 $\mathcal{O}(N \times L)$。
  * $N$ 是插入的单词数量，$L$ 是平均长度。
  * 最坏情况：所有的单词都没有任何公共前缀（比如 `a`, `b`, `c`），那么每个字符都要开辟一个新节点。
  * 真实场景（最佳情况）：大量单词共享前缀（如 `auto`, `automatic`），空间会被极限压缩，远小于把所有字符串直接存进哈希表所需的内存。