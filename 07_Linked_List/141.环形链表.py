#
# @lc app=leetcode.cn id=141 lang=python
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None
# 快慢指针找链表环,快指针每次走两步，慢指针每次走一步
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 边界判断,空链表或单节点链表无环
        if not head or not head.next:
            return False
        # 初始化快慢指针
        slow = head
        fast = head
        # 循环条件：只要fast指针不是None(链表末尾)或不指向链表末尾
        while fast and fast.next:
            # 快指针走两步
            fast = fast.next.next
            # 慢指针走一步
            slow = slow.next
            # 两者相遇即说明有环
            if slow == fast:
                return True
        # 循环结束都没有返回，说明fast已经走到链表的末尾，无环
        return False
# 时间复杂度O(n),无环，快指针走到末尾，o(n);有环，慢指针走n-l步进入环，快指针最多追L步（l为环长）
# 空间复杂度O(1)     
# @lc code=end

