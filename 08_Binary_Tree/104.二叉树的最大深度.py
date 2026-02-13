#
# @lc app=leetcode.cn id=104 lang=python
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 递归法（深度优先搜索）：该节点的最大深度 = 1 + max(左子树高度，右子树高度)
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # if not root:
        #     return 0
        # left_height = self.maxDepth(root.left)
        # right_height = self.maxDepth(root.right)

        # return 1 + max(left_height,right_height)
        if not root:
            return 0
        # 初始化双端队列,直接把根节点加入队列中
        queue = deque([root])
        depth = 0

        while queue:
            # 记录当前层节点的个数
            # 因为在下面的for循环过程中队列的长度会改变
            level_size = len(queue)
            # 把当前层的左右节点一个一个拿出来，并把他们的字节点放到队列尾部
            for _ in range(level_size):
                node = queue.popleft() # 当前层的最左侧节点即最早入队的出列并获取该节点(即队列头部)，O(1)
                if node.left:
                    queue.append(node.left) # O(1)
                if node.right:
                    queue.append(node.right) # O(1)
                
            depth += 1 #当前层处理完 + 1
        
        return depth
# 时间复杂度O(N),每个节点被访问一次
# 空间复杂度O(H),H为树的高度     
# @lc code=end

# 迭代法（广度优先搜索、层序遍历）
# 用队列一层一层地遍历二叉树
# 每遍历完一层，深度就加1，直到队列为空

from collections import deque
class Solution:
    def maxDepth(self,root):
        """
        maxDepth 的 Docstring
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # 边界判断：
        if not root:
            return 0
        # 初始化双端队列,直接把根节点加入队列中
        queue = deque([root])
        depth = 0

        while queue:
            # 记录当前层节点的个数
            # 因为在下面的for循环过程中队列的长度会改变
            level_size = len(queue)
            # 把当前层的左右节点一个一个拿出来，并把他们的字节点放到队列尾部
            for _ in range(level_size):
                node = queue.popleft() # 当前层的最左侧节点即最早入队的出列并获取该节点(即队列头部)，O(1)
                if node.left:
                    queue.append(node.left) # O(1)
                if node.right:
                    queue.append(node.right) # O(1)
                
            depth += 1 #当前层处理完 + 1
        
        return depth
# 时间复杂度O(N),每个节点入队出队一次
# 空间复杂度O(N),取决于节点数最多的一层，最坏情况下，如果是满二叉树，则需要N/2的空间
