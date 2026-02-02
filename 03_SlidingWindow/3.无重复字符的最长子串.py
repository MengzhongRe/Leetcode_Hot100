#
# @lc app=leetcode.cn id=3 lang=python
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s) # 边界判断
        if n <= 1:
            return n
        
        # 用哈希表记录字符上次出现的位置
        dic = {}
        left = 0 # 用滑动窗口的左边界表示当前不重复子串的起始位置
        max_length = 0

        # 右指针遍历字符串，表示当前滑动窗口（当前不重复子串）的结束位置
        for right,char in enumerate(s):
            if char in dic and dic[char] >= left:# 如果字符已经出现过且在当前窗口内
                left = dic[char] + 1 # 更新左指针到上次出现位置的下一个位置,这样当前窗口就一定不包含重复字符
            dic[char] = right # 无论如何都更新字符最后一次出现的位置
            max_length = max(max_length,right-left+1)
        
        return max_length

# 时间复杂度O(N),N为字符串长度,每个字符被右指针访问一次,左指针最多也被访问N次
# 空间复杂度O(min(M,N)),M为字符集大小,N为字符串长度
        
# @lc code=end

