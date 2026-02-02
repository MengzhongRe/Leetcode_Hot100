#
# @lc app=leetcode.cn id=1 lang=python
#
# [1] 两数之和
#
# 用哈希表存储Num上一次出现的索引，用空间换时间 
# @lc code=start

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {} # 哈希表创建O(1)
        for i,num in enumerate(nums): # 最多N次
            if (target - num) in dic: # 一次减法 + 一次哈希表查表，最好、平均(O1)，最坏O(N),哈希冲突极端情况
                return [dic[target - num],i]
            else:
                dic[num] = i # 哈希表增加，更改都是平均/最好O(1)，最坏O(N)

# 时间复杂度为O(N)
# 空间复杂度O(N)

        
# @lc code=end

