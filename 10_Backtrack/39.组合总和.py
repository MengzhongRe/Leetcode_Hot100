#
# @lc app=leetcode.cn id=39 lang=python
#
# [39] 组合总和
#

# @lc code=start

# 排序 + 剪枝:升序排序数组当当前检索数字大于剩余需要拼的数时，说明
# 后续数字也大于剩余需要拼的数，因此也不可能满足条件，可以直接返回
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort() # 升序排序 O(nlogn)
        path = []
        # 递归函数需要带起始索引，以防止选到前面选到过的数字导致重复结果（组合问题的标配）
        def backtrack(strat_index,remain):
            if remain == 0:
                res.append(path[:])
                return
            
            for i in range(strat_index,len(candidates)):
                # 剪枝：如果当前数字大于剩余需要拼的数，说明后续数字也大于剩余需要拼的数，因此不可能满足条件，可以直接返回
                if candidates[i] > remain:
                    break # 直接退出当前递归函数的整个后续的for循环
                path.append(candidates[i])
                # 由于数字可以无限次重复选取因此下一层递归函数的起始索引仍然是i
                # 即我们仍然可以选取当前数字及其之后的数字
                backtrack(i,remain - candidates[i])
                path.pop() # 回溯
        backtrack(0,target)
        return res    
# @lc code=end

# 对于这种**可以无限次重复选取**的回溯问题，时间复杂度很难给出一个像 $O(N^2)$ 那样精确的公式，但在面试中，你可以通过以下极其专业的推导震撼面试官：

# *   **时间复杂度**：上限为 $\mathcal{O}(N^{\frac{T}{M}})$，实际通常写为 $\mathcal{O}(S)$。
#     *   $N$ 是候选数组 `candidates` 的长度，$T$ 是目标值 `target`，$M$ 是候选数组中的**最小值** `min(candidates)`。
#     *   **深度推导**：如果你一直死磕那个最小的数字 $M$，你最多能往购物车里装 $\frac{T}{M}$ 个。这就意味着，这棵递归决策树的**最大深度是 $\frac{T}{M}$**。
#     *   **广度推导**：在树的每一个节点，你最多面临 $N$ 个数字的选择（分支）。
#     *   **结合**：一个分支最多为 $N$，深度最深为 $\frac{T}{M}$ 的树，节点上限级别就是 $N^{\frac{T}{M}}$。
#     *   *补充（剪枝的威力）*：因为我们做了提前排序和 `current_target - candidates[i] < 0` 时的 `break` 极速剪枝，大量的不可能分支被提前砍掉了。所以官方通常将时间复杂度表示为 $\mathcal{O}(S)$，其中 $S$ 为**所有可行解的长度之和**。

# *   **空间复杂度**：$\mathcal{O}(\frac{T}{M})$（辅助空间）。
#     *   同样根据上面的推导，空间消耗主要取决于**递归调用栈的最大深度**以及**用来记录当前状态的 `path` 数组的最大长度**。
#     *   它们双双都取决于最极端的情况（全拿最小的数字），即 $\frac{T}{M}$ 层。
#     *   因此辅助空间复杂度是 $\mathcal{O}(\frac{T}{M})$。

