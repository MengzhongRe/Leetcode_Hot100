#
# @lc app=leetcode.cn id=46 lang=python
#
# [46] 全排列
#

# @lc code=start
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [] # 结果数组

        def backtrack(path): # 定义递归函数
            if len(path) == len(nums): # 递归终止条件：
                res.append(path[:]) # 浅拷贝
                return # 返回递归函数
            
            for num in nums: # 遍历原数组
                if num in path:
                    continue # 已经使用则跳过
                path.append(num) # 加入到路径中
                backtrack(path) # 递归进入下一层
                path.pop() # 撤销选组回溯
        
        backtrack([]) # 主逻辑：将空数组传入调用递归函数

        return res
# 时间复杂度O(N * N!),全排列的结果有N！，每次递归结束将path加入结果集需要N的时间
# 空间复杂度O(N),不算结果数组，递归调用栈最多需要N，path数组也需要N     
# @lc code=end

