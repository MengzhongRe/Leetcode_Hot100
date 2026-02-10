#
# @lc app=leetcode.cn id=19 lang=python
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 快慢指针一次遍历链表，快指针先走n + 1步，当fast指针走到None时，slow即走到目标节点的前一个节点
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        # 创建虚拟节点，防止头节点丢失
        dummy = ListNode(0)
        dummy.next = head
        slow,fast = dummy,dummy
        # 让fast指针先走n + 1步，因为我们需要让slow指针停到倒数第n个节点的前一个
        for _ in range(n + 1):
            fast = fast.next
         # 2. fast 和 slow 同时移动，直到 fast 走到尽头
        while fast:
            fast = fast.next
            slow = slow.next
        # 3. 此时 slow.next 就是倒数第 n 个节点，删除它
        slow.next = slow.next.next

        return dummy.next
# 时间复杂度O(n)
# 空间复杂度O(1)
# @lc code=end

# 两次遍历链表，第一次计算来链表长度，第二次删除目标
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        point = head
        lenth = 0
        # 遍历链表计算链表总长度
        while point:
            point = point.next
            len += 1
        # 创建虚拟节点指向新头节点
        dummy = ListNode(0)
        dummy.next = head # 当head是None时，直接返回None
        # 移动到目标节点前一个节点
        curr =dummy
        # 我们需要移动(lenth - n)次
        for _ in range(lenth - n):
            curr = curr.next
            # 删除目标节点
        curr.next = curr.next.next
        return dummy.next
# 时间复杂度O(n)
# 空间复杂度O(1)