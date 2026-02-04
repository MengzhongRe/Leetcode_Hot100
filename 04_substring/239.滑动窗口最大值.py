#
# @lc app=leetcode.cn id=239 lang=python
#
# [239] 滑动窗口最大值
#

# @lc code=start
from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        dq = deque()
        max_length = []

        for i in range(n):
            # 移除滑动窗口外的元素
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
            dq.append(i)
            # 移除不在窗口中的元素
            while dq[0] <= i -k:
                dq.popleft()
            # 记录当前窗口的最大值
            if i >= k -1:
                max_length.append(nums[dq[0]])
        
        return max_length

# 时间复杂度:O(N),N为数组nums的长度
# 空间复杂度:O(K),K为滑动窗口的大小  
# @lc code=end
# 暴力枚举法:直接列举所有可能的滑动窗口，计算其最大值
# 时间复杂度:O(N*K),N为数组nums的长度,K为滑动窗口的大小
# 空间复杂度:O(1)
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        max_length = []
        n = len(nums)
        for i in range(n - k + 1):
            max_length.append(max(nums[i:i + k]))
        
        return max_length