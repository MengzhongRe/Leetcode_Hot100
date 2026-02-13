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