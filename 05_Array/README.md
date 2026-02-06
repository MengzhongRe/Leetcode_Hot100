# LeetCode 刷题笔记 - 数组与动态规划专题
> 日期：2026.02.04
> 专题：数组操作、动态规划
> 题目列表：
> 1. 53. 最大子数组和
> 2. 189. 轮转数组
> 3. 排序算法（Python 内置排序原理与实践）

---

## 一、 53. 最大子数组和
### 题目描述
给定一个整数数组 `nums`，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

### 解题思路
#### 1. 暴力解法（基础思路）
- **核心逻辑**：两层循环枚举所有可能的子数组，计算子数组和并记录最大值。
- **代码实现**
  ```python
  class Solution(object):
      def maxSubArray(self, nums):
          n = len(nums)
          if n == 1:
              return nums[0]
          max_sum = -1e9
          for i in range(n):
              total = 0
              for j in range(i, n):
                  total += nums[j]
                  max_sum = max(max_sum, total)
          return max_sum
  ```
- **复杂度分析**
  - 时间复杂度：$O(n^2)$，两层嵌套循环遍历所有子数组。
  - 空间复杂度：$O(1)$，仅使用常数级额外空间。

#### 2. 最优解法：Kadane 算法（动态规划）
- **核心逻辑**
  定义子问题：$S[i]$ 表示以 $nums[i]$ 结尾的最大子数组和。
  推导状态转移方程：
  $$S[i] = \max(nums[i], S[i-1] + nums[i])$$
  证明：以 $nums[i]$ 结尾的子数组只有两种可能：
  - 仅包含 $nums[i]$ 自身，和为 $nums[i]$；
  - 包含 $nums[i]$ 和以 $nums[i-1]$ 结尾的最优子数组，和为 $S[i-1]+nums[i]$。
  取两者最大值即为 $S[i]$。全局最大和为所有 $S[i]$ 的最大值。

- **核心代码**
  ```python
  class Solution(object):
      def maxSubArray(self, nums):
          current_max = global_max = nums[0]
          for num in nums[1:]:
              current_max = max(num, current_max + num)
              global_max = max(global_max, current_max)
          return global_max
  ```

- **复杂度分析**
  - 时间复杂度：$O(n)$，仅需一次遍历数组。
  - 空间复杂度：$O(1)$，仅使用两个变量维护状态。

---

## 二、 189. 轮转数组
### 题目描述
给定一个整数数组 `nums`，将数组中的元素向右轮转 `k` 个位置，要求**原地修改**数组。

### 解题思路
#### 1. 辅助数组法（基础思路）
- **核心逻辑**：使用辅助数组存储旋转后的元素，再通过切片赋值覆盖原数组。关键公式：元素 `nums[i]` 旋转后的位置为 $(i+k)\%n$，同时 `k = k\%n` 处理 `k` 大于数组长度的情况。
- **代码实现**
  ```python
  class Solution(object):
      def rotate(self, nums, k):
          n = len(nums)
          k = k % n
          copy_nums = [0] * n
          for i in range(n):
              copy_nums[(i + k) % n] = nums[i]
          nums[:] = copy_nums # 原地修改
  ```
- **复杂度分析**
  - 时间复杂度：$O(n)$，遍历一次数组。
  - 空间复杂度：$O(n)$，需要额外数组存储元素。

#### 2. 最优解法：三次反转法
- **核心逻辑**：数组向右轮转 `k` 位等价于将末尾 `k` 个元素移到开头，通过三次反转实现原地操作：
  1. 反转整个数组，将末尾 `k` 个元素移到头部（顺序反转）；
  2. 反转前 `k` 个元素，恢复头部元素顺序；
  3. 反转后 `n-k` 个元素，恢复尾部元素顺序。
- **核心代码**
  ```python
  class Solution(object):
      def rotate(self, nums, k):
          n = len(nums)
          k = k % n

          def reverse(left, right):
              while left < right:
                  nums[left], nums[right] = nums[right], nums[left]
                  left += 1
                  right -= 1

          reverse(0, n-1)   # 反转整个数组
          reverse(0, k-1)   # 反转前k个元素
          reverse(k, n-1)   # 反转后n-k个元素
  ```
