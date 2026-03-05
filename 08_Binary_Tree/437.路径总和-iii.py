#
# @lc app=leetcode.cn id=437 lang=python
#
# [437] 路径总和 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 前缀和 + 递归 + 回溯算法
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        prefix_count = {0:1} # 创建哈希表，存储前缀和出现的次数，key为前缀和，value为其出现的次数
        self.count = 0 # 结果值

        def backtrack(node,cur_sum):
            # 递归终止条件:若无节点直接返回
            if not node:
                return
            # 步骤一：更新前缀和
            cur_sum += node.val
            # 步骤二判断 cur_sum - target值是否已经出现在哈希表当中
            # 若存在则说明存在从相应祖先节点到当前node节点到路径和为target
            self.count += prefix_count.get(cur_sum - targetSum,0)
            # 步骤三，更新前缀和哈希表
            prefix_count[cur_sum] = prefix_count.get(cur_sum,0) + 1
            # 步骤四：递归左右子树获取结果
            backtrack(node.left,cur_sum)
            backtrack(node.right,cur_sum)

            # 步骤五：必要，在递归完左右子树之后由于其他节点已经不需要截止到当前节点的前缀和，需要在哈希表中删除
            prefix_count[cur_sum] -= 1
        # 启动递归
        backtrack(root,0)
        return self.count
            

# 时间复杂度	O(n)	每个节点仅被遍历一次（深度优先），哈希表的增删查操作都是 O(1)；
# 空间复杂度	O(n)	哈希表最多存储 n 个前缀和（最坏情况，二叉树退化为链表），递归栈深度最坏为 n；
# @lc code=end
# 暴力枚举法：通过双重递归，外层递归二叉树的每一个节点作为可能的路径起点，内层递归某选定节点作为路径起点下能够凑出和的路径数
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        # 内层递归函数，负责收集以node为起点的和 = remain的路径总数：
        def dfs_path(node,remain):
            # 递归终止条件
            if not node:
                return 0
            count = 1 if node.val == remain else 0
            # 递归左子树,收集经过左子节点的符合条件的路径数
            count += dfs_path(node.left,remain - node.val)
            # 递归右子树,收集经过右子节点的符合条件的路径数
            count += dfs_path(node.right,remain - node.val)
            return count # 返回以当前node节点为起点和为remain的路径数量
        
        # 外层递归函数：负责遍历所有节点作为内层函数的起点
        def dfs_start(node):
            # 递归终止条件
            if not node:
                return 0
            # 返回以当前节点为起点的路径数 + 以左子节点为起点 + 以右子节点为起点
            return dfs_path(node,targetSum) + dfs_start(node.left) + dfs_start(node.right)
        # 主逻辑
        return dfs_start(root)

# 时间复杂度分析
# 1. 最坏情况：O(n2)
# 场景：二叉树退化为「链表」（比如所有节点只有左孩子），这是暴力解法的最坏情况。
# 计算过程：
# 外层递归遍历第 1 个节点（根）：内层递归需要遍历剩下的 n-1 个节点 → 耗时 O(n)；
# 外层递归遍历第 2 个节点：内层递归需要遍历剩下的 n-2 个节点 → 耗时 O(n)；
# 外层递归遍历第 n 个节点：内层递归遍历 0 个节点 → 耗时 O(1)；
# 总操作数：n+(n−1)+(n−2)+...+1=2n(n+1)​ → 时间复杂度为 O(n2)。


# 2. 最好情况：O(nlogn)

# 场景：二叉树是「平衡二叉树」（比如完全二叉树），树的高度为 logn。
# 计算过程：
# 外层递归遍历每个节点（共 n 个）；
# 每个节点的内层递归最多遍历「从该节点到叶子的路径长度」（平衡树中平均为 logn）；
# 总操作数：n×logn → 时间复杂度为 O(nlogn)。

# 空间复杂度分析
# 空间复杂度的核心是「递归调用栈的深度」（因为暴力解法没有额外的哈希表 / 数组等空间开销）。
# 1. 最坏情况：O(n)
# 场景：二叉树退化为链表，递归调用栈的深度等于节点数 n。
# 比如外层递归到链表最后一个节点时，递归栈已经有 n 层；
# 内层递归调用时，栈深度会在 n 的基础上再增加，但复杂度仍为 O(n)（高阶项主导）。

# 2. 最好情况：O(logn)
# 场景：平衡二叉树，递归栈的深度等于树的高度 logn。