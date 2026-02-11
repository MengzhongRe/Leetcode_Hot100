#
# @lc app=leetcode.cn id=25 lang=python
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        # 用虚拟头节点防止翻转后丢失头节点
        dummy = ListNode(0)
        dummy.next = head
        # prev_tail 上一组翻转后的尾节点（初始化为虚拟头）
        prev_tail = dummy

        while True:
            # 1.找到当前组的尾节点（从prev_tail出发走k步）
            curr_tail = prev_tail
            # 已翻转尾节点向前走k步看看够不够
            for _ in range(k):
                curr_tail = curr_tail.next
                if not curr_tail:
                    return dummy.next # 如果最后一组不够k个直接返回翻转后的头节点
            # 记录下一组翻转前的头节点，防止当组翻转后丢失
            next_group_head = curr_tail.next
            # 翻转当前组([prev_tail.next,curr_tail])
            # 子函数返回翻转后的组头
            new_group_head = self.reverse(prev_tail.next,curr_tail)
            # 存储翻转前的组头节点也就是翻转后的组尾节点
            new_group_tail = prev_tail.next
            # prev_tail指向翻转后的头节点
            prev_tail.next = new_group_head
            # curr_group_tail反转后当前组尾节点指向下一组头节点
            new_group_tail.next = next_group_head
            # 前驱尾节点后移，准备处理下一组
            prev_tail = new_group_tail

    # 用迭代实现从start到end的节点反转
    def reverse(self,start,end):
        """
        定义辅助函数，用于反转从start到end节点的链表，逻辑同206反转链表
        """
        prev = None
        curr = start
        # 循环终止条件，curr走到end的下一个节点
        while prev != end:
            next_node = curr.next# 存储当前指针的原下一个节点
            curr.next = prev # 修改当前节点指向为前一个节点
            prev = curr # 移动前驱指针
            curr = next_node # 移动当前指针到原下一个节点
        return prev #  返回翻转后的头节点(原end)
# 时间复杂度O(n)
# 空间复杂度O(1)
# @lc code=end

