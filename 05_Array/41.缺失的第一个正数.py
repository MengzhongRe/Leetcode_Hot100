#
# @lc app=leetcode.cn id=41 lang=python
#
# [41] 缺失的第一个正数
#
# 原地哈希操作
# @lc code=start
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # 第一次循环让数字归位，若1<= x <= n,则让x去下标为x - 1的位置上去
        # 原因在于我们的结果是从1开始遍历的，而数组的下标是从0开始的，我们关心的是1要去到第一个位置上，也就是索引为0处
        for i in range(n):
            # 如果x，即nums[i]是我们关心的数（1<= x <= nums[i],负数和0我们并不关系）
            # 并且x还不在正确的座位上，也就是在下标为x-1处。即nums[nums[i] - 1] != nums[i]
            # 则我们需要交换这两个索引处的值。这里我们已经排除了重复的情况。
            # 因为只要nums[nums[i]-1] 处已经放好了Nums[i],我们就不需要交换了
            while 0 < nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                target_dix = nums[i] - 1
                nums[i],nums[target_dix] = nums[target_dix],nums[i] # 交换
        
        # 第二次循环看看哪个i缺少正确的元素，则结果就是i + 1
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        # 如果遍历完没有返回，则数组是从1开始的连续整数数组，直接返回n + 1
        return n + 1

# 时间复杂度O(n)
# 空间复杂度O(1),原地哈希    
# @lc code=end
# 用哈希表记录Nums中出现的数，这里用set记录数，排除了重复数，同时也实现了O(1)查找
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums) # o(N)

        # 从1开始查找，第一个不在哈希表中的数就是未在数组中出现的最小的正整数
        index = 1
        while True: # O(N)
            if index not in num_set:
                return index
            index += 1

# 时间复杂度O(N)
# 空间复杂度O(N),哈希表存储空间

# 排序算法，先排序，再按照抽屉原理寻找
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort() # 排序 O(nlogn)
        target = 1 # 从1开始判断

        for x in nums: # 遍历数组 # O(n)
            if x == target: # 如果存在则target不是结果
                target += 1 # 加1继续判断
            elif x > target: # 这里跳过了重复数字，只有当x> taget时才说明没有出现target
                return target
        
        return target # 当For循环遍历完整个数组时，说明数组是连续的，就返回target
# 时间复杂度O(nlogn),主要取决于排序算法
# 空间复杂度O(1)或O(logn),主要取决于排序算法是否为原地
