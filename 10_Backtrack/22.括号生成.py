#
# @lc app=leetcode.cn id=22 lang=python
#
# [22] 括号生成
#

# @lc code=start
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        path = []

        def backtrack(left_count,right_count):
            if len(path) == 2 * n:
                res.append(''.join(path))
                return
            
            if left_count < n:
                path.append('(')
                backtrack(left_count + 1,right_count)
                path.pop()
            
            if right_count < left_count:
                path.append(')')
                backtrack(left_count,right_count + 1)
                path.pop()
        
        backtrack(0,0)
        return res 
# @lc code=end

### ⏱️ 复杂度分析 (数学彩蛋)


# *   **时间复杂度**：$\mathcal{O}\left(\frac{4^n}{\sqrt{n}}\right)$。
#     *   合法括号组合的数量，在数学上严格等于第 $n$ 个**卡特兰数**。
#     *   卡特兰数的渐进增长级别就是 $\frac{4^n}{n\sqrt{n}}$。我们在每个有效组合上花费 $O(n)$ 的时间（无论数组拼接还是字符串拼接），相乘之后时间复杂度就是 $\mathcal{O}\left(\frac{4^n}{\sqrt{n}}\right)$。
#     *   *面试话术*：“这道题的合法结果数量是第 $n$ 个卡特兰数，由于我们做了极速剪枝，没有进行任何无效搜索，所以时间复杂度与卡特兰数的渐进界相关，约为 $\mathcal{O}(\frac{4^n}{\sqrt{n}})$。”
# *   **空间复杂度**：$\mathcal{O}(n)$。
#     *   空间开销完全取决于递归调用栈的最大深度，也就是拼出完整字符串的长度 $2n$。去掉常数项后，空间复杂度为 $\mathcal{O}(n)$。


# 面试炫技版：利用 Python 字符串的“不可变性”隐式回溯

# 在 Python 中，处理字符串有一个极其优雅的写法。
# 因为字符串是**不可变对象（Immutable）**，当我们执行 `path_str + "("` 时，实际上是在内存里生成了一个**全新的字符串**传给下一层，而当前层的 `path_str` 根本没有被改变！

# 这就意味着：**我们连 `path.pop()` 撤销选择这一步都省了！**（系统在返回上一层时，自动用回了上一层的那个老字符串）。

# 这也是很多大神写算法题时最爱用的写法，代码极其短小精悍：
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []

        def backtrack(left_count,right_count,current_str):
            if len(current_str) == 2 * n:
                res.append(current_str)
                return
            
            if left_count < n:
                backtrack(left_count + 1,right_count,current_str + '(')
            
            if right_count < left_count:
                backtrack(left_count,right_count + 1,current_str + ')')
        
        backtrack(0,0,'')
        return res
