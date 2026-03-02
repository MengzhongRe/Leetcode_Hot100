# 🌲 二叉树算法精讲 (Binary Tree Mastery)

## 📌 目录
1.  **[94] 二叉树的中序遍历** —— 栈模拟递归的经典
2.  **[104] 二叉树的最大深度** —— 分治法与层序遍历
3.  **[226] 翻转二叉树** —— Google 面试名题

---

## ⚔️ 1. [94] 二叉树的中序遍历 (Binary Tree Inorder Traversal)

> **核心奥义**：
> 中序顺序：**左 -> 根 -> 右**。
> 递归依靠系统栈，迭代依靠手动栈（Stack）。

### 💡 方法一：递归法 (Recursive)
最直观的写法。利用函数调用栈自动回溯。
```python
class Solution(object):
    def inorderTraversal(self, root):
        res = []
        def dfs(node):
            if not node: return
            dfs(node.left)       # 1. 尽头走到左
            res.append(node.val) # 2. 访问中间
            dfs(node.right)      # 3. 再去右边
        dfs(root)
        return res
```

### 💡 方法二：迭代法 (Iterative) —— **面试重点**
**思路**：模拟系统栈。
1.  **一路向左**：把所有左子节点压入栈，直到撞墙（None）。
2.  **弹栈访问**：弹出栈顶（最左下的节点），加入结果。
3.  **转向右边**：指针指向右孩子，重复上述过程。

```python
class Solution(object):
    def inorderTraversal(self, root):
        res, stack = [], []
        curr = root
        
        while curr or stack:
            # 1. 一路向左冲到底，沿途入栈
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # 2. 弹出栈顶并访问
            node = stack.pop()
            res.append(node.val)
            
            # 3. 转向右子树
            curr = node.right
            
        return res
```

### 📊 复杂度分析
| 维度 | 复杂度 | 说明 |
| :--- | :--- | :--- |
| **时间** | $O(N)$ | 每个节点进栈一次，出栈一次。 |
| **空间** | $O(H)$ | $H$ 为树高。平均 $O(\log N)$，最坏（链表）$O(N)$。 |

---

## ⚔️ 2. [104] 二叉树的最大深度 (Maximum Depth of Binary Tree)

> **核心奥义**：
> **分治法**：我的深度 = 1 + Max(左深度, 右深度)。
> **层序遍历**：像剥洋葱一样，剥了一层计数器 +1。

### 💡 方法一：递归法 (DFS) —— **推荐**
代码最短，逻辑最清晰。
```python
class Solution(object):
    def maxDepth(self, root):
        # 终止条件
        if not root: 
            return 0
        
        # 分治：左边深度 vs 右边深度
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        # 当前深度 = 1 + 子树最大深度
        return 1 + max(left_depth, right_depth)
```

### 💡 方法二：迭代法 (BFS / 层序遍历)
使用 `deque` 队列，一层一层遍历。
```python
from collections import deque
class Solution(object):
    def maxDepth(self, root):
        if not root: return 0
        
        queue = deque([root])
        depth = 0
        
        while queue:
            # 记录当前层的节点数（定格）
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            # 遍历完一层，深度+1
            depth += 1
            
        return depth
```

### 📊 复杂度分析
| 维度 | 复杂度 | 说明 |
| :--- | :--- | :--- |
| **时间** | $O(N)$ | 遍历所有节点。 |
| **空间** | $O(N)$ | 递归栈深度 $O(H)$；BFS 队列最大宽度可能达到 $O(N)$。 |

---

## ⚔️ 3. [226] 翻转二叉树 (Invert Binary Tree)

> **核心奥义**：
> 只要遍历到每个节点，把它的 **左孩子** 和 **右孩子** 交换一下即可。
> 递归是 DFS 思路，迭代通常用 BFS 思路。

### 💡 方法一：递归法 (DFS) —— **推荐**
先序遍历：交换左右 -> 递归左 -> 递归右。
```python
class Solution(object):
    def invertTree(self, root):
        if not root:
            return None
        
        # 1. 核心操作：交换左右子树
        root.left, root.right = root.right, root.left
        
        # 2. 递归处理子节点
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
```

