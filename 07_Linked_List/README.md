# 链表经典算法题总结（160/206/234）
本文总结三道高频链表算法题：相交链表（160）、反转链表（206）、回文链表（234），包含解题思路、核心代码、复杂度分析，逻辑清晰且可直接复用。

## 一、160. 相交链表
### 题目核心
给定两个单链表头节点 `headA`/`headB`，找出并返回相交的起始节点（无交点返回 `null`）。**相交定义为节点引用相同，而非值相同**。

### 解题思路（双指针法，最优）
#### 原理推导
设：
- 链表A长度 = `a + c`（`a`：A独有长度，`c`：相交部分长度）
- 链表B长度 = `b + c`（`b`：B独有长度）

让指针 `pA` 遍历A后切换到B，指针 `pB` 遍历B后切换到A，最终两者走的总长度均为 `a + b + c`，会在相交节点相遇（无相交则同时到 `null`）。

#### 核心代码
```python
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        
        pA, pB = headA, headB
        while pA != pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        
        return pA
```

#### 复杂度分析
- 时间复杂度：`O(n + m)`，`n/m` 分别为两个链表长度，最多遍历两轮。
- 空间复杂度：`O(1)`，仅使用常量级指针变量。

---

## 二、206. 反转链表
### 题目核心
反转单链表，返回反转后的头节点。

### 解题思路（迭代双指针法）
通过两个指针 `prev`（前节点）、`curr`（当前节点）遍历链表，核心三步：
1. 保存当前节点的下一个节点（避免链表断裂）；
2. 反转当前节点的指向（`curr.next = prev`）；
3. 双指针同步后移，重复上述操作。

#### 核心代码
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head
        
        prev = None
        curr = head
        while curr:
            next_node = curr.next  # 保存下一个节点
            curr.next = prev       # 反转指向
            prev = curr            # prev后移
            curr = next_node       # curr后移
        
        return prev  # 最终prev为新头节点
```

#### 复杂度分析
- 时间复杂度：`O(n)`，仅遍历链表一次。
- 空间复杂度：`O(1)`，无额外空间开销。

---

## 三、234. 回文链表
### 题目核心
判断单链表是否为回文链表（对称）。

### 解题思路（快慢指针 + 反转后半段链表）
1. **找中点**：快慢指针（慢走1步、快走2步）定位前半段最后一个节点；
2. **反转后半段**：复用反转链表逻辑，反转中点后的后半段链表；
3. **对比两段**：遍历前半段和反转后的后半段，判断节点值是否全相等；
4. **恢复链表（可选）**：将反转的后半段还原，保证输入不被修改。

#### 核心代码
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        # 边界处理
        if not head or not head.next:
            return True
        
        # 1. 快慢指针找前半段最后一个节点
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # 2. 反转后半段链表
        reverse_head = self.reverseList(slow.next)
        
        # 3. 对比前半段和反转后的后半段
        p1, p2 = head, reverse_head
        is_pali = True
        while p2:
            if p1.val != p2.val:
                is_pali = False
                break
            p1 = p1.next
            p2 = p2.next
        
        # 4. 恢复原链表（可选，推荐）
        slow.next = self.reverseList(reverse_head)
        
        return is_pali
    
    # 复用反转链表函数
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
```

#### 复杂度分析
- 时间复杂度：`O(n)`，找中点 `O(n/2)` + 反转后半段 `O(n/2)` + 对比 `O(n/2)`，总为线性级。
- 空间复杂度：`O(1)`，仅使用指针变量，无额外空间。

---

## 整体总结
| 题目         | 核心技巧               | 时间复杂度 | 空间复杂度 |
|--------------|------------------------|------------|------------|
| 160 相交链表 | 双指针遍历切换链表     | O(n+m)     | O(1)       |
| 206 反转链表 | 迭代双指针反转指向     | O(n)       | O(1)       |
| 234 回文链表 | 快慢指针找中点 + 反转  | O(n)       | O(1)       |

**核心共性**：三道题均围绕「链表遍历」「指针操作」展开，反转链表是基础工具，可复用解决回文链表等衍生问题；双指针是链表题最优解的核心思路，能大幅降低空间复杂度。

