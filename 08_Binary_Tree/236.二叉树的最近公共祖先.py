#
# @lc app=leetcode.cn id=236 lang=python
#
# [236] 二叉树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 后序遍历 + 递归
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # 递归终止条件
        if not root or root == p or root == q:
            return root
        # 递归左子树，在左子树中找节点p,q并返回结果值
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        # 左右子树递归完成后，拿到两个结果，代表了左右子树是否有相关节点
        if left and right: # 如果左右子树都有返回值，则说明p,q一个在左一个在右，且当前节点root是目前唯一的交叉节点，因此是最近的公共祖先直接返回
            return root 
        return left if left else right # 如果只有Left节点有返回值，代表左子树有找到节点或者公共祖先，无论如何我们都把结果上报就行了
# 时间复杂度o(n),最坏情况下需要遍历所有节点
# 空间复杂度o(h)
# @lc code=end

