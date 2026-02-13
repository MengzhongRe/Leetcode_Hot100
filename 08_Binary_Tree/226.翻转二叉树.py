#
# @lc app=leetcode.cn id=226 lang=python
#
# [226] 翻转二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 递归法：先交换自身节点的左右子节点，再对左右子节点递归翻转
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        # 递归终止条件，当当前节点为空时直接返回，不再交换其左右孩子
        if not root:
            return None
        # 交换左右子节点
        root.left,root.right = root.right,root.left
        self.invertTree(root.left) # 翻转左子树
        self.invertTree(root.right) # 翻转右子树
        return root # 返回根节点
# 时间复杂度O(N),每个节点需要被访问一次
# 空间复杂度O(H)
        
# @lc code=end

# 递归法
from collections import deque
class Solution:
    def invertTree(self,root):
        """
        :type root: Optional[TreeNode]
        :rtype: OPtional[TreeNode]
        """
        if not root:
            return None
        # 初始化双端队列，并把根节点加入队列
        queue = deque([root])
        # 迭代处理队列，直到队列为空，即所有节点已处理完毕
        while queue:
            # 准备弹出当前节点（从队头）
            node = queue.popleft()
            # 核心操作：交换该节点的左右子节点，即便子节点是None也没关系
            # 因为也是对的
            node.left,node.right = node.right,node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return root
# 时间复杂度O(N),每个节点入队出队一次
# 空间复杂度O(W).W 是树的最大宽度，在满二叉树中是N/2