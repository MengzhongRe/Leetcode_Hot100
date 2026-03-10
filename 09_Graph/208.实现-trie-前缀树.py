#
# @lc app=leetcode.cn id=208 lang=python
#
# [208] 实现 Trie (前缀树)
#

# @lc code=start
class TireNode(object):
    def __init__(self):
        # children 是一个哈希表。键是字符 (比如 'a')，值是下一个 TrieNode
        self.children = {}
        self.is_end = False
class Trie(object):

    def __init__(self):
        self.root = TireNode() # 根节点不存储任何字符

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        # 无论什么时候都从根节点开始搜索
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TireNode()
            node = node.children[char]
        node.is_end = True # 最后一个字符的节点标记为单词结尾
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end # 只有当最后一个字符的节点标记为单词结尾时，才返回True
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True # 只要能找到前缀的最后一个字符的节点，就返回True
# 时间复杂度O(L),L是所操作的字符串的长度，查询时间与词库的大小N绝对无关
# 空间复杂度O(N * L),N为字符串数量，L为所有字符串平均长度，最坏情况下所字符串之间都没有公共前缀，则需要N * L 
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

