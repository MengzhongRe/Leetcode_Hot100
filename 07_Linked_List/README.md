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