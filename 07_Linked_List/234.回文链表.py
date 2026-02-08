#
# @lc app=leetcode.cn id=234 lang=python
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        # 若链表为空或链表中只有一个节点，则一定为回文
        if not head or not head.next:
            return True
        # 用快慢指针找链表前半段的最后一个节点
        slow = head
        fast = head
        # 只要fast还能走两步到非None节点就移动快慢指针
        while fast.next and fast.next.next:
            slow = slow.next # 慢指针每次移动一步
            fast = fast.next.next # 快指针每次移动两步
        # 循环结束后，slow指针一定会在前半段的最后一个节点，当链表长度为偶数时，它就是在前刚好一半的最后一个节点
        # 奇数时，则为中间节点。
        # 无论如何，我们都从slow下一个节点开始反转链表，此时一定有后半段链表的长度<=前半段链表的长度
        reverse_head = self.reverseList(slow.next) # 存储反转后的后半段链表的头节点
        # 初始化返回值为True
        is_pali = True
        p1 = head # 初始化两个指针，开始逐一遍历前半段和后半段链表的节点
        p2 = reverse_head

        while p2: # 只需遍历到后半段结束，因为后半段长度一定《=前半段长度，当前半段多一个数时，不需要管
            if p1.val != p2.val:
                is_pali = False
                break
            p1 = p1.next
            p2 = p2.next
        # 恢复原链表
        slow.next = self.reverseList(reverse_head)
        
        return is_pali



    def reverseList(self,head):
        """
        reverseList 的 Docstring
        
        :param self: 说明
        :param head: Optional[ListNode]
        :rtype: OPtional[ListNode]
        """
        # 边界判断
        if not head or not head.next:
            return head
        
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
# 时间复杂度O(n)
# 空间复杂度O(1)   
# @lc code=end

