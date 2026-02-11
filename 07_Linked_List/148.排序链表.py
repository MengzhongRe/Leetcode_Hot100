#
# @lc app=leetcode.cn id=148 lang=python
#
# [148] 排序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 自顶向下法（递归法）
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        
        # 快慢指针找中点,fast指针先走一步防止偶数长度时,slow指针走到后半部分
        slow,fast = head,head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 循环结束后slow指针在前半部分尾部slow.next为后半部分的头节点
        mid = slow.next
        # 切断前后链表链接，防止后续merge归并出现混乱
        slow.next = None
        #对左右两侧递归排序
        left = self.sortList(head)
        right = self.sortList(mid)
        # 对排好序的左右链表归并
        return self.merge(left,right)

    def merge(self,left,right):
        dummy = ListNode(0)
        curr = dummy
        while left and right:
            if left.val <= right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next
        curr.next = left if left else right

        return dummy.next
# 时间复杂度O(nlogn),本质是归并排序，总共有logN层递归，每层都需要遍历所有节点找中点即o(N),
# 空间复杂度O(logn),取决于递归深度     
# @lc code=end

class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        node_list = [] # 初始化节点列表用于排序节点
        curr = head
        while curr: # 把原链表的节点逐个加入列表
            node_list.append(curr)
            curr = curr.next
        
        # 步骤2：按值排序节点列表
        node_list.sort(key=lambda x: x.val)
        # 创建虚拟头节点
        dummy = ListNode(0)
        curr = dummy
        # 按顺序遍历排好序的节点列表
        for node in node_list:
            curr.next = node
            curr = curr.next
        curr.next = None # 最后一个节点置None，避免环

        return dummy.next
# 时间复杂度O(nlogn),主要取决于排序
# 空间复杂度O(n)  
    