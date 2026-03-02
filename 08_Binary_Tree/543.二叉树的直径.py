#
# @lc app=leetcode.cn id=543 lang=python
#
# [543] 二叉树的直径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # 二叉树的直径 = 所有节点的左右子树深度和 的 最大值
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # 初始化一个列表，由于列表是可变对象，可以在嵌套函数中修改
        diameter = [0]
        # 递归函数：计算当前节点的深度：，当前节点深度 = max(左右子树深度) + 1
        def depth(node):
            # 递归终止条件
            if not node:
                return 0
            # 计算左右子树深度
            left_depth = depth(node.left)
            right_depth = depth(node.right)
            # 计算左右子树深度和
            current_depth = left_depth + right_depth
            if current_depth > diameter[0]:
                diameter[0] = current_depth
            return max(left_depth, right_depth) + 1
        # 调用递归函数，计算每个节点的左右子树深度和
        depth(root)
        return diameter[0]        
# @lc code=end

# 时间复杂度：O (n)，n 是二叉树节点数，每个节点仅被递归访问一次。
# 空间复杂度：O (h)，h 是二叉树的高度。最坏情况（退化为链表）h=n，空间复杂度 O (n)；
# 平衡二叉树 h=logn，空间复杂度 O (logn)。空间消耗主要来自递归栈。