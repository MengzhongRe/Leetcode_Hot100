#
# @lc app=leetcode.cn id=416 lang=python
#
# [416] 分割等和子集
#

# @lc code=start

# 分割成两个元素子集，假设可以，设其中一个和为sum1,另一个为sum2,设整个数组所有和为num,则必有sum1 = sum2 = sum // 2
# 因此我们可以先判断sum % == 0，如果不是，则由于里面都是正整数，则显然根本不可能会有，直接返回False
# 接下来就需要判断，nums中的数是否有可能组合在一起其和为sum // 2。显然这是一个0-1背包问题，背包容量为sum // 2,物品即为
# nums中的所有数字，数字不可重复选取，故为0-1背包。
# 设dp[i][j]为能否从前i个数字中凑出数字j,值为True 或者False,则考虑第i个数字num,则if dp[i - 1][j - num]:dp[i][j]
# 为True,考虑到状态转移公式依赖于左上角的dp旧值，因此在一维dp滚动数组中必须倒序遍历背包容量j，外层物品，内层背包
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_sum = sum(nums)
        # 剪枝：如果总和为奇数，则不可能分成两个子集，直接返回False
        if nums_sum % 2 != 0:
            return False
        # 求目标值，即总和的一半
        target = nums_sum // 2
        # 剪枝：如果最大值都比总和的一半大，则不可能
        if max(nums) > target:
            return False
        # 初始化dp数组，dp[j]表示是否可以从nums中选取一些数字使得它们的和为j
        dp = [False] * (target + 1)
        # 作为基础条件，dp[0]为True，表示可以通过不选取任何数字来达到和为0
        dp[0] = True
        # 0-1背包模板：外层物品，内层背包容量倒序遍历
        for num in nums:
            # 必须倒序遍历背包容量j，避免状态转移公式依赖于左上角的dp旧值被覆盖
            for j in range(target,num - 1,- 1):
                # 只要dp[j - num]为True，说明之前的状态可以通过选取当前数字num来达到和为j，因此dp[j]也为True
                if dp[j - num]:
                    dp[j] = True
        
        return dp[target]  
# 时间复杂度O(n * target)   
# 空间复杂度O(target)   
# @lc code=end

# 方法二：动态规划 + python集合set自动去重更新
# 我们可以维护一个dp集合，初始dp={0},遍历原数组数字，dp集合表示目前为止遍历过的数字可以组成的和
# 每次遍历到新数字num时，将其与dp中的每一元素相加，得到一个新的和，然后集合自动去重更新
# 过程中一旦判断到target在dp中，则说明可以分割成两个子集，直接返回True
class Solution(object):
     def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        if max(nums) > target:
            return False
        # dp集合表示目前为止遍历过的数字可以组成的和，初始为{0}
        dp = {0}
        # 遍历原数组数字，dp集合表示目前为止遍历过的数字可以组成的和，每次遍历到新数字num时，
        # #将其与dp中的每一元素相加，得到一个新的和，然后集合自动去重更新
        for num in nums: # O(N)
            dp |= {v + num for v in dp if v + num <= target}    # O(target)
            if target in dp:    # 判断是否在dp中，说明可以分割成两个子集，直接返回True
                return True
        return False
# 时间复杂度O(N * target),外层需要遍历每个数字，内层操作平均时间复杂度也是O(target)
# 空间复杂度O(target),dp集合中最多存储target个元素