# 链表经典算法题总结（141/142/21）
本文总结三道高频链表算法题：环形链表（141）、环形链表 II（142）、合并两个有序链表（21），涵盖解题思路、数学证明、核心代码及复杂度分析，逻辑清晰且可直接复用。

## 一、141. 环形链表
### 题目核心
判断给定单链表是否存在环（节点的 `next` 指针指向已出现的节点，形成闭合环），要求空间复杂度尽可能为 `O(1)`。

### 解题思路（快慢指针法/龟兔赛跑算法）
#### 核心原理
- 慢指针（龟）：每次走 1 步；
- 快指针（兔）：每次走 2 步；
- 无环：快指针先走到 `null`（链表终点），返回 `false`；
- 有环：快慢指针最终进入环，快指针速度更快，必然在环内追上慢指针（相遇），返回 `true`。

#### 数学证明（简单版）
设环长为 `L`，慢指针入环时，快慢指针的环内距离为 `d`。每轮移动后，快指针比慢指针多走 1 步，距离减少 1，经过 `d` 轮后距离为 0，必然相遇。

#### 核心代码
```python
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode | None) -> bool:
        # 边界条件：空链表/单节点链表无环
        if not head or not head.next:
            return False
        
        slow, fast = head, head
        # 循环条件：快指针能走2步（避免空指针异常）
        while fast and fast.next:
            slow = slow.next       # 慢指针走1步
            fast = fast.next.next  # 快指针走2步
            if slow == fast:       # 相遇则有环
                return True
        
        # 快指针走到终点，无环
        return False
```

#### 复杂度分析
- 时间复杂度：`O(n)`，无环时遍历链表一次，有环时快慢指针最多遍历 `n` 步；
- 空间复杂度：`O(1)`，仅使用 2 个指针变量，无额外空间开销。

---

## 二、142. 环形链表 II
### 题目核心
进阶版 141 题：判断链表是否有环，若有环则返回**环的入口节点**，无环返回 `null`。

### 解题思路（快慢指针 + 数学推导）
#### 步骤1：复用 141 题逻辑找相遇节点
快慢指针遍历链表，若相遇则说明有环，进入步骤2；否则返回 `null`。

#### 步骤2：数学推导入口节点位置（核心）
定义变量：
- `a`：头节点 → 环入口的节点数；
- `b`：环入口 → 相遇节点的节点数；
- `c`：相遇节点 → 环入口的节点数；
- `L`：环的总长度（`L = b + c`）。

推导过程：
1. 相遇时，慢指针步数 `s = a + b`，快指针步数 `f = a + b + k*L`（`k ≥ 1`，快指针绕环圈数）；
2. 因 `f = 2*s`，代入得 `a + b + k*L = 2(a + b)` → 化简为 `a = k*L - b`；
3. 结合 `L = b + c`，得 `a = c + (k-1)*L`（核心结论）。

#### 步骤3：找入口节点
- 相遇后，将慢指针重置为头节点；
- 快慢指针均改为每次走 1 步，最终会在环的入口节点相遇（`a = c + (k-1)*L`，绕环不影响相遇结果）。

#### 核心代码
```python
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode | None) -> ListNode | None:
        # 步骤1：快慢指针找相遇节点
        slow, fast = head, head
        has_cycle = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                has_cycle = True
                break
        
        # 无环直接返回null
        if not has_cycle:
            return None
        
        # 步骤2：重置慢指针，同速移动找入口
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        # 相遇节点即为入口
        return slow
```

#### 复杂度分析
- 时间复杂度：`O(n)`，找相遇节点 `O(n)` + 找入口节点 `O(n)`，总为线性级；
- 空间复杂度：`O(1)`，仅使用 2 个指针变量。

---

## 三、21. 合并两个有序链表
### 题目核心
将两个升序单链表合并为一个新的升序单链表，返回新链表头节点（要求复用原节点，仅调整指针指向）。

### 解题思路（双指针 + 虚拟头节点）
#### 核心逻辑
1. **虚拟头节点（dummy）**：创建哨兵节点，简化「新链表第一个节点」的边界处理；
2. **遍历指针（curr）**：指向新链表的最后一个节点，用于拼接新节点；
3. **双指针（p1/p2）**：分别遍历两个输入链表，每次取值较小的节点拼接到 `curr` 后；
4. **处理剩余节点**：循环结束后，将未遍历完的链表直接拼接到新链表末尾；
5. **返回结果**：虚拟头节点的 `next`（新链表真正头节点）。

