#
# @lc app=leetcode.cn id=101 lang=python
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 判断对称二叉树的核心是：
# 根节点的左右子节点值必须相等
# 左子树的左子节点要和右子树的右子节点相等
# 左子树的右子节点要和右子树的左子节点相等
# 递归解法
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        # 边界判断，如果根节点为空，则一定是对称二叉树
        if not root:
            return True
        # 将根节点的左右子树传给辅助函数
        return self.compare(root.left,root.right)
    # 定义辅助函数
    # 判断对称二叉树的核心是：
# 根节点的左右子节点值必须相等
# 左子树的左子节点要和右子树的右子节点相等
# 左子树的右子节点要和右子树的左子节点相等
    def compare(self,left,right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        
        outside = self.compare(left.left,right.right)
        inside = self.compare(left.right,right.left)
        return outside and inside
# @lc code=end

