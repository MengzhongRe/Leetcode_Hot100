#
# @lc app=leetcode.cn id=199 lang=python
#
# [199] 二叉树的右视图
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 通过双端队列层序遍历，遍历前记录每一层的节点数，当达到最后一个节点时记录该节点的值
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        from collections import deque
        # 边界判断
        # if not root:
        #     return []
        
        # res = [] # 结果列表
        # queue = deque([root]) # 双端队列，初始时加入根节点

        # while queue:
        #     level_size = len(queue) # 当前层的节点数
        #     for i in range(level_size):
        #         node = queue.popleft() # 弹出当前层的节点
        #         if i == level_size - 1:
        #             res.append(node.val) # 记录最后一个节点值
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        
        # return res
    
# @lc code=end

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        # 边界判断
        if not root:
            return []
        
        res = []
        
        def dfs(node,level):
            # 递归终止条件
            if not node:
                return
            
            if level == len(res):
                res.append(node.val)
            # 先递归右子树
            dfs(node.right,level + 1)
            # 再递归左子树
            dfs(node.left,level + 1)
        
        dfs(root,0)

        return res

# 时间复杂度O(N),每个节点入队出队一次
# 空间复杂度O(h)  

# 栈模拟递归
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        # 边界判断
        if not root:
            return []
        
        stack = [(root,0)]
        res = []

        while stack:
            node,level = stack.pop()
            # 如果当前层还未访问过，则将节点值加入到结果数组中
            if level == len(res):
                res.append(node.val)
            # 先加入右子孩
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        return res
