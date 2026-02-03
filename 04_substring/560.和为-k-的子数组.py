#
# @lc app=leetcode.cn id=560 lang=python
#
# [560] 和为 K 的子数组
#

# @lc code=start
# 前缀和 + 哈希表
# 时间复杂度:O(N),N为数组nums的长度
# 空间复杂度:O(N),N为数组nums的长度
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 初始化哈希表，存储前缀和及其出现次数
        pre_sum_map = {0:1}
        pre_sum = 0
        count = 0
        # 遍历每一个数
        for num in nums:
            pre_sum += num # 计算每一个前缀和
            if (pre_sum - k) in pre_sum_map:# 若pre_sum - k存在于哈希表中，说明存在一个子数组的和为k,且该数组为[i,j]
                count += pre_sum_map[pre_sum - k] # 累加该前缀和出现的次数
            # 将当前前缀和加入哈希表
            pre_sum_map[pre_sum] = pre_sum_map.get(pre_sum,0) + 1
        
        return count
        
        
# @lc code=end
# 暴力枚举法，直接列举所有可能的子数组:[i,j],计算其和是否等于k
# 时间复杂度:O(N^2),N为数组nums的长度
# 空间复杂度:O(1)
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        count = 0
        for i in range(n):
            current_sum = 0
            for j in range(i,n):
                current_sum += nums[j]
                if current_sum == k:
                    count += 1
        
        return count