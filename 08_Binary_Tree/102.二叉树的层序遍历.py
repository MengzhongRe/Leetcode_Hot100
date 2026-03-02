#
# @lc app=leetcode.cn id=102 lang=python
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 用双端队列模拟层序遍历
from collections import deque

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        # 初始化队列，存入根节点
        queue = deque([root])
        res = [] # 初始化结果列表
        # 只要队列不为空，即只要还有没有遍历过的树节点
        while queue:
            # 由于队列在遍历的过程中会加入新的节点，因此在进行该层遍历前需要先记录当前层的节点数量
            level_size = len(queue)
            # 初始化当前层的结果列表
            current_res = []
            # 进行该层的遍历
            for _ in range(level_size):
                # 取出队首节点
                node = queue.popleft()
                current_res.append(node.val)
                # 若子节点存在则加入到队尾
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(current_res)
        
        return res
# 时间复杂度O（N）,空间复杂度O(W),W 为二叉树最大宽度
# @lc code=end

