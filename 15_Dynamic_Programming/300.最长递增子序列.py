#
# @lc app=leetcode.cn id=300 lang=python
#
# [300] 最长递增子序列
#

# @lc code=start
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [1] * n

        for i in range(1,n):
            for j in range(0,i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i],dp[j] + 1)

        return max(dp)
# @lc code=end
import bisect
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tails = []

        for num in nums:
            idx = bisect.bisect_left(tails,num)
            if idx == len(tails):
                tails.append(num)
            else:
                tails[idx] = num
            
        return len(tails)

