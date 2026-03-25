#
# @lc app=leetcode.cn id=215 lang=python
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        min_heap = [] # 初始化最小堆，堆顶是堆中最小的元素
        # 遍历原数组
        for num in nums:
            # 分两个阶段，第一阶段当索引<k时，直接把数组中的元素加入堆中
            if len(min_heap) < k:
                heapq.heappush(min_heap,num)
            # 第二阶段，当堆中元素已经达到k时，需比较其与堆顶元素（即最小值），若其比堆顶元素大
            # 则我们可以pop掉堆顶元素，加入新元素，然后调整堆结构
            elif num > min_heap[0]:
                # heapreplace仅仅只需要一次堆调整，而heappop,heappush需要两次，更好
                heapq.heapreplace(min_heap,num)
        # 遍历结束后堆顶元素自然就是原数组中第k大的值
        return min_heap[0]      
# 时间复杂度O(N * logK),每个元素需要遍历一次，最多每个入堆一次，出堆一次，每次入堆或出堆一次调整堆结构最多需要logK
# 因此时N * logK
# 空间复杂度O(K),经典的top K问题需要最大K的最小堆
# @lc code=end

import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        min_heap = nums[:k] # 取数组前k个元素的切片O(K)
        heapq.heapify(min ) # 直接对切片后的数组建最小堆O(K)，防止因遍历数组逐个放入堆中从而调整堆结构导致的O(k*logk)

        # 在这里我们直接用索引，而非数组切片nums[k:]因为在python中数组切片会新开辟切片长度的新内存，时间复杂度也是O(L)
        # L是切片长度，在本题目就是O(n - k),在大量流失数据下会导致空间复杂度直接爆炸到O(N)，因此不适合
        for i in range(k,len(nums)):
            if nums[i] > min_heap[0]:
                # heapreplace仅仅只需要一次堆调整，而heappop,heappush需要两次，更好
                heapq.heapreplace(min_heap,nums[i])
        # 遍历结束后堆顶元素自然就是原数组中第k大的值
        return min_heap[0] 