- **复杂度分析**
  - 时间复杂度：$O(n)$，每个元素最多被反转两次，总操作数为 $2n$。
  - 空间复杂度：$O(1)$，仅使用常数级额外空间，满足原地修改要求。

---

## 三、 Python 排序算法（内置排序原理）
### 核心知识点
Python 内置排序的底层实现为 **Timsort** 算法，是归并排序与插入排序的混合算法，适用于真实场景中的大部分数据。

### 两种核心排序方法
| 方法 | 适用对象 | 是否原地修改 | 返回值 | 核心参数 |
|------|----------|--------------|--------|----------|
| `list.sort()` | 仅列表 | 是 | None | `key`：自定义排序依据；`reverse`：升序/降序 |
| `sorted()` | 所有可迭代对象 | 否 | 新列表 | `key`：自定义排序依据；`reverse`：升序/降序 |

### 关键用法示例
1. **基础排序**
   ```python
   nums = [3,1,4,1,5]
   nums.sort(reverse=True) # 降序原地排序
   sorted_nums = sorted(nums, key=abs) # 按绝对值排序
   ```
2. **复杂对象排序**
   ```python
   students = [{"name":"Tom", "score":85}, {"name":"Jerry", "score":92}]
   students.sort(key=lambda x: x["score"]) # 按分数升序
   ```

### 复杂度分析
- 时间复杂度：平均 $O(n\log n)$，最坏 $O(n\log n)$。
- 空间复杂度：$O(n)$（Timsort 需临时空间存储归并片段）。
- 特性：**稳定排序**，相同 `key` 的元素保持原顺序。

---

## 总结
1. 最大子数组和的最优解为 **Kadane 算法**，动态规划思想降低时间复杂度至 $O(n)$。
2. 轮转数组的最优解为 **三次反转法**，实现 $O(1)$ 空间复杂度的原地修改。
3. Python 内置排序依赖 **Timsort**，兼顾效率与实用性，`key` 参数是自定义排序的核心。

# LeetCode 高频数组/矩阵题解总结（238、41）
本文汇总今日讲解的三道经典算法题，从**暴力解法→逐步优化→最优解**完整呈现思路演进，包含解题思路、数学证明、优化逻辑、各阶段核心代码及复杂度分析，兼顾细节与实用性，适合系统学习。

## 一、LeetCode 238. 除了自身以外数组的乘积
### 题目描述
给定整数数组 `nums`，返回数组 `answer`，其中 `answer[i]` 等于 `nums` 中除 `nums[i]` 外所有元素的乘积，**禁止使用除法**，且时间复杂度为 O(n)。

示例：
输入：`nums = [1,2,3,4]` → 输出：`[24,12,8,6]`

---

### 优化过程：从 O(n) 空间 → O(1) 空间
#### 阶段1：基础解法（O(n) 空间，左右乘积数组）
**思路**：分别创建「左侧乘积数组」和「右侧乘积数组」，最后对应位置相乘得到结果。
- 左侧数组 `L`：`L[i]` 表示 `nums[0]~nums[i-1]` 的乘积；
- 右侧数组 `R`：`R[i]` 表示 `nums[i+1]~nums[n-1]` 的乘积；
- 结果：`answer[i] = L[i] × R[i]`。

**核心代码**：
```python
def productExceptSelf(nums):
    n = len(nums)
    # 初始化左右乘积数组
    L = [1] * n  # 左侧乘积
    R = [1] * n  # 右侧乘积
    answer = [1] * n

    # 计算左侧乘积
    for i in range(1, n):
        L[i] = L[i-1] * nums[i-1]

    # 计算右侧乘积
    for i in range(n-2, -1, -1):
        R[i] = R[i+1] * nums[i+1]

    # 合并结果
    for i in range(n):
        answer[i] = L[i] * R[i]

    return answer
```

**复杂度分析**：
- 时间复杂度：O(n)，三次线性遍历；
- 空间复杂度：O(n)，需额外存储 `L` 和 `R` 两个数组。