#### 核心代码
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        # 虚拟头节点（哨兵），值无意义
        dummy = ListNode(-1)
        curr = dummy  # 指向新链表末尾
        
        p1, p2 = list1, list2
        # 双指针遍历，拼接较小节点
        while p1 and p2:
            if p1.val <= p2.val:
                curr.next = p1
                p1 = p1.next
            else:
                curr.next = p2
                p2 = p2.next
            curr = curr.next
        
        # 处理剩余节点（最多一个链表有剩余）
        curr.next = p1 if p1 else p2
        
        # 返回新链表头节点
        return dummy.next
```

#### 复杂度分析
- 时间复杂度：`O(n + m)`，`n/m` 为两个链表长度，每个节点仅遍历一次；
- 空间复杂度：`O(1)`，仅使用指针变量，无额外空间开销（未新建节点）。

---

## 整体总结
| 题目         | 核心技巧               | 数学证明       | 时间复杂度 | 空间复杂度 |
|--------------|------------------------|----------------|------------|------------|
| 141 环形链表 | 快慢指针检测环         | 环内距离推导   | O(n)       | O(1)       |
| 142 环形链表 II | 快慢指针 + 数学推导找入口 | a = c + (k-1)L | O(n)       | O(1)       |
| 21 合并有序链表 | 双指针 + 虚拟头节点    | 无             | O(n+m)     | O(1)       |

### 核心共性
1. **指针操作是核心**：快慢指针/双指针是链表题最优解的关键，可大幅降低空间复杂度；
2. **边界处理技巧**：虚拟头节点（21题）、空指针判断（141/142题）是避免异常的核心；
3. **数学推导辅助**：142题的公式推导是找环入口的关键，简化记忆为 `a = c` 即可满足解题需求。


---

## 1. 两数相加
### 题目核心
输入两个**逆序存储数字**的单链表（如 `2→4→3` 代表 342），逐位相加并处理进位，返回逆序存储结果的链表。

### 解题思路
1. **虚拟头节点**：简化链表构建，避免头节点为空的特殊处理；
2. **逐位相加**：遍历两个链表，计算当前位总和（含前一位进位）；
3. **进位处理**：用整除 `//10` 计算进位，取余 `%10` 计算当前位值；
4. **边界处理**：循环条件包含「链表未遍历完」或「仍有进位」，覆盖所有场景。

### 核心代码
```python
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)  # 虚拟头节点
        curr = dummy
        p1, p2 = l1, l2
        carry = 0  # 进位
        
        # 核心循环：处理所有节点 + 最后进位
        while p1 or p2 or carry > 0:
            val1 = p1.val if p1 else 0
            val2 = p2.val if p2 else 0
            
            total = val1 + val2 + carry
            carry = total // 10
            current_val = total % 10
            
            curr.next = ListNode(current_val)
            curr = curr.next
            
            # 指针后移
            if p1: p1 = p1.next
            if p2: p2 = p2.next
        
        return dummy.next
```

### 复杂度分析
- **时间复杂度**：O(max(n, m))，n/m 为两个链表长度，循环次数由最长链表+进位决定；
- **空间复杂度**：O(max(n, m))（含输出）/ O(1)（仅额外变量），输出链表长度最多为最长链表+1。

---

## 2. 删除链表的倒数第 N 个结点
### 题目核心
删除单链表的倒数第 N 个节点，要求尽可能少遍历链表（最优为一次遍历）。

### 解题思路
1. **双指针法（最优）**：
   - 虚拟头节点：统一处理删除头节点的场景；
   - 快慢指针：快指针先移动 N 步，再与慢指针同步移动；
   - 精准定位：快指针到末尾时，慢指针停在目标节点的前驱，直接删除。
2. **边界处理**：覆盖「删除头节点/尾节点/中间节点」「奇数/偶数长度链表」。

### 核心代码
```python
class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        slow, fast = dummy, dummy
        
        # 快指针先走n步
        for _ in range(n):
            fast = fast.next
        
        # 同步移动，直到快指针到末尾
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        # 删除目标节点
        slow.next = slow.next.next
        
        return dummy.next
```

### 复杂度分析
- **时间复杂度**：O(L)，L 为链表长度，仅遍历链表一次；
- **空间复杂度**：O(1)，仅使用有限指针变量，无额外动态空间。

