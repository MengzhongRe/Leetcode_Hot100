#
# @lc app=leetcode.cn id=131 lang=python
#
# [131] 分割回文串
#

# @lc code=start
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        path = []

        def ispalidrome(str): # 定义辅助函数判断字符串是否是回文串
            return str == str[::-1] # Python字符切片操作把字符串反转，需要O(N)的时间和额外空间，因为回开辟新数组

        def backtrack(start_index): # start_index表示剩余需要切的起始位置
            if start_index == len(s):
                res.append(path[:])
                return
            
            for i in range(start_index,len(s)): # i表示真正落刀的位置
                sub_str = s[start_index:i + 1] # 当前所切出来的片段索引(start_index,i)，包含i

                if ispalidrome(sub_str): # 如果当前切出来的片段是回文串，才真正切，继续切下一段
                    path.append(sub_str) # 加入当前结果集
                    backtrack(i + 1) # 从当前所切位置的下一个位置开始切下一段
                    path.pop() # 回退
                else:
                    continue # 当前切出来的片段不是回文串，继续尝试从下一个位置下刀
        
        backtrack(0)
        return res   
# @lc code=end

### ⏱️ 复杂度分析

# 这道题的复杂度分析也是非常有意思的，我们按最坏情况来推导。

# *   **时间复杂度**：$\mathcal{O}(N \times 2^N)$。
#     *   $N$ 是字符串的长度。
#     *   **最坏情况**：字符串里的字符全是一样的，比如 `"aaaa"`。这意味着你**不管怎么切，切出来的必定都是回文串**。
#     *   长度为 $N$ 的字符串，中间有 $N-1$ 个空隙。每个空隙你都可以选择“切”或者“不切”。所以切法的总组合数是 $2^{N-1}$ 种。
#     *   对于每一种合法的切法，我们要把它装进 `path[:]` 中，耗时 $O(N)$。
#     *   所以总时间复杂度是 $\mathcal{O}(N \times 2^N)$。
# *   **空间复杂度**：$\mathcal{O}(N)$（辅助空间）。
#     *   空间消耗依然是我们熟悉的两位老朋友：**递归调用栈的最深深度**（最多切 $N$ 刀，深度为 $N$），以及 **`path` 数组的最大长度**（最多装 $N$ 个单字符）。两者都是 $\mathcal{O}(N)$。

### 总结归纳

# 你看，131 题虽然披着“字符串、回文”的外衣，剥开一看，其实就是一个**加上了特定过滤条件（必须是回文）的子集问题**！

# 1. **组合/子集问题（无条件）**：随便挑，只要 `startIndex` 往后走就行。
# 2. **组合总和问题（过滤条件 = sum）**：挑出来的总和必须等于 Target，大了就剪枝。
# 3. **分割回文串问题（过滤条件 = is_palindrome）**：切出来的子串必须是回文串，不是就剪枝。