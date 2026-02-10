#
# @lc app=leetcode.cn id=24 lang=python
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        # 创建虚拟节点防止后续头节点消失
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy # prev:当前待交换组的前驱节点

        # 循环条件：至少有两个节点可交换（处理奇数长度的核心）
        while prev.next and prev.next.next:
            # 1.存储当前组的两个节点，防止因交换丢失节点
            first = prev.next
            sencond = prev.next.next
            # 核心交换：三步调整指针
            prev.next = sencond # 步骤一：前驱指向第二个节点（交换后第一个）
            first.next = sencond.next # 步骤二：第一个节点指向下一组首节点
            sencond.next = first # 步骤三：第二个节点指向第一个节点（交换后第二个）
            # 交换完成后，前驱节点移到当前组最后一位
            prev = first
        # 返回交换后的头节点
        return dummy.next     
# 时间复杂度O(n)
# 空间复杂度O(1)
# @lc code=end