### 💡 方法二：迭代法 (BFS / 层序遍历)
利用队列，见到一个节点，就交换它的左右孩子，然后把孩子入队。
```python
from collections import deque
class Solution(object):
    def invertTree(self, root):
        if not root: return None
        
        queue = deque([root])
        while queue:
            node = queue.popleft()
            
            # 1. 交换（哪怕孩子是 None 也能交换）
            node.left, node.right = node.right, node.left
            
            # 2. 只有存在的孩子才入队（不要把 None 放进队列）
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
            
        return root
```

### 📊 复杂度分析
| 维度 | 复杂度 | 说明 |
| :--- | :--- | :--- |
| **时间** | $O(N)$ | 每个节点都需要被交换一次。 |
| **空间** | $O(N)$ | 最坏情况下（满二叉树），队列需要存储最底层节点 $N/2$ 个。 |

---

## 🏆 总结心得

1.  **递归 vs 迭代**：
    *   **递归**胜在代码简洁，逻辑符合人类直觉（分治）。
    *   **迭代**胜在稳健，不会因为树太深而爆栈（Stack Overflow），是工程实现的常用手段。
2.  **栈 vs 队列**：
    *   **DFS**（深度优先，如中序遍历）通常用 **栈 (Stack/List)**。
    *   **BFS**（广度优先，如层序遍历）必须用 **双端队列 (Deque)**。
3.  **None 的处理**：
    *   在 BFS 队列中，通常**不建议**把 `None` 放进去，取出时再判断很麻烦。建议在入队前检查 `if node.left:`。

# 力扣二叉树经典题目解题总结
> 总结题目：101.对称二叉树、543.二叉树的直径、102.二叉树的层序遍历  
> 核心考点：二叉树的遍历（DFS/BFS）、递归/迭代实现、复杂度分析  

