#
# @lc app=leetcode.cn id=114 lang=python
#
# [114] 二叉树展开为链表
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 莫里斯遍历实现原地O(1)空间调整
# 核心思路（莫里斯先序遍历）
# 莫里斯遍历的本质是 “利用树的空指针做线索，模拟递归 / 栈的遍历过程”，先序版的关键步骤：
# 找前驱节点：对于当前节点 cur，找到其左子树的最右侧节点（即中序遍历的前驱节点）。
# 建立临时链接：将前驱节点的右指针指向 cur 的右子树（保存右子树的引用）。
# 重构指针：将 cur 的右指针指向其左子树，同时置空左指针。
# 移动当前节点：cur 指向其右子树（原左子树），重复上述步骤，直到所有节点处理完毕。

class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        # 边界判断
        if not root:
            return []
        
        curr = root # 当前处理的节点

        while curr:
            # 如果当前节点有左子树，先处理左子树
            if curr.left:
                # 找到左子树的最右节点，即前驱节点
                predecessor = curr.left
                while predecessor.right:
                    predecessor = predecessor.right
                # 找到前驱节点后，该节点的右指针一定为空，将其指向为当前节点的右子树
                predecessor.right = curr.right
                # 当前节点的右指针指向当前节点的左子树，左指针置空
                curr.right = curr.left
                curr.left = None
            # 若当前节点无左子树或左子树已经处理完，则处理当前节点的右子树（即原左子树）
            curr = curr.right
# 时间复杂度O（N），每个节点最多被访问两次，一次curr,一次predecessor
# 空间复杂度O（1），莫里斯遍历无递归，栈，队列等额外空间，只用了curr,predecessor常数个指针
# @lc code=end

class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        # 边界判断
        if not root:
            return []
        
        stack = [root]
        # 初始化一个虚拟头节点，防止以根节点为最初前驱节点重复引用自己
        dummy = TreeNode(0)
        # 将前驱节点初始化为虚拟头节点
        prev_node = dummy

        while stack:
            # 因为是先序遍历，直接弹出栈顶
            node = stack.pop()
            # 修改节点的引用
            prev_node.left = None
            prev_node.right = node
            # 由于栈是后进先出的，所以为了保证先序遍历，先访问左子节点，就需要先将右子节点压入栈
            if node.right:
                stack.append(node.right)
            # 再将左子节点压入栈 
            if node.left:
                stack.append(node.left)
            prev_node = node
        # 返回根节点，也就是虚拟头节点的右子节点
        return dummy.right
# 时间复杂度O(N)
# 空间复杂度O（N）

class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        # 边界判断
        if not root:
            return []
        res = []
        
        def dfs(node):
            # 递归终止条件
            if not node:
                return
            res.append(node)
            dfs(node.left)
            dfs(node.right)
        dfs(root)

        for i in range(len(res) - 1):
            res[i].left = None
            res[i].right = res[i + 1]
        
        return res[0] 