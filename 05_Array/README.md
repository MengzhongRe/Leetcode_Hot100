LeetCode 每日三题解题笔记

本文档总结今日完成的三道 LeetCode 题目，每道题包含 题目核心、解题逻辑（必要时附数学证明）、核心代码、复杂度分析，格式清晰，便于复盘回顾。

题目一：53. 最大子数组和（Maximum Subarray）

1. 题目核心

给定一个整数数组 nums，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

2. 解题逻辑

本题有两种核心解法：暴力枚举法（直观但低效）、Kadane 算法（最优解，动态规划思想），重点掌握 Kadane 算法。

方法一：暴力枚举法

核心思路：枚举所有可能的子数组（通过两层循环，外层控制子数组起始索引，内层控制结束索引），计算每个子数组的和，记录最大值。

局限性：重复计算子数组和，时间复杂度极高，无法通过大数据测试用例，仅用于理解问题本质。

方法二：Kadane 算法（最优解）

核心思想：利用动态规划，定义子问题，避免重复计算，仅需一次遍历即可找到最大和。

关键定义与数学证明

设数组为 \( A[0], A[1], \dots, A[n-1] \)，定义：

- \( S[i] \)：以 \( A[i] \) 结尾的所有子数组中，和最大的子数组的和（即算法中的 current_max）。

需证明：\( S[i] = \max\left(A[i], S[i-1] + A[i]\right) \)

证明：

1. 引理：以 \( A[i] \) 结尾的任意子数组，均可表示为 \( A[k] + A[k+1] + \dots + A[i] \)（其中 \( 0 \le k \le i \)）。

2. 分两类讨论：
        

  - 当 \( k = i \)：子数组仅包含 \( A[i] \)，和为 \( A[i] \)。

  - 当 \( k \le i-1 \)：子数组包含 \( A[i] \) 和以 \( A[i-1] \) 结尾的子数组，和为 \( (A[k] + \dots + A[i-1]) + A[i] \)。设 \( T = A[k] + \dots + A[i-1] \)，则 \( T \le S[i-1] \)（因 \( S[i-1] \) 是以 \( A[i-1] \) 结尾的最大子数组和），故该类子数组的最大和为 \( S[i-1] + A[i] \)。

3. 综合两类情况，以 \( A[i] \) 结尾的最大子数组和为 \( \max\left(A[i], S[i-1] + A[i]\right) \)，证毕。

算法步骤：

1. 初始化 current_max（当前结尾最大和）和 global_max（全局最大和）为数组第一个元素。

2. 从第二个元素开始遍历，每一步更新 current_max 为 \( \max(num, current_max + num) \)。

3. 同步更新 global_max 为 current_max 和自身的最大值，遍历结束后返回 global_max。

3. 核心代码

暴力枚举法（参考代码）

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        max_sum = -1e9
        for i in range(n):
            total_sum = 0
            for j in range(i, n):
                total_sum += nums[j]
                max_sum = max(max_sum, total_sum)
        return max_sum

Kadane 算法（最优代码）

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        # 初始化当前结尾最大和、全局最大和
        current_max = global_max = nums[0]
        # 从第二个元素开始遍历
        for num in nums[1:]:
            current_max = max(num, current_max + num)
            global_max = max(global_max, current_max)
        return global_max

4. 复杂度分析

解法

时间复杂度

空间复杂度

说明

暴力枚举法

O(n²)

O(1)

两层嵌套循环，枚举所有子数组，低效

Kadane 算法

O(n)

O(1)

一次遍历，常数级额外空间，最优解

题目二：189. 轮转数组（Rotate Array）

1. 题目核心

给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，要求 原地修改 数组（不返回任何值，直接修改输入数组）。

2. 解题逻辑

本题有三种常见解法，重点掌握三次反转法（最优解，原地修改且空间最优）。

方法一：辅助数组法（直观易懂）

核心思路：创建一个与原数组长度相同的辅助数组，将原数组每个元素放到轮转后的正确位置，再通过切片赋值将辅助数组内容覆盖原数组（实现原地修改）。

关键细节：\( k = k \% n \)（处理 k 大于数组长度的情况，避免无效轮转），轮转后位置公式为 \( (i + k) \% n \)（i 为原索引）。

方法二：三次反转法（最优解）

核心思路：数组向右轮转 k 位，等价于将数组末尾 k 个元素移到开头，通过三次反转实现原地修改，无需额外空间。

反转步骤：

1. 反转整个数组：将末尾 k 个元素移到开头（但顺序反转）。

2. 反转前 k 个元素：恢复末尾 k 个元素的正确顺序。

3. 反转后 n-k 个元素：恢复剩余元素的正确顺序。

示例演示（nums = [1,2,3,4,5,6,7], k=3）：

1. 反转整个数组 → [7,6,5,4,3,2,1]

2. 反转前 3 个元素 → [5,6,7,4,3,2,1]

