#
# @lc app=leetcode.cn id=160 lang=python
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 双指针法思路 1：双指针法（最优，时间 O (n+m)，空间 O (1)）
 #核心思想：让两个指针分别遍历两个链表，遍历完自己的链表后，切换到另一个链表的头节点继续遍历，最终两个指针会在相交节点相遇（或同时到 null）。
# 链表 A 的长度 = a + c（c 是相交部分长度，a 是 A 独有的长度）
# 链表 B 的长度 = b + c（b 是 B 独有的长度）
# 指针 pA 走：a + c + b
# 指针 pB 走：b + c + a
# 两者走的总长度相等，因此会在相交节点相遇；若没有相交（c=0），则最终都走到 null。

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # 边界判断
        if not headA or not headB:
            return None
        # 初始化两个指针，分别指向两个链表的头节点
        p1 = headA
        p2 = headB
        # 循环：直到两个指针相遇
        while p1 != p2:
            # 如果pA走到链表末尾，切换到headB；否则走下一步
            p1 = p1.next if p1 else headB
            # 如果pB走到链表末尾，切换到headA；否则走下一步
            p2 = p2.next if p2 else headA
         # 循环结束时，pA（或pB）要么是相交节点，要么是null（无相交）
        return p1
# 时间复杂度O(n + m)
# 空间复杂度O(1)        
# @lc code=end
# 哈希表法
class Solution:
    def getIntersectionNode(self,headA,headB):
        """
        :param self: 说明
        :param headA: Optional[ListNode]
        :param headB: Optional[ListNode]
        :rtype: ListNode
        """
        nodes_set = set() # 初始化哈希表
        p1 = headA
        while p1: # 遍历headA,把所有遍历到的节点加入到哈希表
            nodes_set.add(p1)
            p1 = p1.next
        
        p2 = headB
        while p2:
            if p2 in nodes_set:
                return p2
            p2 = p2.next
        
        return None
# 时间复杂度O(m + n)
# 空间复杂度O(n)



