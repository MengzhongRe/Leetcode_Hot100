#
# @lc app=leetcode.cn id=230 lang=python
#
# [230] 二叉搜索树中第 K 小的元素
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        count = [0]
        res = [0]
        found = [False]

        def inorder(node):
            if not node or found[0]:
                return 
            # 先处理左子树
            inorder(node.left)
            # 若左子树已经找到，则直接返回当前层递归函数，不再处理当前节点
            if found[0]:
                return # 返回当前层递归函数
            # 处理当前节点值
            count[0] += 1
            if count[0] == k:
                res[0] = node.val
                found[0] = True # 标记为已找到
                return # 直接返回，不再递归右子树
            # 再处理右子树
            inorder(node.right)
            
        inorder(root)
        return res[0]

# 时间复杂度O（h + k）,先递归探到树底需要O(h)，然后再花O(k)时间找到第k个小元素
# 空间复杂度O(h),取决于递归栈调用，即二叉树的深度      
# @lc code=end

# 用栈模拟中序遍历递归过程
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        stack = [] # 初始化栈
        curr = root # 初始化指针
        count = 0

        while curr or stack: # 只要curr指针不为None，或栈不为空
            # 阶段一：向左探
            while curr: # 只要curr不为None就一直向左探
                stack.append(curr) # 将当前指针所在的节点推入栈中
                curr = curr.left # 指针转向左子孩
            # 阶段二：curr指针为None,说明左边已经探到头了
            node = stack.pop() # 弹出栈顶节点
            count += 1
            if count == k:
                return node.val
            curr = node.right # 转向弹出节点的右子孩
# 时间复杂度O(h + k),
# 空间复杂度O（h）,同上，但是由于是迭代实现的，无递归调用栈溢出风险，空间复杂度最优

        

