#
# @lc app=leetcode.cn id=138 lang=python
#
# [138] 随机链表的复制
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
# 用哈希表存储新旧节点之间的映射，两轮遍历，第一轮遍历仅初始化新节点的val,等到第二轮遍历所有节点已经初始化完毕后再设置next,random
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        # 边界判断
        if not head:
            return None
        # 步骤一:创建哈希表，简历旧节点和新节点之间的映射
        node_map = {}
        curr = head
        while curr:
            # 先创建新节点，仅赋值val（next/random指针后续设置）
            node_map[curr] = Node(curr.val)
            curr = curr.next  

        # 步骤二：第二次遍历原链表，设置新节点的Next、random
        curr = head
        while curr:
            # 先获取当前节点的对应新节点
            new_node = node_map[curr]
            # 设置新节点的next指针
            new_node.next = node_map.get(curr.next) # 不存在则返回None
            # 设置新节点的random指针
            new_node.random = node_map.get(curr.random)
            curr = curr.next # curr指针前移
        
        return node_map[head]

# 时间复杂度O(n)
# 空间复杂度O(n)
# @lc code=end
# 原地拆分法：无需额外哈希表，通过「原节点后插入新节点 → 设置 random → 拆分链表」三步实现：
# 插入新节点：遍历原链表，在每个原节点后插入对应的新节点（如 1→新1→2→新2）；
# 设置 random：利用「新节点 = 原节点.next」的关系，设置新节点的 random（新节点.random = 原节点.random.next）；
# 拆分链表：将混合链表拆分为原链表和新链表，恢复原链表结构，返回新链表。
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        # 步骤一：在每个原节点后插入新节点
        curr = head
        while curr:
            new_node = Node(curr.val)
            new_node.next = curr.next
            curr.next = new_node
            curr = new_node.next # 跳过新节点，直接处理原来的下一个节点
        # 步骤二：设置新节点的random指针
        curr = head
        while curr:
            new_code = curr.next
            # 原节点的random不为空时，新节点的random = 原节点的random.next
            if curr.random:
                new_code.random = curr.random.next
            curr = new_code.next # 跳过新节点，处理下一个旧节点
        # 步骤三：拆分链表（恢复原链表，提取新链表）
        curr = head
        new_head = curr.next
        while curr:
            new_code = curr.next
            # 恢复原链表的next指针
            curr.next = new_code.next
            # 设置新链表的节点的next指针
            if new_code.next:
                new_code.next = new_code.next.next
            curr = curr.next # 移动当前指针

        return new_head
# 时间复杂度O(n)
# 空间复杂度O(1)