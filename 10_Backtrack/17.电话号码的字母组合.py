#
# @lc app=leetcode.cn id=17 lang=python
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # 定义数字到字符串的映射表（哈希表）
        digit_to_letter = {
            '2':'abc','3':'def','4':'ghi',
            '5':'jkl','6':'mno','7':'pqrs',
            '8':'tuv','9':'wxyz',
        }
        res = [] # 结果数组
        path = [] # 临时结果数组，用于递归存储中间字符结果

        def backtrack(i):
            if len(path) == len(digits):
                res.append(''.join(path)) # 将字符列表拼接为字符串O(m + n)
                return # 返回当层递归函数
            
            digit = digits[i] # 字符串可以直接通过类似于数组的方式索引
            letters = digit_to_letter[digit] 
            for letter in letters:  # 迭代该数字代表的字符序列
                path.append(letter) # 将该字符加入路径
                backtrack(i + 1) # 进入下一层即下一个数字的递归
                path.pop() # 回溯
        # 主逻辑：从第0层开始递归
        backtrack(0)
        return res
# 时间复杂度O(3**m * 4**n),这是该题目的理论下界，因为结果数组的长度就是3**m * 4**n，操作中只有join操作需要O(m + n),其他都是O(1)，回溯算法刚好每个结果递归了一次没有冗余
# 空间复杂度O(m + n),递归调用栈最深为digits长度，即m + n，path最长也为m + n      
# @lc code=end

