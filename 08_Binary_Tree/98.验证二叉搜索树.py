#
# @lc app=leetcode.cn id=98 lang=python
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 解法一：递归 + 上下界限
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        # 构造辅助函数，参数为当前节点和当前节点值的合法范围
        def isValid(node,lower,upper):
            # 递归终止条件：当前节点为空，说明当前路径合法
            if not node:
                return True
            # 当前节点值不在合法范围内，说明不是二叉搜索树
            if node.val <= lower or node.val >= upper:
                return False
            # 递归检查左子树和右子树，更新合法范围
            return isValid(node.left,lower,node.val) and isValid(node.right,node.val,upper)
    
# 时间复杂度O(N)，其中N为二叉树的节点数，每个节点被访问一次。
# 空间复杂度O(H)，其中H为二叉树的高度，递归调用栈的空间取决于二叉树的高度，最坏情况下为O(N）
# @lc code=end

# 解法二：中序遍历法——BST 的中序遍历结果是严格升序数组，因此也可以通过中序遍历验证：
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        self.prev = float('-inf') # 记录前一个节点值
        return self.inorder(root) # 中序遍历函数，返回当前子树是否合法
    
    def inorder(self,node):
        if not node:
            return True
        # 先遍历左子树
        if not self.inorder(node.left):
            return False
        # 假如当前节点值小于等于先前的节点值，则说明不是二叉搜索树，因为二叉搜索树在中序遍历下是严格递增的
        if node.val <= self.prev:
            return False
        self.prev = node.val # 更新前一个节点值为当前节点值
        # 最后遍历右子树
        return self.inorder(node.right)

# 时间复杂度O(N)，其中N为二叉树的节点数，每个节点被访问一次。
# 空间复杂度O(H)，其中H为二叉树的高度，递归调用栈的空间取决于二叉树的高度，最坏情况下为O(N）