#
# @lc app=leetcode.cn id=763 lang=python
#
# [763] 划分字母区间
#

# @lc code=start
# 哈希表 + set集合统计：维护一个哈希表统计字符出现频次，再维护一个set集合包含当前子区间出现过且尚未遍历完的字符，遍历字符，如果字符不在set集合种
# 就加入进去，然后计数，然后由于我们已经遇到了一个该字符，就意味着后来的该字符出现的次数就 - 1，如果频率减为0，表明当前字符
# 已经不可能再在后面出现，因此在set种remove掉该字符，
# #此时判断set集合是否为空，如果为空表明当前子区间内的所有字符在后面都不会再出现，于是在当前位置切割，然后更新变量
from collections import defaultdict
class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        str_freq = defaultdict(int) # O(N)
        for char in s:
            str_freq[char] += 1

        res = []
        cur_count = 0
        cur_str = set()
        for char in s: # O(N)
            cur_count += 1
            if char not in cur_str:
                cur_str.add(char)
            str_freq[char] -= 1
            if str_freq[char] == 0:
                cur_str.remove(char)
                if not cur_str:
                    res.append(cur_count)
                    cur_count = 0
        return res
# 时间复杂度O(N),两次遍历，一次用哈希表统计字符出现频率，一次遍历分割子区间
# # 空间复杂度O(E),E是唯一字符集合的长度     
# @lc code=end
# 列表统计字符频次 + set集合：
class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        freq_count = [0] * 26
        for char in s:
            freq_count[ord(char) - 97] += 1

        res= []
        cur_count = 0
        cur_str = set()

        for char in s:
            cur_count += 1
            if char not in cur_str:
                cur_str.add(char)
            freq_count[ord(char) - 97] -= 1
            if freq_count[ord(char) - 97] == 0:
                cur_str.remove(char)
                if not cur_str:
                    res.append(cur_count)
                    cur_count = 0
        
        return res
# 时间复杂度O(N),两次遍历，一次用列表统计字符出现频率，一次遍历分割子区间
# # 空间复杂度O(E),E是唯一字符集合的长度 

# 哈希表统计字符最后一次出现位置 + 结界维护：这道题目本质上“最远边界问题”，其实是55题目跳跃游戏的翻版。假设当前片段（结界）包含字符'a',而字符'a'在字符串中
# 出现的最后一个位置在索引8,则意味着当前片段至少也要延伸到索引8。此外，我们别忘了这个片段里面可能还有
# 其他的字符，这些字符有其他的边界，也就是当前片段的边界end = max(旧end,8)，也就是
# 跳跃游戏的max_pos = max(max_pos,i + nums[i]) 当我们遍历过程中 i == end,意味着
# 当前片段的所有字符的最远出现位置都在当前end = i以内,也就是之后不会再出现了，就可以在当前i位置切割了。
# 记录每个字符的“最远射程”：遍历一次字符串，用字典或数组记录每个字符最后一次出现的索引。
# 遍历刷新结界：维护一个当前片段的极限边界 end（这就相当于跳跃游戏里的 end 或 max_pos）。
# 每走到一个字符，就看看它的最远射程在哪，试图去扩大当前的结界：end = max(end, 字符的最后出现索引)。
# 触发切割：当我们一直走，走到 i == end 时，说明什么？说明在这个结界里，
# 所有的字符的最远射程都没有超出这个边界，完美切割

from collections import defaultdict
class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        # 维护一个哈希表用于记录每个字符char最后一次出现的索引位置i
        char_freq = defaultdict(int)
        for i,char in enumerate(s):
            char_freq[char] = i
        # 也可以用字典推导式快速建立
        # char_freq = {char: i for i,char in enumerate(s)}
        res = []
        cur_count = 0
        end = 0 # 当前子区间的最远边界

        for i,char in enumerate(s):
            cur_count += 1
            end = max(end,char_freq[char]) # 更新边界
            if i == end: # 如果已经走到了最远边界
                res.append(cur_count)
                cur_count = 0
        
        return res
# 时间复杂度O(N),两次遍历，一次用哈希表统计每个唯一字符最后一次出现的下标位置，一次遍历分割子区间
# 空间复杂度O(E),E是唯一字符集合的长度，该版本比以上统计字符频率的版本所需空间小，因为不需要维护set集合



        