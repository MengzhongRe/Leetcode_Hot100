#
# @lc app=leetcode.cn id=76 lang=python
#
# [76] 最小覆盖子串
#

# @lc code=start
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        from collections import defaultdict

        need = defaultdict(int)
        # 用哈希表统计t中每个字符的需求数量（字符频次）
        for char in t: # O（N）
            need[char] += 1
        window = defaultdict(int)
        # 初始化滑动窗口左右指针
        left,right = 0,0
        start,min_len = 0,float('inf') # 初始化最小窗口子串起始索引和其长度
        valid = 0 # 用来记录窗口中满足need条件的字符种类数量

        # 每个字符最多被左右指针各遍历一次，所以是O(2m)
        while right < len(s):
            curr_char = s[right]
            right += 1
            # 更新窗口内数据
            if curr_char in need:
                window[curr_char] += 1
                # 判断该字符数量是否已经匹配，若匹配则直接valid +1
                if window[curr_char] == need[curr_char]:
                    valid += 1
            
            # 只要当前窗口是可行窗口即valid = need键的长度，就收缩窗口
            while valid == len(need):
                # 更新最小子串的起始索引和长度
                if right - left < min_len:
                    start = left
                    min_len = right - left
                # 获取即将被移除窗口的左边界值
                curr_char = s[left]
                left += 1 # 移动左边界，收缩窗口
                # 如果curr_cahr 是need需要的元素，即t中出现过的元素，则更新窗口哈希表
                # 如果curr_char 不在need中，则我们根本不需要关心。
                if curr_char in need:
                    if window[curr_char] == need[curr_char]: # 只要移除之刚刚好供给 = 需求，则说明移除后供给 < 需求
                        valid -= 1 # valid需要 - 1
                    window[curr_char] -= 1 # 无论供给是否等于需求，由于curr_char将被移除窗口，所以需要 - 1
        
        return '' if min_len == float('inf') else s[start:start + min_len]
# 时间复杂度O(m+n)
# 空间复杂度O（E）,E为字符集大小
# @lc code=end

