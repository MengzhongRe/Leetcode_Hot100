#
# @lc app=leetcode.cn id=295 lang=python
#
# [295] 数据流的中位数
#

# @lc code=start
import bisect
class MedianFinder(object):

    def __init__(self):
        self.nums = []


    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
         #手动实现二分插入
        # def binary_insert(left,right):
        #     while left <= right:
        #         mid = left + (right - left) // 2
        #         if num < self.nums[mid]:
        #             right = mid - 1
        #         else:
        #             left = mid + 1
        #     self.nums.insert(left,num)
        
        # binary_insert(0,len(self.nums) - 1)
        bisect.insort(self.nums,num)
        

    def findMedian(self):
        """
        :rtype: float
        """
        n = len(self.nums)
        if n % 2 == 0:
            left = int(n // 2 - 1)
            right = int(n // 2)
            return (self.nums[left] + self.nums[right]) / 2.0
        else:
            index = int((n - 1) // 2)
            return self.nums[index]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

# 双堆法（最小堆 + 最大堆）：本题最优解法，中位数的本质是在数组中间切一刀，使得满足以下条件
# 1.左半区的所有值 <= 右半区的所有值
# 2.左半区与右半区人数尽可能相等，或最多前者比后者多一个
# 3.只要能迅速获得左半区的最大数和右半区的最小数，就可以计算出来中位数
# 因此我们需要：一个数据结构，装左半区的数据，且能够O(1)获得左半区的最大值->最大堆
# 一个数据结构，装右半区的数据，且能够O(1)获得右半区的最小值->最小堆
# 这样，以上条件三就满足了，给定一个新数num，我们都先把它加入到左半区最大堆中，然后取出最大堆的堆顶（最大值），然后
# push进右半区的最小堆当中，这样我们始终能够满足条件一，然后若此时右半区数量大于左半区，我们就取出最小堆的堆顶，push进
# 左半区，直到满足条件二
# heapq只有最小堆，为了实现最大堆我们需要在push进堆时取负数，取出时再取回正数
import heapq
class MedianFinder(object):

    def __init__(self):
        self.min_heap = []
        self.max_heap = []


    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        # 无论来什么元素，先把其压入左半区（最大堆）
        heapq.heappush(self.max_heap,-num)
        # 为了防止左半区中的有数（其实就是新来的数），大于右半区的数
        # 我们直接取出最大堆堆顶元素，压入右半区（最小堆）
        poped_num = -heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap,poped_num)
        # 此时右半区是比左半区多了一个元素，我们再取出最小堆堆顶
        # 压入最大堆，这样满足条件二
        while len(self.min_heap) > len(self.max_heap):
            poped_num = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap,-poped_num)
        

    def findMedian(self): # O(1)
        """
        :rtype: float
        """
        # 如果左半区（最大堆）中的元素比右半区多，则说明现数据流是奇数，最大堆堆顶即为中位数
        # 注意：最大堆中的数取出时需取负数
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        # 若两个半区数量一样多，则各区堆顶元素取均值
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
# 时间复杂度addnum方法O(logN),最多五次pop或push，每次logN,因此是O(logN)findMedian()方法O(1)
# 空间复杂度O(N),所有数据均需存储在两个堆中