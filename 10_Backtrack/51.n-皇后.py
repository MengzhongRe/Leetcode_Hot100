#
# @lc app=leetcode.cn id=51 lang=python
#
# [51] N 皇后
#

# @lc code=start
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = [] # 完整结果集合
        # 死亡集合，用于判断当前皇后放置位置是否安全
        cols = set() # 用于判断皇后是否在同一列
        diag1 = set() # 是否在同一主对角线
        diag2 = set() # 副对角线
        path = []

        def backtrack(row): # 每个递归函数只放置row行的皇后，天然保证了每一行只有一个皇后的条件
            # 递归终止条件
            if row == n: # 已经放置了n行皇后，说明找到了一种合法的解
                board = generate_board(path) # 调用生成函数将生成解法的棋盘
                res.append(board) # 将当前可能结果加入
                return
            
            for col in range(n): # 在改行（row），每一列都尝试防止皇后
                # 如果当前列或者当前主对角线或者当前副对角线已经有皇后了，那么当前位置不合法，跳过
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue

                # 以上条件均不满足，则说明当前col安全，防止皇后
                # 做选择
                path.append(col)
                # 由于我们尝试把皇后放在了（row，col）,所以我们需要更新死亡名单
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                #向下一行递归
                backtrack(row + 1)

                # 回溯 
                path.pop()
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        
        def generate_board(path):
            board = []
            for col in path:
                row_str = '.' * col + 'Q' + '.' * (n - 1 - col)
                board.append(row_str)
            return board
        
        backtrack(0)
        return res
              
# @lc code=end

# ### 1. 时间复杂度：$O(N!)$
# * **状态树的遍历**：在第一行放置皇后时，有 $N$ 个位置可以选择；进入第二行时，由于不能放在同一列，最多只有 $N-1$ 个位置可以选择；进入第三行最多有 $N-2$ 个选择，依此类推。因此，即使不考虑对角线冲突的剪枝，搜索树的遍历路径总数上限为 $N \times (N-1) \times (N-2) \times \dots \times 1 = N!$。
# * **冲突检测 ($O(1)$)**：代码中使用了 `cols`、`diag1`、`diag2` 这三个哈希集合来记录不可放置的列和对角线。判断 `col in cols` 等操作的时间复杂度均为 $O(1)$，因此每次做决定的代价极小。
# * **构造棋盘 ($O(N^2)$)**：当回溯到底部（`row == n`），说明找到了一个有效解。此时会调用 `generate_board` 生成棋盘，生成过程需要遍历 $N$ 个元素并对每个元素构造长度为 $N$ 的字符串，这一步耗时 $O(N^2)$。
# * **综合来看**：虽然每次找到有效解都需要 $O(N^2)$ 来构造结果，但 N 皇后的有效解数量（我们记为 $S$）远小于 $N!$。因此，算法的整体时间消耗由状态树的遍历主导，**总体时间复杂度为 $O(N!)$**。

# ### 2. 空间复杂度：$O(N)$（不包含返回结果所占的空间）
# 在算法分析中，我们通常将**辅助空间（Auxiliary Space）**与存储最终返回结果所需的空间分开计算：

# * **递归调用栈空间**：代码通过 `backtrack(row + 1)` 向下递归，每次递归前进一行，最大递归深度恰好为 $N$。因此，递归系统栈的空间消耗为 $O(N)$。
# * **状态记录数据结构**：
#   * `cols`（记录被占用的列）：最多存储 $N$ 个元素，空间为 $O(N)$。
#   * `diag1`（记录被占用的主对角线 `row - col`）：最多存储 $N$ 个元素，空间为 $O(N)$。
#   * `diag2`（记录被占用的副对角线 `row + col`）：最多存储 $N$ 个元素，空间为 $O(N)$。
#   * `path`（记录每行皇后所在的列）：存储 $N$ 个列号，空间为 $O(N)$。
# * **总体辅助空间**：以上所有的辅助变量和调用栈的空间都在 $O(N)$ 级别，因此**总体额外空间复杂度为 $O(N)$**。