---

## 3. 两两交换链表中的节点
### 题目核心
两两交换链表相邻节点（不修改节点值，仅调整指针），奇数长度链表保留最后一个节点。

### 解题思路
1. **迭代法（最优）**：
   - 虚拟头节点：统一处理头节点交换；
   - 分组交换：每两个节点为一组，调整指针完成交换；
   - 边界处理：循环条件为「至少有两个节点可交换」，奇数长度自动保留最后一个节点；
   - 断链防护：先衔接下一组节点，再完成当前组交换，避免链表断裂。

### 核心代码
```python
class Solution(object):
    def swapPairs(self, head):
        # 边界：空/单节点直接返回
        if not head or not head.next:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy  # 前驱节点，指向待交换组的前一个节点
        
        # 循环条件：至少有两个节点可交换（处理奇数长度）
        while prev.next and prev.next.next:
            first = prev.next       # 组内第一个节点
            second = prev.next.next # 组内第二个节点
            
            # 核心交换：三步调整指针
            prev.next = second       # 前驱指向第二个节点
            first.next = second.next # 第一个节点衔接下一组
            second.next = first      # 第二个节点指向第一个节点
            
            prev = first  # 前驱后移，处理下一组
        
        return dummy.next
```

### 复杂度分析
- **时间复杂度**：O(n)，n 为链表长度，每个节点仅访问一次；
- **空间复杂度**：O(1)，仅使用有限指针变量，无额外动态空间。

---

## 共性总结
| 核心技巧         | 适用场景                     | 关键作用                     |
|------------------|------------------------------|------------------------------|
| 虚拟头节点       | 所有链表修改类问题           | 统一处理头节点，简化边界判断 |
| 双指针法         | 倒数定位、快慢遍历场景       | 减少遍历次数，提升效率       |
| 指针衔接顺序     | 节点交换/删除                | 避免链表断链                 |
| 循环条件设计     | 进位/奇数长度/边界场景       | 覆盖所有测试用例             |

### 链表问题通用思路
1. 优先使用虚拟头节点，避免头节点特殊处理；
2. 指针操作遵循「先衔接后修改」，防止断链；
3. 循环条件需覆盖「边界场景」（如进位、奇数长度）；
4. 时间复杂度优先优化到 O(n)，空间复杂度优先 O(1)（迭代法）。

---

# 📚 链表进阶算法笔记 (Linked List Mastery)

## 📌 目录
1.  **[25] K 个一组翻转链表** —— 链表指针操作的天花板
2.  **[148] 排序链表** —— 归并排序在链表中的应用
3.  **[138] 随机链表的复制** —— 空间优化的极致技巧

---

## ⚔️ 1. [25] K 个一组翻转链表 (Reverse Nodes in k-Group)

> **一句话题解**：
> 这是一个“局部翻转 + 全局连接”的问题。核心在于维护好每组的“前驱节点”和“后继节点”，防止断链。

### 💡 解题思路 (迭代法)
1.  **探路**：从当前位置向后走 $k$ 步，判断剩余节点是否足够 $k$ 个。若不足，直接结束（保持原样）。
2.  **断开与记录**：记录当前组的头 `start`、尾 `end`，以及下一组的头 `next_group_head`。
3.  **局部翻转**：对 `[start, end]` 区间进行标准链表翻转。
4.  **拼接**：
    *   将上一组的尾巴 `prev_group_tail` 连接到翻转后的新头（原 `end`）。
    *   将翻转后的新尾巴（原 `start`）连接到下一组的头 `next_group_head`。
5.  **推进**：更新 `prev_group_tail`，进入下一轮。

### 🚀 核心代码 (Python)
```python
class Solution(object):
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        prev_group_tail = dummy # 永远指向"待翻转区域"的前一个节点

        while True:
            # 1. 检查剩余节点是否有 k 个
            kth = prev_group_tail
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next # 不足 k 个，直接返回
            
            # 2. 记录关键节点
            group_start = prev_group_tail.next
            next_group_head = kth.next
            
            # 3. 翻转当前组 (传入头部和尾部)
            # 翻转后：group_start 变成尾，kth 变成头
            self.reverse(group_start, kth)
            
            # 4. 重新连接
            prev_group_tail.next = kth        # 上一组尾 -> 接当前组新头
            group_start.next = next_group_head # 当前组新尾 -> 接下一组头
            
            # 5. 指针推进
            prev_group_tail = group_start
    
    # 辅助函数：翻转 [start, end] 区间
    def reverse(self, start, end):
        prev, curr = None, start
        while prev != end: # 巧妙的终止条件
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
```

