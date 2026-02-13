#
# @lc app=leetcode.cn id=94 lang=python
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        res = [] # 结果数组
        stack = [] # 维护一个栈空间，用于记录父节点
        curr = root # 维护一个指针，用于访问树的各个节点

        while curr or stack: # 只要curr不为None或栈不为空
            while curr: # 只要curr不为None我们就一直往左探，直到左边没有元素，即curr为None 
                stack.append(curr) # 把当前节点加入栈中
                curr = curr.left # 指针向左子孩移动
            # 第一层循环结束，curr为None，左边走到头了
            # 阶段二：弹出访问
            node = stack.pop() # 弹出栈顶，也就是最左下角的元素
            res.append(node.val)
            # 阶段三：转向右子孩
            # 不管右边有没有子节点，都先把curr指针转向右子节点
            # 如果右边有节点，下一次循环会继续往该节点的左子节点下探
            # 如果右侧无子节点，则跳过第一阶段，直接弹出栈顶的元素（回溯到更上一层）
            curr = node.right

        return res
# @lc code=end
# 递归法
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []

        def inorder(node):
            # 递归终止条件：无节点则返回
            if not node:
                return
            
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)
        
        inorder(root)
        return result
# 时间复杂度O(N)
# 空间复杂度最坏O(N)，平均O(logN)