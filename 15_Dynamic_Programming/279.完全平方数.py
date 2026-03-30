#
# @lc app=leetcode.cn id=279 lang=python
#
# [279] 完全平方数
#

# @lc code=start
# 动态规划数组:定义动态规划数组dp[i]为,和为数字i的完全平方数的最小个数，则递推公式为对于任意的0<=i<=n
# 我们遍历所有的小于i的完全平方数j*j,我们尝试用j*j这个完全平方数和其他完全平方数求和n,此时需要的
# 最小完全平方数即为dp[i - j*j] + 1，我们取该值和旧dp[i]的最小值即可，因此递推公式为
# dp[i] = min(dp[i],dp[i - j*j] + 1),对于任意的j由递推公式知，我们需要从小到大遍历，由动态规划数组定义知
# 最终的结果为dp[n]，
import math
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 初始化 dp 数组，容量为 n，默认全为正无穷
        dp = [float('inf')] * (n + 1)
        dp[0] = 0 # 基础

        for i in range(1,n + 1):    # dp[0]已求出，跳过
            max_j = int(math.sqrt(i)) # 对n求根号，刺此为dp[n]的下界情形
            for j in range(1,max_j + 1):    # 0不是完全平方数，不需要遍历
                square = j * j  # 计算完全平方数
                dp[i] = min(dp[i],dp[i - square] + 1)   # 更新当前dp[i]
        
        return dp[n]
# 时间复杂度O(N*N^1/2)，从1遍历到n，每次最多需要遍历n^1/2次
# 空间复杂度O(N),dp数组为n

# @lc code=end
# 【完全背包问题 降维解析】
# 1. 模型映射：背包最大容量为 n；物品为 1, 4, 9... 根号n以内的完全平方数；每个物品可无限次取用。
# 2. 一维 dp[j] 定义：在【目前已遍历过的】完全平方数中，凑出和为 j 所需的最少数字个数。
#
# 3. 状态转移降维推导：
#    - 设第 i 个完全平方数为 square = i * i。
#    - 【二维视角】：面对第 i 个数，凑出容量 j 有两种选择：
#        (1) 不选它：数量 = 仅用前 i-1 个数凑 j 的数量 -> dp[i-1][j]
#        (2) 选它（且可重复选）：数量 = 用前 i 个数凑 (j - square) 的数量 + 1个当前数 -> dp[i][j - square] + 1
#        公式：dp[i][j] = min(dp[i-1][j], dp[i][j - square] + 1)
#
#    - 【一维空间压缩】：
#        因为 dp[i][j] 的计算只依赖于“正上方的旧值 (dp[i-1][j])”和“同层左侧的新值 (dp[i][j - square])”。
#        我们可以省略掉表示物品种类的维度 i，复用一个一维数组。
#        压缩后公式：dp[j] = min(dp[j], dp[j - square] + 1)
#
# 4. 遍历顺序的奥秘：
#    - 外层循环遍历物品（完全平方数），内层循环遍历背包容量（j 从 square 到 n）。
#    - 为什么内层必须【正序】？因为在计算当前 dp[j] 时，需要查询 dp[j - square]。
#      为了体现“完全背包”可以【重复】拿取同一个物品的特性，我们必须保证查到的 dp[j - square] 是
#      当前这一轮【已经拿过该物品后的新状态】。正序遍历完美契合了这一依赖关系！
import math
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 维护一个长度为n + 1的滚动一维dp数组,其中dp[j]表示截止到遍历到的第i个完全平方数，能凑出j的最小个数
        # 由于我们求大的是最小值，所以dp数组初始化为正无穷大
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        max_j = int(math.sqrt(n))   # 求根号n，从而确定物品（完全平方数）的数组大小
        squares = [j * j for j in range(1,max_j + 1)]
        # 外层遍历物品（完全平方数）
        for square in squares:
            # 内层遍历背包
            for j in range(square,n + 1):
                # 更新当前dp[j]
                dp[j] = min(dp[j],dp[j - square] + 1)
        return dp[n]

# 外层背包，内层物品:本题是完全背包问题的求极值问题，因此内外层的遍历顺序可以颠倒，即外层遍历背包容量，内层遍历物品也可！
import math
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
                # 维护一个长度为n + 1的滚动一维dp数组,其中dp[j]表示截止到遍历到的第i个完全平方数，能凑出j的最小个数
        # 由于我们求大的是最小值，所以dp数组初始化为正无穷大
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        max_j = int(math.sqrt(n))   # 求根号n，从而确定物品（完全平方数）的数组大小
        squares = [j * j for j in range(1,max_j + 1)]

        for j in range(1,n + 1):
            for square in squares:
                if j >= square:
                    dp[j] = min(dp[j],dp[j - square] + 1)
        
        return dp[n]
        