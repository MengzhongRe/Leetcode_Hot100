#
# @lc app=leetcode.cn id=142 lang=python
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return None
        
        has_cycle = False

        slow,fast = head,head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                has_cycle = True
                break
        
        # 无环，直接返回null
        if not has_cycle:
            return None
        
        slow = head # 慢指针重置为头节点
        while slow != fast:
            slow = slow.next
            fast = fast.next 

        return slow  
# 时间复杂度O(n)
# 空间复杂度O(1)
# @lc code=end

