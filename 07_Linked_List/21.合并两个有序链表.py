#
# @lc app=leetcode.cn id=21 lang=python
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(-1) # 初始化一个虚拟头节点，防止新链表生成后头节点丢失
        curr = dummy # curr是新链表的遍历指针，始终为新链表的最后一个节点

        p1,p2 = list1,list2 # 双指针遍历两个旧链表

        while p1 and p2:
            if p1.val <= p2.val:
                curr.next = p1 # 把p1节点拼接到curr后面
                p1 = p1.next # 移动p1指针
            else:
                curr.next = p2 # 把p2节点拼接到curr后面
                p2 = p2.next # 移动p2指针
            curr = curr.next # 无论如何都要移动curr指针到新链表最后一个节点
        
        curr.next = p1 if p1 else p2 # 循环结束后至多还有一个链表未遍历完，直接把新链表指针指向该节点即可（原链表是升序的）

        return dummy.next # 虚拟头节点的下一个即是新链表头节点
# 时间复杂度O(m + n)
# 空间复杂度O（1）       
# @lc code=end

