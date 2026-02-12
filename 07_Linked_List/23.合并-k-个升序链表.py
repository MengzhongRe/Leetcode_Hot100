#
# @lc app=leetcode.cn id=23 lang=python
#
# [23] 合并 K 个升序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 维护一个大小为k的最小堆，每次从堆中取出元素（自然是最小元素）直接接在答案链表后面，再推入该元素后面的节点自动调整堆结构。
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        # 边界处理：空列表直接返回None
        if not lists:
            return None
        # 过滤掉Lists中的None
        lists = [l for l in lists if l is not None]
        # 创建一个最小堆
        min_heap = [] # 维护一个大小为K的最小堆
        for i,node in enumerate(lists):
            heapq.heappush(min_heap,(node.val,i,node))
        dummy = ListNode(0) # 虚拟头节点
        curr = dummy
        # 只要堆中还有元素，也就是只要还有节点未处理
        while min_heap:
            val,i,node = heapq.heappop(min_heap) # 获取并删除堆顶元素即堆中最小的节点O(logk)
            curr.next = node # 直接吧这个最小值赋给当前节点的指向
            curr = curr.next # 移动指针
            if node.next: # 如果该链表节点后还有剩余节点，则将其加入到堆中，自动调整结构
                heapq.heappush(min_heap,(node.next.val,i,node.next)) # o(logk)
        
        return dummy.next
# 时间复杂度O(nk*logk),总共有nk个节点需要处理，每个节点最多入堆出堆一次，每次需进行堆的删除和插入操作，耗时O(logk)
# 空间复杂度O(k) ,堆中最多同时存在k个节点
# @lc code=end
# 暴力解法
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        if not lists:
            return None
        prev_list = lists[0]
         
        for i in range(1,len(lists)):
            curr_list = lists[i]
            prev_list = self.merge(prev_list,curr_list)

        return prev_list
    
    def merge(self,l1,l2):
        dummy = ListNode(0)
        curr = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 if l1 else l2

        return dummy.next
# 时间复杂度O(k**2n)：假设每个链表平均长度为 n，K 个链表逐次合并的时间复杂度为 O(k²n)（第一次合并 2n，第二次合并 3n… 第 k-1 次合并 kn，总和为 n×(2+3+…+k) = O (k²n)）。
# 空间复杂度O(1)