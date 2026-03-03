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
# 时间复杂度O（N）所有节点遍历一次,空间复杂度O(H)取决于递归栈深度
# @lc code=end
from collections import deque

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        # 边界判断
        if not root:
            return True
        # 初始化队列，需要存入需要比较的两个节点
        queue = deque()
        queue.append(root.left)
        queue.append(root.right)
        # 只要队列不为空，即只要还有节点没有遍历完
        while queue:
            # 取出前两个节点
            node1 = queue.popleft()
            node2 = queue.popleft()
            # 两个都为空则直接比较下一轮
            if not node1 and not node2:
                continue
            # 只有一个为空，返回False
            if not node1 or not node2:
                return False
            # 值不相等，返回False
            if node1.val != node2.val:
                return False
            
            # 按照镜像顺序将子节点加入到队列当中去
            queue.append(node1.left)
            queue.append(node2.right)
            queue.append(node1.right)
            queue.append(node2.left)
        # 所有节点都匹配成功
        return True
# 时间复杂度O(N),空间复杂度O(N),队列层序遍历取决于节点数最多的一层，最坏情况下平衡二叉树最后一层节点数约为