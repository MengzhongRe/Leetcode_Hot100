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

# 二叉搜索树（BST）经典题目解题总结
> 核心考点：BST特性（中序升序、左小右大）、递归/迭代遍历、平衡树构建、高效查询优化  

## 目录
- [108. 将有序数组转换为二叉搜索树](#108-将有序数组转换为二叉搜索树)
- [98. 验证二叉搜索树](#98-验证二叉搜索树)
- [230. 二叉搜索树中第k小的元素](#230-二叉搜索树中第k小的元素)
- [核心知识点总结](#核心知识点总结)

---

## 108. 将有序数组转换为二叉搜索树
### 题目描述
将升序数组转换为**高度平衡**的二叉搜索树（BST），平衡定义：左右子树高度差≤1。

### 解题思路
#### 核心逻辑
1. BST特性：中序遍历为升序数组 → 数组中点作为根节点，左半区为左子树，右半区为右子树；
2. 平衡要求：选中点作为根，保证左右子树节点数尽可能均衡，避免退化为链表；
3. 分治思想：递归处理左右子数组，构建子树。

#### 实现步骤
1. 找当前数组中点 `mid`，作为当前子树根节点；
2. 递归构建左子树（`[left, mid-1]`）和右子树（`[mid+1, right]`）；
3. 终止条件：`left > right`（子数组为空）。

### 核心代码（最优解）
```python
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build(left: int, right: int) -> Optional[TreeNode]:
            # 终止条件：区间无效
            if left > right:
                return None
            # 选中点作为根（偏左/偏右均可，保证平衡）
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            # 递归构建左右子树
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            return root
        
        return build(0, len(nums) - 1)
```

### 优化过程
| 优化阶段 | 初始思路 | 优化点 |
|----------|----------|--------|
| 1. 基础版 | 数组切片（`nums[:mid]`）构建子树 | 切片生成新数组，空间O(n) → 改用`left/right`指针，仅操作索引，空间O(1) |
| 2. 平衡版 | 选最左/最右元素为根 | 选中点为根，保证树平衡，时间/空间更优 |

### 复杂度分析
- **时间复杂度**：O(n)（每个节点仅创建一次）；
- **空间复杂度**：O(logn)（递归栈深度，平衡树高度=logn）。

---

## 98. 验证二叉搜索树
### 题目描述
验证一棵二叉树是否为有效的BST（左子树所有节点<根，右子树所有节点>根，且左右子树也为BST）。

### 解题思路
#### 核心逻辑
1. 错误思路：仅验证当前节点与直接子节点的大小关系（漏检深层节点）；
2. 正确思路：递归传递**上下界**，限制每个节点的合法值范围：
   - 根节点范围：(-∞, +∞)；
   - 左子节点范围：(父节点下界, 父节点值)；
   - 右子节点范围：(父节点值, 父节点上界)。

#### 实现步骤
1. 初始化上下界为负无穷、正无穷；
2. 递归检查节点值是否在合法范围；
3. 递归验证左/右子树，更新对应上下界；
4. 终止条件：空节点（合法）或节点值越界（非法）。

### 核心代码（最优解）
```python
from typing import Optional

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(node: Optional[TreeNode], lower: float, upper: float) -> bool:
            if not node:
                return True
            # 节点值越界，直接非法
            if node.val <= lower or node.val >= upper:
                return False
            # 递归验证左右子树，更新上下界
            return isValid(node.left, lower, node.val) and isValid(node.right, node.val, upper)
        
        return isValid(root, float('-inf'), float('inf'))
```

### 优化过程
| 优化阶段 | 初始思路 | 优化点 |
|----------|----------|--------|
| 1. 错误版 | 仅验证当前节点与直接子节点 | 增加上下界，覆盖所有子树节点的范围限制 |
| 2. 进阶版 | 递归上下界 | 补充中序遍历解法（BST中序升序），迭代实现避免栈溢出 |

#### 拓展：中序遍历验证（辅助解法）
```python
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = float('-inf')
        def inorder(node):
            if not node:
                return True
            if not inorder(node.left):
                return False
            if node.val <= self.prev:
                return False
            self.prev = node.val
            return inorder(node.right)
        return inorder(root)
```

### 复杂度分析
- **时间复杂度**：O(n)（每个节点仅访问一次）；
- **空间复杂度**：O(h)（h为树高，平衡树O(logn)，链表O(n)）。

---

## 230. 二叉搜索树中第k小的元素
### 题目描述
找到BST中第k小的元素（k从1开始）。

### 解题思路
#### 核心逻辑
1. BST特性：中序遍历（左→根→右）为升序序列 → 第k小元素是中序遍历的第k个节点；
2. 优化方向：找到目标后立即终止遍历，避免无效操作。

#### 实现步骤
1. 迭代模拟中序遍历（栈），先遍历左子树最深处；
2. 弹出节点时计数，计数等于k时直接返回；
3. 未找到则遍历右子树，重复步骤1-2。

### 核心代码（最优解：迭代中序遍历）
```python
from typing import Optional

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        current = root
        count = 0
        
        while stack or current:
            # 遍历左子树最深处
            while current:
                stack.append(current)
                current = current.left
            # 处理当前节点
            current = stack.pop()
            count += 1
            if count == k:
                return current.val  # 找到后立即返回，提前终止
            # 遍历右子树
            current = current.right
        
        return -1  # 题目保证k有效，仅兜底
```

### 优化过程
| 优化阶段 | 初始思路 | 优化点 |
|----------|----------|--------|
| 1. 递归版 | 存储所有中序结果，取第k-1个 | 空间O(n) → 改为计数+提前终止，空间O(h) |
| 2. 递归计数版 | 计数到k后未终止递归 | 增加`found`标志位，逐层终止递归，减少无效遍历 |
| 3. 迭代版 | 递归可能栈溢出 | 栈模拟中序，无栈溢出风险，直接return终止整个流程 |

#### 拓展：进阶优化（频繁修改+查询）
给节点增加`size`属性（子树节点数），查询时通过数值计算定位，时间复杂度O(h)：
```python
def kth_smallest_with_size(node, k):
    left_size = node.left.size if node.left else 0
    if left_size >= k:
        return kth_smallest_with_size(node.left, k)
    elif left_size + 1 == k:
        return node.val
    else:
        return kth_smallest_with_size(node.right, k - (left_size + 1))
```

### 复杂度分析
| 解法 | 时间复杂度 | 空间复杂度 |
|------|------------|------------|
| 迭代中序（最优） | O(h + k) | O(h) |
| 递归计数版 | O(h + k) | O(h) |
| 存储所有中序结果 | O(n) | O(n) |
| 带size属性版 | O(h) | O(h) |

---

## 核心知识点总结
### 1. BST核心特性
- 中序遍历结果为升序数组；
- 任意节点的左子树所有节点<当前节点<右子树所有节点；
- 平衡BST（如AVL）保证操作复杂度稳定在O(logn)。

### 2. 高频解题技巧
| 题目 | 核心技巧 |
|------|----------|
| 108 | 分治选中点构建平衡BST，用指针替代数组切片 |
| 98 | 递归传递上下界，或中序遍历验证升序 |
| 230 | 迭代中序遍历提前终止，进阶用size属性高效查询 |

### 3. 复杂度规律
- 时间：所有解法均为O(n)（每个节点仅访问一次）；
- 空间：递归依赖树高O(h)，迭代栈/队列依赖树高O(h)，存储所有结果依赖O(n)。

### 4. 优化原则
- 优先用迭代法（栈/队列），避免递归栈溢出；
- 找到目标后立即终止遍历，减少无效操作；
- 高频修改场景，用size属性或平衡树（AVL/红黑树）优化查询。

# 二叉树高频算法题复盘笔记
> 精简版笔记，涵盖核心思路、优化逻辑、核心代码与复杂度分析，适配刷题快速复盘

## LeetCode 105 从前序与中序遍历构造二叉树
### 1. 解题思路
核心依托二叉树遍历的固有特性，采用**递归分治**思想拆解问题，核心逻辑可拆分为四步：
1. **定位根节点**：前序遍历遵循「根 → 左子树 → 右子树」规则，因此前序序列的第一个元素必然是当前子树的根节点；
2. **拆分中序区间**：中序遍历遵循「左子树 → 根节点 → 右子树」规则，在中序序列中找到根节点的索引后，索引左侧为左子树的中序序列，右侧为右子树的中序序列；
3. **拆分前序区间**：根据中序序列拆分出的左/右子树节点数量，拆分前序序列（根节点后紧跟左子树所有节点，左子树后为右子树所有节点）；
4. **递归构建子树**：用左子树的前序/中序序列递归构建左子树，用右子树的前序/中序序列递归构建右子树，将左右子树挂载到根节点上；
5. **递归终止条件**：当拆分后的前序/中序区间无有效节点（左边界 > 右边界）时，返回空。

### 2. 优化过程
| 阶段       | 实现方式                | 问题                  | 优化方案                          |
|------------|-------------------------|-----------------------|-----------------------------------|
| 基础版     | `inorder.index()`找根索引 + 序列切片 | 1. `index()`是线性查找，单次耗时O(n)；2. 切片生成新列表，有额外内存/时间开销；3. 切片易导致索引错位 | 1. 哈希表预处理中序序列，建立「值-索引」映射，将根索引查找降为O(1)；2. 放弃切片，传递区间边界索引（前序左/右、中序左/右）递归，避免索引错位 |
| 最优版     | 哈希表 + 区间边界递归   | -                    | 查找效率最优，无切片冗余开销      |

### 3. 核心代码（最优版）
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        # 哈希表缓存中序值-索引映射，O(1)查找根节点索引
        val2idx = {val: idx for idx, val in enumerate(inorder)}
        
        def build(pre_l, pre_r, in_l, in_r):
            if pre_l > pre_r:  # 递归终止：无有效节点
                return None
            # 1. 定位当前根节点（前序左边界为根）
            root_val = preorder[pre_l]
            root = TreeNode(root_val)
            # 2. 找到根节点在中序的索引，拆分左右子树区间
            root_idx = val2idx[root_val]
            left_size = root_idx - in_l  # 左子树节点数量
            # 3. 递归构建左右子树
            root.left = build(pre_l+1, pre_l+left_size, in_l, root_idx-1)
            root.right = build(pre_l+left_size+1, pre_r, root_idx+1, in_r)
            return root
        
        n = len(preorder)
        return build(0, n-1, 0, n-1)
```

### 4. 复杂度分析
- 时间复杂度：$O(n)$（哈希表预处理遍历中序序列O(n) + 递归遍历每个节点O(n)，无冗余操作）；
- 空间复杂度：$O(n)$（哈希表存储n个键值对O(n) + 递归调用栈最坏O(n)（二叉树退化为链表））。

---

## LeetCode 437 路径总和 III
### 1. 解题思路
题目核心要求：找到二叉树中所有「仅向下延伸（父→子）」的路径，路径和等于目标值，**路径起点/终点不固定**（无需从根开始、无需到叶子结束）。

#### （1）暴力解法（双重递归）
将问题拆分为两层递归，本质是暴力枚举所有可能路径：
1. **外层递归（选起点）**：遍历二叉树的每一个节点，将每个节点作为「路径的起点」；
   - 终止条件：节点为空，返回0（无起点可选）；
   - 核心操作：返回「以当前节点为起点的路径数」+「以左孩子为起点的路径数」+「以右孩子为起点的路径数」。
2. **内层递归（找路径）**：从当前起点出发，向下遍历所有子节点，累加路径和，统计和为目标值的路径数；
   - 终止条件：节点为空，返回0（无路径可走）；
   - 核心操作：① 判断当前节点值是否等于「剩余需要凑的和」，若是则计数+1；② 递归左/右子树，剩余和 = 原剩余和 - 当前节点值；③ 返回累计的路径数。

#### （2）最优解法（前缀和+回溯）
借鉴数组「和为k的子数组」思想，将路径求和转化为前缀和差值问题：
1. **前缀和定义**：从根节点到当前节点的路径上，所有节点值的累加和（二叉树从根到任意节点的路径唯一）；
2. **核心公式**：若「当前前缀和 - 目标值 = 某个祖先节点的前缀和」，则「该祖先节点的下一个节点到当前节点」的路径和等于目标值；
3. **回溯操作**：深度优先遍历中，左子树的前缀和仅对左子树有效，遍历完左子树后需删除对应前缀和（次数-1），避免干扰右子树计算；
4. **初始值设置**：哈希表初始化`{0:1}`，处理「从根节点到当前节点的路径和正好等于目标值」的情况（此时当前前缀和 - 目标值 = 0）。

### 2. 优化过程
| 阶段       | 实现方式                | 时间复杂度 | 优化核心                          |
|------------|-------------------------|------------|-----------------------------------|
| 暴力版     | 外层选起点 + 内层找路径 | $O(n²)$    | 无，纯暴力枚举，节点重复遍历      |
| 最优版     | 前缀和 + 哈希表 + 回溯  | $O(n)$     | 1. 哈希表缓存前缀和出现次数，O(1)统计有效路径；2. 单次遍历所有节点，无重复计算 |

### 3. 核心代码
#### （1）暴力解法（双重递归）
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        # 内层：固定起点，统计和为remain的路径数
        def dfs_path(node, remain):
            if not node:
                return 0
            # 当前节点值匹配剩余和，计数+1
            cnt = 1 if node.val == remain else 0
            # 递归左/右子树，剩余和扣除当前节点值
            cnt += dfs_path(node.left, remain - node.val)
            cnt += dfs_path(node.right, remain - node.val)
            return cnt
        
        # 外层：遍历所有节点作为起点
        def dfs_start(node):
            if not node:
                return 0
            # 当前节点为起点 + 左/右孩子为起点的路径数总和
            return dfs_path(node, targetSum) + dfs_start(node.left) + dfs_start(node.right)
        
        return dfs_start(root)
```

#### （2）最优解法（前缀和+回溯）
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        # 哈希表：key=前缀和，value=前缀和出现次数
        prefix_cnt = {0: 1}
        self.res = 0  # 统计最终有效路径数
        
        def backtrack(node, cur_sum):
            if not node:
                return
            # 1. 更新当前前缀和（根到当前节点的和）
            cur_sum += node.val
            # 2. 统计有效路径数：找cur_sum - targetSum的前缀和出现次数
            self.res += prefix_cnt.get(cur_sum - targetSum, 0)
            # 3. 缓存当前前缀和（次数+1）
            prefix_cnt[cur_sum] = prefix_cnt.get(cur_sum, 0) + 1
            # 4. 递归遍历左右子树
            backtrack(node.left, cur_sum)
            backtrack(node.right, cur_sum)
            # 5. 回溯：删除当前前缀和，避免干扰其他分支
            prefix_cnt[cur_sum] -= 1
        
        backtrack(root, 0)
        return self.res
```

### 4. 复杂度分析
| 解法       | 时间复杂度 | 空间复杂度 | 说明                     |
|------------|------------|------------|--------------------------|
| 暴力解法   | $O(n²)$    | $O(n)$     | 最坏二叉树退化为链表，每个节点需遍历后续所有节点；递归栈深度最坏O(n) |
| 前缀和解法 | $O(n)$     | $O(n)$     | 单次遍历所有节点；哈希表存储前缀和O(n) + 递归栈O(n) |

---

## 核心考点总结
1. 二叉树递归核心：明确**递归终止条件**，将问题拆分为「处理当前节点 + 递归处理左右子树」的子问题；
2. 优化核心思路：哈希表预处理（索引/前缀和）实现O(1)查找，以少量空间开销换取时间效率的大幅提升；
3. 易错点：105题的区间索引拆分、437题的回溯操作（删除当前前缀和），需重点把控边界与状态回退。