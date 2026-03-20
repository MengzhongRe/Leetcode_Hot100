#
# @lc app=leetcode.cn id=20 lang=python
#
# [20] 有效的括号
#

# @lc code=start
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 剪枝：如果长度为奇数，则不可能合法
        if len(s) % 2 != 0:
            return False
        # 建立左右括号的哈希映射，方便实现O(1)查找比对
        mapping = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        # 初始化栈
        stack = []
        for char in s:
            # 用哈希表判断该符号是否是右括号 O(1)
            if char in mapping:
                # 如果栈非空则弹出栈顶元素否则先弹出一个假元素，下一步直接判断
                top_element = stack.pop() if stack else '#'
                # 匹配失败直接False(这里直接包含了栈为空的情况)
                if top_element != mapping[char]:
                    return False
            else: # 是左括号直接压入栈
                stack.append(char)

        return not stack
# 时间复杂度O(N)，最坏情况下需要遍历完整字符，每次遍历O(1)
# 空间复杂度O(N + |E|),哈希表和栈空间大小
# @lc code=end

