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