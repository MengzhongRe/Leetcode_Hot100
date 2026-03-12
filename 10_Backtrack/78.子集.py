#
# @lc app=leetcode.cn id=78 lang=python
#
# [78] 子集
#

# @lc code=start
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [] # 结果数组
        path = [] # 路径数组

        def backtrack(start_index): # 定义递归函数，参数为起始索引
            res.append(path[:]) # 浅拷贝

            for i in range(start_index,len(nums)):
                path.append(nums[i]) # 加入到路径中
                backtrack(i + 1) # 递归调用，起始索引加1
                path.pop() # 回溯，移除最后一个元素
        
        backtrack(0)
        return res
# 时间复杂度O（N*2**N）,子集大小为2**N,每次拷贝数组需要N的时间
# 空间复杂度O(N),递归调用栈最深N,path数组最大N      
# @lc code=end