3. 反转后 4 个元素 → [5,6,7,1,2,3,4]（正确结果）

方法三：暴力旋转法（低效，不推荐）

核心思路：每次将数组向右轮转 1 位，重复 k 次。每次轮转需将最后一个元素移到开头，其余元素后移。

局限性：时间复杂度极高，k 较大时会超时，仅作思路参考。

3. 核心代码

辅助数组法（参考代码）

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n  # 处理k大于数组长度的情况
        copyed_nums = [0] * n
        # 赋值到正确位置
        for i in range(n):
            copyed_nums[(i + k) % n] = nums[i]
        # 切片赋值，实现原地修改
        nums[:] = copyed_nums

三次反转法（最优代码）

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n  # 关键：避免无效轮转
        
        # 定义原地反转函数（复用）
        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        # 三次反转核心步骤
        reverse(0, n - 1)    # 1. 反转整个数组
        reverse(0, k - 1)    # 2. 反转前k个元素
        reverse(k, n - 1)    # 3. 反转后n-k个元素

4. 复杂度分析

解法

时间复杂度

空间复杂度

说明

辅助数组法

O(n)

O(n)

直观易懂，需额外空间存储辅助数组

三次反转法

O(n)

O(1)

原地修改，无额外空间，最优解

暴力旋转法

O(n*k)

O(1)

低效，k 较大时超时，不推荐

题目三：Python 列表 sort() 方法详解（关联排序类题目）

1. 核心说明

虽然不是 LeetCode 编程题，但 sort() 方法是 Python 中排序的核心工具，高频用于各类排序相关题目（如数组排序、自定义排序），此处详细总结其用法、参数及特性，适配解题需求。

2. sort() 方法核心细节

2.1 基本语法

sort() 是 Python 列表的内置方法，用于 原地排序 列表，无返回值（返回 None），语法如下：

list.sort(key=None, reverse=False)

2.2 核心参数详解

参数1：reverse（控制升序/降序）

- 默认值：False → 升序排列（从小到大）。

- 设置为 True → 降序排列（从大到小）。

# 示例
nums = [3, 1, 4, 1, 5, 9]
nums.sort()  # 升序：[1, 1, 3, 4, 5, 9]
nums.sort(reverse=True)  # 降序：[9, 5, 4, 3, 1, 1]

参数2：key（自定义排序依据，最常用）

接收一个函数（或 lambda 匿名函数），该函数作用于列表的每个元素，排序时按函数返回值的大小排序，而非元素本身。

默认值：None → 直接比较元素本身。

# 示例1：按字符串长度排序
words = ["banana", "apple", "cherry", "date"]
words.sort(key=len)  # 结果：['date', 'apple', 'banana', 'cherry']

# 示例2：按绝对值排序
nums = [-3, 1, -4, -2]
nums.sort(key=abs)  # 结果：[1, -2, -3, -4]

# 示例3：对字典列表按指定键排序
students = [{"name": "Tom", "score": 85}, {"name": "Jerry", "score": 92}, {"name": "Alice", "score": 78}]
students.sort(key=lambda x: x["score"])  # 按score升序

2.3 关键特性

- 原地排序：直接修改原列表，不创建新列表（若需保留原列表，用 sorted() 函数）。

- 稳定排序：当两个元素的 key 值相等时，保留其在原列表中的相对顺序。

- 仅适用于列表：是列表专属方法，不能用于元组、字符串等其他可迭代对象。

2.4 与 sorted() 函数的区别（补充）

特性

list.sort()

sorted()

适用对象

仅列表

所有可迭代对象（列表、元组、字符串等）

是否修改原对象

是（原地排序）

否（返回新列表）

返回值

None

排序后的新列表

3. 复杂度分析（sort() 底层实现）

Python 的 sort() 方法底层使用 Timsort 算法（一种结合归并排序和插入排序的混合算法），其复杂度为：

- 时间复杂度：O(n log n)（最坏、平均、最好情况均为 O(n log n)，高度优化）。

- 空间复杂度：O(n)（Timsort 算法需额外空间存储临时片段，属于稳定排序的合理开销）。

总结

1. 最大子数组和：最优解为 Kadane 算法（O(n) 时间，O(1) 空间），核心是定义“以当前元素结尾的最大子数组和”，通过动态规划避免重复计算。

2. 轮转数组：最优解为三次反转法（O(n) 时间，O(1) 空间），核心是通过三次反转实现原地修改，关键步骤是 \( k = k \% n \)。

3. sort() 方法：Python 列表内置排序工具，底层为 Timsort 算法，核心参数为 key（自定义排序）和 reverse（控制升降序），高频用于各类排序场景。

复盘重点：掌握动态规划（Kadane 算法）、原地修改技巧（三次反转）、排序工具的灵活使用，理解每种解法的复杂度优化逻辑。
