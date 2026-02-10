#
# @lc app=leetcode.cn id=2 lang=python
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0) # 建立虚拟头节点，防止遍历完后丢失新链表的头节点
        curr = dummy
        p1,p2 = l1,l2
        carry = 0
        # 核心循环：只要有连目标未遍历完，或仍有进位，就继续
        while p1 is not None or p2 is not None or carry > 0:
            # 取当前节点值，若遍历完则取0
            val1 = p1.val if p1 else 0
            val2 = p2.val if p2 else 0
            # 计算当前位总和和新进位
            total = val1 + val2 + carry
            carry = total // 10 # 新进位
            current_val = total % 10 # 当前值
            # 新建节点并移动游标
            curr.next = ListNode(current_val)
            curr = curr.next
            # 
            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next

        return dummy.next
# 时间复杂度O(max(m + n))
# 空间复杂度O(1)   
# @lc code=end