### 📊 复杂度分析
*   **时间复杂度**：$O(N)$。每个节点被访问两次（一次探路，一次翻转）。
*   **空间复杂度**：$O(1)$。只使用了有限的指针变量。

---

## ⚔️ 2. [148] 排序链表 (Sort List)

> **一句话题解**：
> 链表排序首选 **归并排序 (Merge Sort)**。利用分治思想：切分找中点 -> 递归排序 -> 合并有序链表。

### 💡 解题思路 (递归归并)
1.  **Base Case**：若链表为空或只有一个节点，视为有序，直接返回。
2.  **找中点 (Cut)**：使用 **快慢指针**。
    *   *技巧*：`fast` 初始指向 `head.next`，确保偶数个节点时 `slow` 停在左半部分的最后一个节点，方便断链。
3.  **递归 (Conquer)**：
    *   `left = sortList(head)`
    *   `right = sortList(mid)`
4.  **合并 (Merge)**：使用“合并两个有序链表”的逻辑（LeetCode 21 原题）将左右两部分合并。

### 🚀 核心代码 (Python)
```python
class Solution(object):
    def sortList(self, head):
        # 1. 终止条件
        if not head or not head.next:
            return head
        
        # 2. 快慢指针找中点
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 3. 切分链表
        mid = slow.next
        slow.next = None # 【关键】断链
        
        # 4. 递归排序
        left = self.sortList(head)
        right = self.sortList(mid)
        
        # 5. 合并
        return self.merge(left, right)

    def merge(self, l1, l2):
        dummy = ListNode(0)
        curr = dummy
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 if l1 else l2
        return dummy.next
```

### 📊 复杂度分析
*   **时间复杂度**：$O(N \log N)$。递归树层级为 $\log N$，每层合并耗时 $N$。
*   **空间复杂度**：$O(\log N)$。递归栈的深度（若用迭代法则为 $O(1)$，但递归法更适合面试手写）。

---

## ⚔️ 3. [138] 随机链表的复制 (Copy List with Random Pointer)

> **一句话题解**：
> 如何处理随机指针指向“还没创建的节点”？
> **方法一**：哈希表存映射（简单直观）。
> **方法二**：交替拼接链表（原地算法，空间最优）。

### 💡 解题思路 (原地交替拼接法)
这是**空间复杂度 O(1)** 的神级解法，分三步走：
1.  **复制节点并拼接**：
    *   将新节点 $A'$ 插在原节点 $A$ 后面。
    *   变身前：`A -> B -> C`
    *   变身后：`A -> A' -> B -> B' -> C -> C'`
2.  **复制 Random 指针**：
    *   因为 $A'$ 在 $A$ 后面，所以 $A'$.random 就是 $A$.random.next。
    *   `curr.next.random = curr.random.next` (若 `curr.random` 存在)。
3.  **拆分链表**：
    *   将交织在一起的链表拆开，恢复原链表，并提取出新链表。
    *   `curr.next = curr.next.next`。

### 🚀 核心代码 (Python)
```python
class Solution(object):
    def copyRandomList(self, head):
        if not head: return None
        
        # 第一步：复制节点，交替拼接
        # A -> B  =>  A -> A' -> B -> B'
        curr = head
        while curr:
            new_node = Node(curr.val)
            new_node.next = curr.next
            curr.next = new_node
            curr = new_node.next # 移动到下一个原节点
            
        # 第二步：复制 random 指针
        curr = head
        while curr:
            if curr.random:
                # 新节点的 random 指向 原节点 random 的下一个（也就是它的副本）
                curr.next.random = curr.random.next
            curr = curr.next.next
            
        # 第三步：拆分链表
        # 恢复原链表，提取新链表
        curr = head
        new_head = head.next
        while curr.next:
            nxt = curr.next # nxt 是新节点
            curr.next = nxt.next # 原节点指向原节点
            curr = nxt # 步进
            
        return new_head
```