#### 阶段2：优化解法（O(1) 空间，原地复用）
**优化思路**：无需单独存储 `L` 和 `R`，用结果数组复用左侧乘积，用变量实时计算右侧乘积，节省空间。
- 第一次遍历：结果数组直接存左侧乘积，替代 `L` 数组；
- 第二次反向遍历：用 `right_product` 变量实时计算右侧乘积，直接与结果数组相乘，替代 `R` 数组。

**核心代码**：
```python
def productExceptSelf(nums):
    n = len(nums)
    answer = [1] * n  # 复用结果数组存储左侧乘积
    
    # 计算左侧乘积（替代L数组）
    left_product = 1
    for i in range(n):
        answer[i] = left_product
        left_product *= nums[i]
    
    # 计算右侧乘积并合并（替代R数组，变量实时计算）
    right_product = 1
    for i in range(n-1, -1, -1):
        answer[i] *= right_product
        right_product *= nums[i]
    
    return answer
```

**复杂度分析**：
- 时间复杂度：O(n)，仅两次线性遍历；
- 空间复杂度：O(1)，除输出数组外，仅用两个临时变量，满足进阶要求。

---

## 二、LeetCode 41. 缺失的第一个正数
### 题目描述
给定未排序整数数组 `nums`，找出**未出现的最小正整数**，要求时间复杂度 O(n)、空间复杂度 O(1)。

示例：
输入：`nums = [3,4,-1,1]` → 输出：`2`
输入：`nums = [7,8,9,11,12]` → 输出：`1`

---

### 优化过程：从 O(n) 空间 → O(1) 空间
#### 阶段1：基础解法（O(n) 空间，哈希表）
**思路**：用哈希表存储数组中所有正整数，再从 1 开始遍历，第一个不在哈希表中的数即为答案。
- 优点：思路直观，易实现；
- 缺点：需额外 O(n) 空间存储哈希表，不满足题目进阶要求。

**核心代码**：
```python
def firstMissingPositive(nums):
    n = len(nums)
    # 用集合存储所有正整数
    positive_nums = set()
    for num in nums:
        if num > 0:
            positive_nums.add(num)

    # 从1开始查找缺失的最小正整数
    for i in range(1, n+2):
        if i not in positive_nums:
            return i
```

**复杂度分析**：
- 时间复杂度：O(n)，两次线性遍历；
- 空间复杂度：O(n)，需存储哈希表。

#### 阶段2：优化解法（O(1) 空间，抽屉原理+原地哈希）
**数学证明（抽屉原理）**：
设数组长度为 n，缺失的最小正整数一定在 `[1, n+1]` 范围内：
- 若数组包含 `1~n` 所有正整数 → 缺失数为 `n+1`；
- 若数组不包含 `1~n` 中某个数 → 缺失数为该数（最小未出现者）。

**优化思路**：利用数组下标与正整数的对应关系（数字 k 对应下标 k-1），通过**原地交换**将 `1~n` 的数归位，无需额外空间。
- 仅处理 `1~n` 范围内的数，负数、0 及大于 n 的数直接忽略；
- 用 `while` 循环确保每个数归位，避免单次 `for` 循环漏处理。

**核心代码**：
```python
def firstMissingPositive(nums):
    n = len(nums)
    
    # 原地归位：数字k → 下标k-1
    for i in range(n):
        # 仅处理有效范围的数，且未归位时交换
        while 1 <= nums[i] <= n and nums[nums[i]-1] != nums[i]:
            nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
    
    # 查找第一个未归位的位置，即为答案
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    
    # 1~n全部存在，返回n+1
    return n + 1
```

**复杂度分析**：
- 时间复杂度：O(n)，每个数最多交换归位一次，两次线性遍历；
- 空间复杂度：O(1)，仅用常数级变量，原地操作。

---

## 三、LeetCode 73. 矩阵置零
### 题目描述
给定 m×n 矩阵，若某个元素为 0，则将其所在行和列全部置 0，要求**原地修改**，进阶要求空间复杂度 O(1)。

示例：
输入：`matrix = [[1,1,1],[1,0,1],[1,1,1]]` → 输出：`[[1,0,1],[0,0,0],[1,0,1]]`

---

