#
# @lc app=leetcode.cn id=394 lang=python
#
# [394] 字符串解码
#

# @lc code=start
# 本题是典型的括号匹配问题，且带有明显的嵌套结构，需要用元组存储和读取状态信息，栈就是最好的数据结构
# 道题最大的难点在于**“嵌套（Nested）”**：你正在解析外面的 3[a...]，突然里面又冒出来一个 2[c]。
# 这就好比你正在玩一个游戏（主线任务），突然接到了一个副本任务。你必须：
# 保存当前主线任务的进度（存盘）。
# 进入副本，打完副本（解码内部字符串）。
# 读取刚才的存盘进度，把副本的奖励带回到主线任务中继续。
# 在计算机科学中，“保存现场 →→进入深层 →→ 返回现场” 的完美数据结构，就是栈（Stack）！

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 我们用一个栈存储当前嵌套层的字符串res和乘数multi,形式为[(last_res,cur_multi)]
        stack = [] # 栈，用来存档
        res = '' # 当前正在拼凑的字符串
        multi = 0 # 当前嵌套层乘数
        # 遍历字符
        for char in s:
            if char.isdigit(): # 如果字符，需要转换为整数后和之前的乘数进行拼接
                multi = multi * 10 + int(char)      
            elif char == '[': # 左括号，将(res,multi)元组压入栈中存档
                stack.append((res,multi))
                # 进入下一层嵌套，两个变量重置
                res = ''
                multi = 0
            elif char == ']': # 右括号，读取栈顶存档
                last_res,cur_multi = stack.pop()
                # 读完后，需要把当前副本字符串乘以倍数再拼接到历史字符串后面
                res = last_res + cur_multi * res
            else:# 如果是字符直接拼接到当前字符串后面
                res += char
        
        return res
# 时间复杂度o(N),准确来说等于解码后的字符串长度
# 空间复杂度O(N),不考虑返回结果res,主要取决于栈的深度，最坏情况下为N
# @lc code=end
# 递归解法:递归的本质就是系统底层的调用栈，因此本题也可以通过递归解决，当遇到[时，进入下一层递归，当遇到]是返回该层结果和检索位置
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 定义递归函数，传入参数为目前检索字符串的下标
        def dfs(i):
            # 初始化本层的拼接字符串
            res = ''
            multi = 0 # 本层乘数
            # 迭代
            while i < len(s):
                if s[i].isdigit():
                    multi = multi * 10 + int(s[i])
                # 遇到[，进入下一层循环，返回下一层拼接字符串 与 结束索引
                elif s[i] == '[':
                    sub_str,i = dfs(i + 1)
                    # 将下一层的字符串乘上本层乘数拼接在字符串后面
                    res += multi * sub_str
                    # 本层乘数用过了重置
                    multi = 0
                # 递归函数遇到]直接结束本层递归，返回本层字符串和结束为止
                elif s[i] == ']':
                    return res,i
                else:
                    res += s[i]
                # 无论如何，一次迭代结束索引后移一位
                i += 1
            # 最外层（也就是第一层）递归函数不会触发以上分支，需要最后返回res即拼接字符串
            return res
        return dfs(0)