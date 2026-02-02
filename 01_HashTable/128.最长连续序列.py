#
# @lc app=leetcode.cn id=128 lang=python
#
# [128] 最长连续序列
#

# @lc code=start
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 处理边界条件
        if not nums:
            return 0
        
        # 将数组去重转化为O(1)查找时间复杂度的哈希表（集合）
        nums_ord = set(nums) # O(n)
        # 用一个全局变量存储截至目前为止的最大长度，不需要最后再统计了
        max_length = 0

        for num in nums_ord: # O(n)
            # 关键：只从序列开头统计，防止重复计数，例如[55,1,2,3]
            # 访问到2时，2不是序列开头直接跳过
            if num - 1 not in nums_ord: # O(1)，如果上一个数不在集合中，就是序列开头
                current_num = num # O(1) 
                current_len = 1 # O(1)

                # 步骤3：找连续的下一个数，直到找不到
                while current_num + 1 in nums_ord: # O(1)
                    current_num += 1 # O(1)
                    current_len += 1 # O(1)
                
                # 更新最大长度
                max_length = max(max_length,current_len) # O(1)
        
        return max_length
# 时间复杂度:O(n)
# 空间复杂度:O(n)

        
# @lc code=end