### 📊 复杂度分析
*   **时间复杂度**：$O(N)$。遍历了三次链表。
*   **空间复杂度**：$O(1)$。除了返回用的新链表空间外，没有使用额外的 Hash Map。

---

### 🏆 总结对比

| 题目 | 核心难点 | 关键技巧 | 复杂度 (Time/Space) |
| :--- | :--- | :--- | :--- |
| **[25] K个一组翻转** | 局部翻转后的断链与重连 | `prev_group_tail` 锚点，`reverse` 返回范围 | $O(N)$ / $O(1)$ |
| **[148] 排序链表** | $O(N \log N)$ 的时间限制 | 快慢指针找中点 + 归并排序 | $O(N \log N)$ / $O(\log N)$ |
| **[138] 随机指针复制** | 深拷贝时的节点映射 | **A -> A' -> B -> B'** 交替拼接法 | $O(N)$ / $O(1)$ |

---

## ⚔️ 1. [23] 合并 K 个升序链表 (Merge k Sorted Lists)

> **一句话题解**：
> 面对多路有序数据流的合并，**最小堆 (Min-Heap)** 是永远的神，它能充当“高效筛选器”，每次以 $O(\log k)$ 的代价选出当前最小的节点。

### 📉 优化过程推演

*   **阶段一：暴力法 (Brute Force)**
    *   **思路**：把所有链表的节点全部扔到一个大数组里，然后对数组排序，最后重建链表。
    *   **痛点**：完全忽略了“链表已经有序”这个宝贵信息。时间复杂度 $O(N \log N)$，空间 $O(N)$。
    
*   **阶段二：逐一比较法 (Compare One by One)**
    *   **思路**：每次遍历 $K$ 个链表的头节点，找出最小的那个，接到结果后面。
    *   **痛点**：每选一个节点都要遍历 $K$ 次。总时间 $O(N \times K)$。当 $K$ 很大时，效率极低。

*   **阶段三：优先队列 / 最小堆 (Priority Queue - Optimal)**
    *   **思路**：我们要快速在 $K$ 个数中找到最小值，这正是**最小堆**的强项。我们将比较的复杂度从 $O(K)$ 降维到了 $O(\log K)$。
    *   **关键技巧**：Python 的 `heapq` 无法直接比较 `ListNode` 对象。
        *   *错误写法*：`heapq.heappush(h, node)` -> 报错 `TypeError`。
        *   *正确写法*：存入三元组 `(val, index, node)`。`val` 用于排序，`index` 用于打破平局（Tie-breaker），确保永远不需要比较 `node` 对象本身。

### 🚀 核心代码 (Python)

```python
import heapq

class Solution(object):
    def mergeKLists(self, lists):
        # 1. 初始化最小堆
        # 堆中存放三元组：(节点值, 唯一索引, 节点对象)
        min_heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, i, node))
        
        # 2. 虚拟头节点，简化链表构建
        dummy = ListNode(0)
        curr = dummy
        
        # 3. 循环弹出最小值
        while min_heap:
            # 弹出堆顶（当前所有链表头中最小的那个）
            val, i, node = heapq.heappop(min_heap)
            
            # 拼接到结果链表
            curr.next = node
            curr = curr.next
            
            # 4. 补充新元素
            # 如果被弹出的节点还有后继，将其推入堆中
            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))
                
        return dummy.next
```

### 📊 复杂度分析
*   **时间复杂度**：$O(N \log K)$。
    *   $N$ 是所有节点的总数，$K$ 是链表的条数。
    *   每个节点都会进堆出堆一次，每次堆操作耗时 $O(\log K)$。
*   **空间复杂度**：$O(K)$。
    *   堆中最多同时存在 $K$ 个元素（每条链表的当前头节点）。

---

## ⚔️ 2. [146] LRU 缓存 (LRU Cache)

> **一句话题解**：
> 当需要同时满足 **查找快** (Hash Map) 和 **维护时间顺序** (Linked List) 时，**哈希表 + 双向链表** 是唯一的正解。

### 🧠 设计思路推演

