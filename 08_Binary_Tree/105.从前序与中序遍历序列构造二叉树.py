#
# @lc app=leetcode.cn id=105 lang=python
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        # 递归终止条件
        if not preorder or not inorder:
            return None
        # 前序第一个节点即为当前子树的根节点
        root_val = preorder[0]
        # 初始化根节点
        root = TreeNode(root_val)
        # 获取根节点在中序遍历中的索引位置，从而知道左侧是左子树，右侧时右子树
        root_index = inorder.index(root_val) # 扫描中序遍历数组的根节点所在位置需要O(N)
        # 递归构造左子树
        root.left = self.buildTree(preorder[1:1+root_index],inorder[:root_index])
        # 递归构造右子树
        root.right= self.buildTree(preorder[1+root_index:],inorder[1+root_index:])

        return root
# 时间复杂度O(n**2),每个节点都需要作为根节点遍历一次，每次遍历都需要O(N)的扫描时间
# 空间复杂度O(H),取决于二叉树深度   
# @lc code=end

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        dic = dict()
        for i,val in enumerate(inorder):
            dic[val] = i

        def build(pre_l,pre_r,in_l,in_r):
            # 递归终止条件
            if pre_l > pre_r or in_l > in_r:
                return None
            
            # 取前序序列首为根节点值
            root_val = preorder[pre_l]
            root = TreeNode(root_val) # 初始化根节点

            root_index = dic[root_val] # 用哈希表查找根节点值在中序遍历中的索引位置
            left_size = root_index - in_l # 计算左子树大小

            root.left = build(pre_l + 1,pre_l + left_size,in_l,root_index - 1)
            root.right = build(pre_l + 1 + left_size,pre_r,root_index + 1,in_r)

            return root
        n = len(preorder)

        return build(0,n - 1,0,n - 1)