## 目录
- [101. 对称二叉树](#101-对称二叉树)
- [543. 二叉树的直径](#543-二叉树的直径)
- [102. 二叉树的层序遍历](#102-二叉树的层序遍历)
- [核心知识点总结](#核心知识点总结)

---

## 101. 对称二叉树
### 题目描述
判断一棵二叉树是否是对称的（左右子树互为镜像）。

### 解题思路
#### 核心逻辑
对称二叉树的本质是：
1. 根节点的左右子节点值相等；
2. 左子树的左节点 = 右子树的右节点；
3. 左子树的右节点 = 右子树的左节点。

#### 实现方式
- **递归（DFS）**：通过辅助函数验证两个节点是否互为镜像，递归终止条件为节点为空/值不相等。
- **迭代（BFS/DFS）**：队列实现BFS（逐层验证）、栈实现DFS（模拟递归）。

### 核心代码
#### 1. 递归解法（推荐）
```python
from typing import Optional

# 二叉树节点定义
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def is_mirror(node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
            # 终止条件1：两个节点都为空
            if not node1 and not node2:
                return True
            # 终止条件2：仅一个节点为空
            if not node1 or not node2:
                return False
            # 递归条件：值相等 + 左左=右右 + 左右=右左
            return (node1.val == node2.val and
                    is_mirror(node1.left, node2.right) and
                    is_mirror(node1.right, node2.left))
        
        if not root:
            return True
        return is_mirror(root.left, root.right)
```

#### 2. 迭代解法（队列/BFS）
```python
from collections import deque
from typing import Optional

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        queue = deque([root.left, root.right])
        while queue:
            node1 = queue.popleft()
            node2 = queue.popleft()
            
            if not node1 and not node2:
                continue
            if not node1 or not node2 or node1.val != node2.val:
                return False
            
            # 按镜像顺序入队
            queue.append(node1.left)
            queue.append(node2.right)
            queue.append(node1.right)
            queue.append(node2.left)
        
        return True
```

### 复杂度分析
| 解法       | 时间复杂度 | 空间复杂度（最坏） | 空间复杂度（平均） |
|------------|------------|--------------------|--------------------|
| 递归       | O(n)       | O(n)               | O(log n)           |
| 迭代（队列）| O(n)       | O(n)               | O(n)               |
| 迭代（栈） | O(n)       | O(n)               | O(log n)           |

### 优化过程
1. 初始思路：仅验证根节点左右子节点相等 → 错误（未考虑深层节点）；
2. 优化方向：递归验证镜像关系，覆盖所有层级；
3. 进阶优化：迭代解法避免递归栈溢出，队列实现BFS更符合“层序验证”直觉。

---

## 543. 二叉树的直径
### 题目描述
给定一棵二叉树，计算其直径长度（任意两节点路径长度的最大值，路径长度为边数）。

### 解题思路
#### 核心逻辑
二叉树的直径 = 所有节点的「左子树深度 + 右子树深度」的最大值（路径不一定经过根节点）。

#### 实现方式
后序遍历（DFS）：递归计算每个节点的左右子树深度，同时记录遍历过程中最大的深度和。

### 核心代码
```python
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = [0]  # 用列表存储可变值（嵌套函数可修改）
        
        def depth(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            # 后序遍历：先算左右子树深度
            left_depth = depth(node.left)
            right_depth = depth(node.right)
            
            # 更新最大直径
            max_diameter[0] = max(max_diameter[0], left_depth + right_depth)
            
            # 返回当前节点深度
            return max(left_depth, right_depth) + 1
        
        depth(root)
        return max_diameter[0]
```

### 复杂度分析
| 解法   | 时间复杂度 | 空间复杂度（最坏） | 空间复杂度（平均） |
|--------|------------|--------------------|--------------------|
| 递归   | O(n)       | O(n)               | O(log n)           |

### 优化过程
1. 初始思路：仅计算根节点的左右深度和 → 错误（直径可能不经过根节点）；
2. 优化方向：遍历所有节点，记录每个节点的左右深度和的最大值；
3. 细节优化：用列表存储最大值（避免嵌套函数无法修改外层普通变量）。

---

## 102. 二叉树的层序遍历
### 题目描述
按层级从上到下、从左到右遍历二叉树，返回每一层的节点值列表。

### 解题思路
#### 核心逻辑
层序遍历 = 广度优先搜索（BFS）：用队列逐层处理节点，通过`level_size = len(queue)`确定当前层节点数。

#### 实现方式
- **迭代（队列/BFS）**：标准解法，效率高；
- **递归（DFS）**：模拟层序逻辑（拓展理解）。

### 核心代码
#### 1. 迭代解法（推荐）
```python
from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)  # 关键：确定当前层节点数
            current_level = []
            
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                
                # 子节点入队（下一层）
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            res.append(current_level)
        
        return res
```

#### 2. 递归解法（拓展）
```python
from typing import Optional, List

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        
        def dfs(node: Optional[TreeNode], level: int):
            if not node:
                return
            # 初始化当前层列表
            if len(res) == level:
                res.append([])
            res[level].append(node.val)
            # 递归处理子节点
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        
        dfs(root, 0)
        return res
```

### 复杂度分析
| 解法       | 时间复杂度 | 空间复杂度（最坏） | 空间复杂度（平均） |
|------------|------------|--------------------|--------------------|
| 迭代（队列）| O(n)       | O(n)               | O(n)               |
| 递归       | O(n)       | O(n)               | O(log n)           |

### 优化过程
1. 初始思路：用普通列表模拟队列 → 效率低（`pop(0)`为O(n)）；
2. 优化方向：改用`deque`（双端队列），`popleft()`为O(1)；
3. 细节优化：通过`level_size`精准划分层级，避免混层。

---

## 核心知识点总结
### 1. 遍历方式
| 遍历类型 | 实现方式       | 核心数据结构 | 适用场景               |
|----------|----------------|--------------|------------------------|
| DFS（深度优先） | 递归/栈       | 栈（递归栈/手动栈） | 对称验证、直径计算     |
| BFS（广度优先） | 迭代（队列）   | 队列         | 层序遍历、逐层验证     |

### 2. 关键技巧
1. 对称二叉树：验证「左左=右右、左右=右左」；
2. 二叉树直径：后序遍历记录「左深度+右深度」的最大值；
3. 层序遍历：`level_size = len(queue)` 划分层级，`deque` 提升效率。

### 3. 复杂度规律
- 时间复杂度：所有解法均为O(n)（每个节点仅访问一次）；
- 空间复杂度：递归/栈依赖树的高度（O(log n)~O(n)），队列依赖节点数（O(n)）。

### 4. 优化原则
1. 优先使用迭代（队列）实现层序遍历，递归仅作拓展；
2. 避免递归栈溢出：深度大的树优先用迭代解法；
3. 数据结构选择：队列用`deque`，避免普通列表的低效操作。