### 优化过程：从 O(mn) 空间 → O(m+n) 空间 → O(1) 空间
#### 阶段1：暴力解法（O(mn) 空间，记录所有0坐标）
**思路**：先遍历矩阵，记录所有 0 的坐标，再根据坐标将对应行和列置 0。
- 优点：思路直观，完全避免“边遍历边修改”的干扰；
- 缺点：最坏情况下（矩阵全为0），需 O(mn) 空间存储坐标，空间效率极低。

**核心代码**：
```python
def setZeroes(matrix):
    m = len(matrix)
    n = len(matrix[0])
    zero_positions = []  # 存储所有0的坐标

    # 第一步：记录所有0的位置
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                zero_positions.append((i, j))
    
    # 第二步：根据坐标置零对应行和列
    for i, j in zero_positions:
        # 置零第i行
        for k in range(n):
            matrix[i][k] = 0
        # 置零第j列
        for k in range(m):
            matrix[k][j] = 0
```

**复杂度分析**：
- 时间复杂度：O(m×n)，两次线性遍历；
- 空间复杂度：O(mn)，最坏情况存储所有元素坐标。

#### 阶段2：优化解法（O(m+n) 空间，行/列标记数组）
**优化思路**：无需记录所有0坐标，只需记录「哪些行需要置零」「哪些列需要置零」，用两个一维数组替代二维坐标列表，空间复杂度降至 O(m+n)。
- 行标记数组 `row`：`row[i] = True` 表示第 i 行需要置零；
- 列标记数组 `col`：`col[j] = True` 表示第 j 列需要置零。

**核心代码**：
```python
def setZeroes(matrix):
    m = len(matrix)
    n = len(matrix[0])
    row = [False] * m  # 标记需要置零的行
    col = [False] * n  # 标记需要置零的列

    # 第一步：标记需要置零的行和列
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                row[i] = True
                col[j] = True
    
    # 第二步：根据标记置零行
    for i in range(m):
        if row[i]:
            for j in range(n):
                matrix[i][j] = 0
    
    # 第三步：根据标记置零列
    for j in range(n):
        if col[j]:
            for i in range(m):
                matrix[i][j] = 0
```

**复杂度分析**：
- 时间复杂度：O(m×n)，三次线性遍历；
- 空间复杂度：O(m+n)，用两个一维数组存储标记，空间效率大幅提升。

#### 阶段3：最优解法（O(1) 空间，首行首列标记法）
**优化思路**：利用**矩阵首行、首列作为标记位**，替代 `row` 和 `col` 数组，空间复杂度降至 O(1)。
- 关键：首行、首列既要做标记，又可能原本有0，需用 `row0`、`col0` 提前记录原始状态，避免标记覆盖原始信息；
- 步骤：先标记→再置零非首行首列→最后置零首行首列。

**核心代码**：
```python
def setZeroes(matrix):
    m = len(matrix)
    n = len(matrix[0])
    row0 = False  # 标记首行是否有0
    col0 = False  # 标记首列是否有0
    
    # 1. 记录首行、首列原始状态（避免标记覆盖）
    for j in range(n):
        if matrix[0][j] == 0:
            row0 = True
            break
    for i in range(m):
        if matrix[i][0] == 0:
            col0 = True
            break
    
    # 2. 用首行首列标记需置零的行和列（仅遍历非首行首列）
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0  # 标记第i行
                matrix[0][j] = 0  # 标记第j列
    
    # 3. 根据标记置零非首行首列元素
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    
    # 4. 置零首行、首列（根据原始标记）
    if row0:
        for j in range(n):
            matrix[0][j] = 0
    if col0:
        for i in range(m):
            matrix[i][0] = 0
```

**复杂度分析**：
- 时间复杂度：O(m×n)，四次线性遍历；
- 空间复杂度：O(1)，仅用两个布尔变量，满足题目所有要求。

---


### 通用优化技巧
1. **空间复用**：优先复用输入/输出空间，减少额外数组使用；
2. **标记简化**：从记录具体位置→记录行/列状态→利用自身空间做标记，逐步降低空间复杂度；
3. **数学推导**：通过数学原理（如抽屉原理）缩小问题范围，减少无效计算；
4. **遍历顺序**：正向/反向遍历结合，简化乘积、标记等逻辑。