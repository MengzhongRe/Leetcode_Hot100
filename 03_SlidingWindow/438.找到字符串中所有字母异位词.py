#
# @lc app=leetcode.cn id=438 lang=python
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        s_len,p_len = len(s),len(p)
        # 若s长度小于p长度，则不可能存在异位词
        if s_len < p_len:
            return []
        
        count = [0] * 26 # 记录字母出现次数差值
        res = [] # 存储结果数组
        # 遍历p和s的前p_len个字符，统计字符频次差值 O(m),m为p的长度
        for i in range(p_len):
            count[ord(s[i]) - ord('a')] += 1 
            count[ord(p[i]) - ord('a')] -= 1
        # 统计不同字符频次的字符种类数量 O(E),E为字符集大小
        differ = [c != 0 for c in count].count(True)

        if differ == 0:
            res.append(0)
        # 使用滑动窗口统计每种字符出现的频次差值，O(n-m),n为s的长度,m为p的长度
        for i in range(s_len - p_len):
            left_char = ord(s[i]) - ord('a')
            if count[left_char] == 1:
                differ -= 1
            elif count[left_char] == 0:
                differ += 1
            count[left_char] -= 1

            right_char = ord(s[i + p_len]) - ord('a')
            if count[right_char] == -1:
                differ -= 1
            elif count[right_char] == 0:
                differ += 1
            count[right_char] += 1

            if differ == 0:
                res.append(i + 1)
        
        return res
# 时间复杂度:O(N),N为字符串s的长度
# 空间复杂度:O(E),E为字符集大小
# @lc code=end

