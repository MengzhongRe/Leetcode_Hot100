#
# @lc app=leetcode.cn id=56 lang=python
#
# [56] 合并区间
#

# @lc code=start
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # 贪心 + 排序 + 区间
        # 边界判断
        if not intervals:
            return []
        
        # 对intervals的各个子区间的左边界升序排序
        intervals.sort(key = lambda x: x[0]) # O(nlogn)
        # 初始化结果数组，将排序好的第一个区间加入到结果中
        result = []
        result.append(intervals[0])
        # 从第二个区间开始遍历
        for interval in intervals[1:]: # O(N)
            last_merged = result[-1] # 取出已经合并好的最后一个区间
            if interval[0] <= last_merged[1]: # 如果当前区间的左边界<=上一个区间的右边界,则可以合并上一个区间和这一个区间
                last_merged[1] = max(last_merged[1],interval[1]) # 合并后的区间的左边界就是上一个区间的左边界，
            # 而右边界则取决于这两个区间右边界的最大值 
            else: # 若当前区间的左边界大于上一个区间的右边界，则说明两者无法合并，直接加入到结果数组即可
                result.append(interval) 
        
        return result
# 时间复杂度O(nlogn),主要取决于排序算法
# 空间复杂度O(1)或O(n),取决于是否是原地排序     
# @lc code=end