*   **需求分析**：
    1.  `get(key)`: 需要 $O(1)$ 找到数据 -> **必须用哈希表**。
    2.  `put(key, value)`: 
        *   需要 $O(1)$ 更新数据。
        *   **难点**：当缓存满时，需要淘汰“最久未使用的”。这意味着我们需要维护一个时间顺序队列。
    3.  **核心冲突**：
        *   用数组/普通队列存顺序？删除中间某个节点（比如把刚访问的元素移到队尾）需要 $O(N)$ 的移动时间。**不合格**。
        *   用单向链表？删除节点需要遍历找到前驱，也是 $O(N)$。**不合格**。
    
*   **最终方案：哈希链表 (Hash + Doubly Linked List)**
    *   **双向链表**：节点自带 `prev` 和 `next` 指针，**只要拿到了节点对象的引用，就能在 $O(1)$ 时间内把自己从链表中摘除**。
    *   **哈希表**：存储 `Key -> Node` 的映射。让我们能瞬间拿到节点对象的引用。

### 🏗️ 架构设计图
*   **Head (伪头)** <-> [最新节点] <-> [次新节点] <-> ... <-> [最旧节点] <-> **Tail (伪尾)**
*   *注：也可以定义 Head 为最旧，Tail 为最新，只要逻辑自洽即可。下文代码采用 Head 为最新。*

### 🚀 核心代码 (标准手写版)

```python
class DLinkedNode:
    """双向链表节点"""
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.cache = dict() # Hash Map: key -> node
        self.capacity = capacity
        self.size = 0
        # 伪头和伪尾，避免处理 null 指针
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key not in self.cache:
            return -1
        # 1. 通过哈希表找到节点
        node = self.cache[key]
        # 2. 移动到头部（标记为最近使用）
        self.moveToHead(node)
        return node.value

    def put(self, key, value):
        if key not in self.cache:
            # 新增节点
            node = DLinkedNode(key, value)
            self.cache[key] = node
            self.addToHead(node) # 放在头部
            self.size += 1
            
            if self.size > self.capacity:
                # 淘汰最久未使用的（尾部节点）
                removed = self.removeTail()
                self.cache.pop(removed.key) # 别忘了删哈希表
                self.size -= 1
        else:
            # 更新节点
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)

    # --- O(1) 的链表操作 ---
    
    def addToHead(self, node):
        """插入到伪头之后"""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def removeNode(self, node):
        """从链表中摘除节点"""
        node.prev.next = node.next
        node.next.prev = node.prev

    def moveToHead(self, node):
        """移动到头部 = 先摘除 + 再插入"""
        self.removeNode(node)
        self.addToHead(node)

    def removeTail(self):
        """删除尾部节点（淘汰）"""
        res = self.tail.prev
        self.removeNode(res)
        return res
```

### ⚡ Python 作弊版 (OrderedDict)
面试时如果允许使用标准库，可以用这个。原理相同，但封装更完美。

```python
from collections import OrderedDict

class LRUCache(OrderedDict):
    def __init__(self, capacity):
        super().__init__()
        self.capacity = capacity

    def get(self, key):
        if key not in self:
            return -1
        self.move_to_end(key) # 刷新到末尾
        return self[key]

    def put(self, key, value):
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False) # 弹出开头（最旧的）
```

### 📊 复杂度分析
*   **时间复杂度**：
    *   `get`: $O(1)$。哈希查找 + 链表指针修改，均为常数操作。
    *   `put`: $O(1)$。同上。
*   **空间复杂度**：$O(capacity)$。
    *   需要存储 `capacity` 个节点和哈希表条目。

---

## 🏆 总结与对比

| 题目 | 核心数据结构 | 关键技巧 | 为什么难？ |
| :--- | :--- | :--- | :--- |
| **[23] 合并K个链表** | **最小堆 (Min-Heap)** | 存入三元组 `(val, i, node)` 避免比较报错 | 需要理解堆如何处理流式数据的 Top K 问题。 |
| **[146] LRU 缓存** | **哈希表 + 双向链表** | 伪头伪尾 (`dummy head/tail`) 简化边界判断 | 需要手写双向链表的指针操作，容易写错 prev/next。 |

**🌟 今日心得**：
1.  **堆** 是处理“在一堆动态数据中找最值”的最佳工具。
2.  **双向链表** 的最大优势在于：一旦拥有节点引用，删除自身只需要 $O(1)$。
3.  **复合数据结构**（如哈希表+链表）通常是解决 $O(1)$ 复杂约束问题的终极方案。