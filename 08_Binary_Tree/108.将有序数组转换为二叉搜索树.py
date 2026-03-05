#
# @lc app=leetcode.cn id=108 lang=python
#
# [108] 将有序数组转换为二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        # 辅助递归函数，处理数组的左右边界
        def build(left,right):
            # 递归终止条件
            if left > right:
                return 
            # 取当前区间的中点为根节点，保证树的平衡性，偏左偏右均可，因本题无唯一解
            mid = (left + right) // 2
            # 初始化当前子树根节点，值为有序数组的中间位置的数值
            root = TreeNode(nums[mid])
            # 递归构造左右子树
            root.left = build(left,mid - 1)
            root.right = build(mid + 1,right)
            # 返回当前子树根节点
            return root
        return build(0,len(nums) - 1)
# 时间复杂度O(N),其中N为输入数组的长度，每个元素被访问一次。
# 空间复杂度O(logN)        
# @lc code=end