#
# @lc app=leetcode.cn id=124 lang=python
#
# [124] 二叉树中的最大路径和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 后序遍历 + 递归 
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_sum = float('-inf')
        def dfs(node):
            # 递归终止条件
            if not node:
                return 0
            # 去左边和右边找它们能提供的最大单链和。注意：如果该单链和为负数，则意味着我们不应该加入该单链，因此返回结果应该取0
            left = max(dfs(node.left),0)
            right = max(dfs(node.right),0)
            #算私房钱：包括当前节点的倒V型的路径和
            # 把它和历史最大值比较更新
            current_sum = node.val + left + right
            self.max_sum = max(self.max_sum,current_sum)
            # 只能挑左右两边最大的一个加上自己，作为一条线报上去
            return node.val + max(left,right)
        # 启动递归
        dfs(root)
        return self.max_sum
        
# @lc code=end

