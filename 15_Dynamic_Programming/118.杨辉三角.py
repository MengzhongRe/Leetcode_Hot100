#
# @lc app=leetcode.cn id=118 lang=python
#
# [118] 杨辉三角
#

# @lc code=start
# 动态规划 + 两行滚动数组：考虑每一行有n个数字，收尾数字为1,考虑1<= i < n - 1,则新dp[i] = 旧dp[i - 1] + 旧dp[i],这就是递推公式，显然循环方向是从上到下，从左到右，
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        
        prev = []
        for i in range(numRows):
            cur = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    cur.append(1)
                else:
                    cur.append(prev[j - 1] + prev[j])
            res.append(cur)
            prev = cur
        return res
# 时间复杂度O(N^2),N行，每行有1,2,3,...N个数字，其实就是等差数列求和SN = N(N + 1)/2,也就是O(N^2)
# 空间复杂度o(N),最大辅助空间cur就是最后一行的数量N
# @lc code=end

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        cur = [0]

        for i in range(numRows):
            left_up = cur[0]
            for j in range(i + 1):  
                if j == 0:
                    cur[j] = 1
                elif j == i:
                    cur.append(1)
                else:
                    next_left_up = cur[j]
                    cur[j] = left_up + cur[j]
                    left_up = next_left_up
            res.append(cur[:]) # 由于列表是可变对象，所以必须先进行浅拷贝，否则存入的只是对该列表对象的内存指针，其内容
            # 会随着后面cur数组变化而改变
        return res

# 逆序遍历一维数组：递推公式是dp[j] = dp[j - 1] + dp[j],正序遍历时dp[j]显然是旧值，但是dp[j - 1]已经被更新污染了。但是如果我们倒序遍历，dp[j - 1]显然还没有被更新，所以我们可以
# 直接dp[j - 1]。倒序时我们忽略首尾即i和0，直接在每一行更新前先加入一个1,后续正常更新和浅拷贝即可。     
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        cur = []

        for i in range(numRows):
            cur.append(1)
            for j in range(i - 1,0,-1):  # 倒序遍历，忽略首尾(i,0)
                cur[j] = cur[j - 1] + cur[j] # 直接更新，不用临时变量
            res.append(cur[:]) # 列表是可变对象，注意浅拷贝
        return res