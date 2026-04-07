#
# @lc app=leetcode.cn id=72 lang=python
#
# [72] 编辑距离
#

# @lc code=start

# 二维动态规划：这是一道非常经典的双序列型动态规划题目。题目探讨的是两个字符串之间的编辑关系。我们自然而然的可以定义
# 动态规划数组如下dp[i][j] 为word1前i个字符转换为word2前j个字符的最短编辑距离。显然答案是dp[m][n]。考虑dp[i][j]，
# 如果word1[i] == word2[j]，则由于最后这两个字符相等，因此意味着我们可以不用任何操作即可从dp[i - 1][j - 1]的次数
# 使得二者相等，因此有dp[i][j] = dp[i - 1][j - 1]。若word1[i] != word2[j]，则意味着我们有三种操作方式可以使
# 二者相等。
# 1)假设我们已经使的前word1的i-1和word2的前j - 1个字符相等，则我们仅需替换最后一个word1[i]为word2[j]即可
# 此时dp[i][j] = dp[i -1][j - 1] + 1
# 2)假设我们已经使的word1的前i - 1个字符和word2的前j个字符相等，则意味着我们仅需删除word1[i]这个字符，即可使得二者相等
# 因此dp[i][j] = dp[i - 1][j] + 1
# 3)假设我们已经使的word1的前i个字符和word2的前j - 1个字符相等，则意味着我们仅需在word1[i - 1]之后插入一个word2[j]即可
# 使得二者相等，此时dp[i][j - 1] + 1
# 综上我们取三者的最小值即可
# 根据递推公式关系我们知道遍历顺序应该是从上到下，从左到右，同时为了避免判断i - 1>= 0或j - 1>= 0，我们初始化二维数组时
# 需要多初始化一行一列。同时在遍历前最好先初始化首行首列。dp[0][j]意味着将空字符转换为word2前j个字符的最小编辑次数，那么显然
# 就是增加这j个字符即可，也就是需要j次。首列的初始化同理
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        m,n = len(word1),len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for j in range(1,n + 1):
            dp[0][j] = j
        
        for i in range(1,m + 1):
            dp[i][0] = i
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1],dp[i - 1][j],dp[i][j - 1]) + 1
        
        return dp[-1][-1]
# 时间复杂度O(m * n),外层m次，内层n次循环
# 空间复杂度O(m * n),我们实例化了一个m * n的二维动态规划数组
# @lc code=end
# 一维动态规划滚动数组优化：注意到动态规划状态转移方程依赖于三个值：左上，正上和正左，一维数组滚动更新时，正上方的
# 值刚好作为旧值dp[i - 1][j]保留，左方的dp[i][j - 1]也刚好时更新过的，但是左上方dp[i - 1][j - 1]因为已经被下一行
# 的dp[i][j - 1]更新过了，因此我们必须使用临时变量来保存该旧值。策略为：首先初始化dp数组的首行:dp = list(range(n + 1))
# 然后由于第一行已经被正确初始化，我们直接从第二行开始遍历，每次遍历到新行时，我们需要先用一个临时变量left_up保存上一行的
# 第一列的旧值，因为新行的第二列的值的更新需要它，在此之后我们需要把dp[0]更新为i。此时首列也已经被我们初始化，因此我们还是
# 从第二列开始更新。更新前，我们需要先用next_left_up来保存更新前的dp[j],因为一旦dp[j]更新完毕，则我们就无法获取其旧值
# 但是dp[j + 1]的更新需要其旧值。剩下的按照动态规划转移公式赋值。在更新完dp[j]后，旧的dp[j - 1]的值也就是left_up已经不需要
# 我们直接用dp[j]的旧值覆写left_up,作为下一次更新dp[j + 1]时的左上角值，紧接着开始下一列的循环。
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # 在本题目中，word1删除一个字符 <=> word2插入一个字符；word1替换一个字符 <=> word2替换一个字符
        # 因此word1和word2的操作完全是对称的，利用这种特性，我们可以交换word1与word2，使得短的那个永远是
        # word2，这样我们就可以用最小的额外空间完成
        if len(word1) < len(word2):
            word1,word2 = word2,word1
        
        m,n = len(word1),len(word2)

        dp = list(range(n + 1))

        for i in range(1, m + 1):
            # 保存上一行的首列值，作为下一行dp[1]的左上角的值
            left_up = dp[0]
            # 更新dp[0] 为下一行首列的值
            dp[0] = i
            for j in range(1, n + 1):
                # 用临时变量保存第j列的旧值，在dp[j]更新之后就无法访问
                next_left_up = dp[j]
                if word1[i -1] == word2[j -1]:
                    dp[j] = left_up
                else:
                    dp[j] = min(left_up,dp[j],dp[j - 1]) + 1
                left_up = next_left_up

        return dp[-1]
# 时间复杂度O(m * n),外层m次，内层n次循环
# 空间复杂度O(min(m,n)),空间复杂度取决于最小字符串的长度