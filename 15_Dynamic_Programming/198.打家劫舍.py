#
# @lc app=leetcode.cn id=198 lang=python
#
# [198] 打家劫舍
#

# @lc code=start
# 动态规划 滚动变量更新：考虑我们已经偷到了第i个房间，分两种情况：1.偷，则第i - 1个房间不能偷，此时的收益就是dp[i - 2] + nums[i].2.不偷，则我们可以考虑偷第i - 1个房间，但是也可以不偷，取决于哪个
# 更划算，这个值就是dp[i - 1]。综合以上两种情况，我们取最大值即可dp[i] = max(dp[i - 2] + nums[i],dp[i - 1])。由此可见我们只需要考虑前两个变量即可，考虑滚动变量优化空间，同时遍历顺序就是从左向右
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if len(nums) < 3:
            return max(nums)
        
        prev,cur = nums[0],max(nums[0],nums[1])
        for i in range(2,n):
            tmp = cur
            cur = max(prev + nums[i],cur)
            prev = tmp
        
        return cur 
# 时间复杂度o(n),一次遍历
# 空间复杂度o(1)   
# @lc code=end

# 可以虚拟初始化动态规划数组,可以省略长度判断
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev,cur = 0,0

        for num in nums:
            tmp = cur
            cur = max(prev + num,cur)
            prev = tmp
        return cur