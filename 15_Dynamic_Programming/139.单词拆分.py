#
# @lc app=leetcode.cn id=139 lang=python
#
# [139] 单词拆分
#

# @lc code=start

# 动态规划-遍历字典法：这是一道完全背包问题，字典中的单词可以重复选取，且由于时拼接单词成字符串，本质上是顺序敏感的，例如
# 'applepen',必须先遍历到'apple',再考虑'pen'才可以拼接成功，而如果我们是外层遍历物品（字典），内层遍历背包，即字符串长度
# 则由于字典取词的顺序完全是固定的，因而如果原字典顺序是['pen','apple']，我们则完全拼不出来，所以我们应该外层遍历背包，
# 内层遍历物品。dp数组可以定义为dp[i],表示字符串s的前i个字符能否由字典中的单词拼出来，显而易见，这应该是个布尔数组。
# 考虑第j个单词，如果s[i - len(worddict[j]):i] == worddict[j]并且dp[i - len(worddict[j])] == True，那么dp[i]就是
# True,之后的就可以不用遍历了！
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for j in range(1,n + 1):
            for word in wordDict:
                if j >= len(word):
                    diff = j - len(word)
                    # 注意：数组切片需要O(L)的时间
                    # 注意：这里我们利用到了python的and短路机制：Python中对and判断是从左到右的，一旦左侧分支为false
                    # python知道整个合取一定为False,因而直接停止判断。又因为数组索引操作是O(1)的，我们左侧写dp[diff]
                    # 可以直接判断出真假，在为假的情况下避免了后续的数组切片O(L)操作
                    if dp[diff] and s[diff:j] == word:
                    # 剪枝：一旦dp[j] = True,就不需要再遍历后续单词了，直接break掉当前内层循环
                        dp[j] = True
                        break    
        return dp[n]    # 返回最后一个数布尔变量
# 时间复杂度O(N * M * L ),N是s的长度,M是worddict中的word数量，L是word的平均长度
# 外层循环N次，内层循环最多M次，s[diff:j] == word，该切片比较需要O(L)的时间，所以综合来看是N * M * L
# 空间复杂度O(N),只需要维护一个长度为N + 1的布尔动态规划数组
        
# @lc code=end
# 动态规划-遍历断点:
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # 把原单词数组转换为哈希表，方便O(1)查找
        word_set = set(wordDict)    # O(M * L),M是字典单词数量，L是单词平均长度
        n = len(s)
        dp = [False] * (n + 1)  # 初始化dp数组
        dp[0] = True
        max_len = max([len(w) for w in wordDict]) if wordDict else 0    # 求原字典单词长度最大值，方便后续剪枝
        # 外层遍历背包
        for i in range(1,n + 1): #O(N)
            start = max(0,i - max_len)
            # 内层遍历切分点
            for j in range(start,i):    # O(max_len)
                if dp[j] and s[j:i] in word_set:    # O(L)
                    dp[i] = True
                    break
        return dp[n]
# 时间复杂度O(N * max_len * L)
# 空间复杂度O(N+ M*L)