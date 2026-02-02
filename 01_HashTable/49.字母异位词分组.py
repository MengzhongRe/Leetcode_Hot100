#
# @lc app=leetcode.cn id=49 lang=python
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        group_dict = {} # 创建空的哈希表 1
        
        for s in strs: # 需要遍历N个字符串，n次
            char_count = {} # 创建空的哈希表 1
            for char in s: # 设最大字符串长度为k,则最多需要遍历k次
                char_count[char] = char_count.get(char,0) + 1 # 哈希表核心操作 1
            count_key = tuple(sorted(char_count.items())) # sorted函数涉及字符排序，排序算法一般为mlogm,其中
            # m为不同字符的数量，由于字符串都是小写英文字母，故m <= 26,故可以看做O(1)

            if count_key in group_dict: # 哈希表判断 O(1)
                group_dict[count_key].append(s) # 哈希表改值 O(1)
            else:
                group_dict[count_key] = [s] # 哈希表改值 O(1)
        
        return list(group_dict.values())
# 时间复杂度为O(nk)
#  空间复杂度为O(nk)
# @lc code=end
# 字符计数的优化版，用数组来统计。因为数组天然有序，没有sorted的排序开销，且数组的下标访问自增都是O(1),
# 虽然字典也是O(1),但字典还需要计算哈希函数，且可能存在哈希冲突，实际执行效率更低
import collections

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # 我们直接用colletions库中的默认字典，该字典可以实现：
        # 当访问字典中不存在的Key0时不会报错，而是直接初始化该key,value为空的list对象
        group_dict = collections.defaultdict(list) # 1

        for s in strs: # 需要遍历n个字符串
            count = [0] * 26 # 
            for char in s: # O(k)
                count[ord(char) - ord('a')] += 1 
            # PYTHON中不能将列表对象作为字典的key,因为列表式可变对象，但是元祖可以，所以我们把它转换为元祖
            key = tuple(count)
            group_dict[key].append(s) 
        
        return list(group_dict.values())
# 时间复杂度O(nk)
# 空间复杂度O(nk)