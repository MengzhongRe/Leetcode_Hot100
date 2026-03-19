# 🚀 算法精进笔记：二分查找核心突围 (Binary Search)

> **💡 核心心法**：二分查找的本质不是“找那个等于目标值的元素”，而是**“在一个单调的区间里，不断逼近和排除边界”**。
> **🔥 核心模板**：永远优先使用**闭区间**写法 `while left <= right`，并在计算中点时使用 `mid = left + (right - left) // 2` 防溢出。

---

## 🟢 1. 力扣 35. 搜索插入位置 (基础与插入点)

### 📝 解题思路
这是一道最经典的二分查找变体。题目要求“找到则返回索引，找不到则返回按顺序插入的位置”。
核心在于理解**循环结束的瞬间发生了什么**：当 `while left <= right` 结束时，一定是 `left > right`。此时 `left` 指向的恰好就是第一个大于 `target` 的元素位置，也就是完美的目标插入点。

### ⚠️ 易错点 (避坑指南)
1. **循环条件丢掉等号**：如果写成 `left < right`，在极端情况（如数组只有一个元素或目标值要插在末尾）时会直接跳过判断，导致结果错误。
2. **返回值写错**：找不到目标值时，**必须返回 `left`**，千万不要返回 `right`。

### 💻 核心代码 (Python)
```python
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid       # 命中，直接返回
            elif nums[mid] < target:
                left = mid + 1   # 目标在右侧，收缩左边界
            else:
                right = mid - 1  # 目标在左侧，收缩右边界
                
        return left              # 找不到时，left 就是天命插入点
```

### ⏱ 复杂度分析
* **时间复杂度**：$O(\log N)$，标准二分折半。
* **空间复杂度**：$O(1)$，仅使用了常数个指针变量。

---

## 🟡 2. 力扣 74. 搜索二维矩阵 (坐标映射降维打击)

### 📝 解题思路 & 优化过程
* **初级想法**：将二维矩阵真实地展开拼接成一个一维数组，然后套用 35 题的代码。但这样做需要开辟新的数组空间，时间和空间都退化为 $O(M \times N)$。
* **进阶优化（虚拟展平）**：既然矩阵的本质是一个严格递增的序列，我们可以**把二维矩阵假想成一维数组**，只需要找出“一维索引”与“二维坐标”的映射公式即可。
  * **行号**：`row = mid // 列数`
  * **列号**：`col = mid % 列数`

### ⚠️ 易错点 (避坑指南)
1. 边界条件：在开始前务必判断矩阵是否为空（`if not matrix:`）。
2. 列数提取：映射公式中的除数和取模数是**列数（`n`）**，千万别写成行数（`m`）。

### 💻 核心代码 (Python)
```python
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
            
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1  # 在假想的 1D 数组上设置双指针
        
        while left <= right:
            mid = left + (right - left) // 2
            
            # 🎯 核心魔法：1D 索引转 2D 坐标
            mid_val = matrix[mid // n][mid % n]
            
            if mid_val == target:
                return True
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return False
```

### ⏱ 复杂度分析
* **时间复杂度**：$O(\log(M \times N))$，相当于对总元素个数做了一次二分。
* **空间复杂度**：$O(1)$，没有真正去创建一维数组，实现了“既要又要”。

---

## 🔴 3. 力扣 34. 在排序数组中查找元素的第一个和最后一个位置 (双射求边界)

### 📝 解题思路 & 优化过程
* **初级想法（三段式）**：先二分找到任意一个等于 `target` 的 `mid`，然后以 `mid` 为界限，分别在左半边找左边界，在右半边找右边界。逻辑可行，但极易写出死循环。
* **进阶优化（独立两段式）**：写两个独立的二分查找函数，一个专门用来找左边界，一个专门用来找右边界。
  * **找左边界时**：遇到 `nums[mid] == target` 不要停，记录位置后，**继续向左收缩（`right = mid - 1`）**。
  * **找右边界时**：遇到 `nums[mid] == target` 不要停，记录位置后，**继续向右收缩（`left = mid + 1`）**。

### ⚠️ 易错点 (避坑指南)
1. **死循环陷阱**：遇到相等的情况时，千万不能写 `right = mid` 或 `left = mid`，必须配合加一或减一打破平衡。
2. **函数调用的括号**：在 Python 中，如果把闭包当作返回值，调用时千万别漏掉末尾的括号 `()`，否则返回的将是函数对象而不是执行结果。

### 💻 核心代码 (Python)
```python
class Solution(object):
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if not nums:
            return[-1, -1]

        # 🔍 专属武器 1：找左边界
        def get_left_border():
            left, right = 0, len(nums) - 1
            left_border = -1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    left_border = mid    # 记下当前位置
                    right = mid - 1      # 别停，继续往左边逼近！
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left_border
        
        # 🔍 专属武器 2：找右边界
        def get_right_border():
            left, right = 0, len(nums) - 1
            right_border = -1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    right_border = mid   # 记下当前位置
                    left = mid + 1       # 别停，继续往右边逼近！
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1  
            return right_border
        
        # 两次独立调用，高度对称，极其优雅
        return [get_left_border(), get_right_border()]
```

### ⏱ 复杂度分析
* **时间复杂度**：$O(\log N) + O(\log N) = O(\log N)$。执行了两次二分查找，常数项可以忽略。
* **空间复杂度**：$O(1)$，充分利用了闭包特性，没有开辟额外空间。


# 🚀 算法精进笔记：二分查找进阶 (旋转数组双璧)

> **💡 核心心法**：面对旋转排序数组，牢记**“一半乱序，一半必定绝对有序”**。
> 二分查找的威力不仅在于直接找目标，更在于**找特征点（断层/悬崖）**以及**利用局部有序性不断排除一半的错误答案**。

---

## 🟡 1. 力扣 33. 搜索旋转排序数组 (高频大厂题)

### 🗡️ 解法一：分治与模块化（你的原生解法 - 两次二分法）
**📝 解题思路**：
降维打击！将复杂问题拆解为两个简单的标准问题：
1. **找断点**：先通过一次二分查找到数组的“旋转点”（最大值）。
2. **切分区间**：以旋转点为界，将原数组劈成两个绝对纯粹的升序数组。
3. **独立查找**：根据 `target` 的大小判断它在哪一段，然后直接调用最基础的二分查找模板。

**💻 核心代码**：
```python
class Solution(object):
    def search(self, nums, target):
        n = len(nums)
        if n == 1: return 0 if nums[0] == target else -1

        # 第一步：找旋转点 (最大值)
        left, right = 0, n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid + 1]:  # 找到断点
                break
            if nums[mid] > nums[n - 1]:
                left = mid + 1
            else:
                right = mid - 1

        # 基础二分查找模板
        def binary_search(l, r):
            while l <= r:
                m = l + (r - l) // 2
                if nums[m] == target: return m
                if nums[m] < target: l = m + 1
                else: r = m - 1
            return -1

        # 第二步：分治查找 (利用变量存储，避免重复调用)
        res_left = binary_search(0, mid)
        return res_left if res_left != -1 else binary_search(mid + 1, n - 1)
```

### 👑 解法二：局部有序法（终极最优解 - 一次二分法）
**📝 优化过程**：
追求极致的 $1 \times \log n$ 遍历。不管怎么切，**数组必定有一半是绝对有序的**。
1. 判断哪一半是有序的（比较 `nums[left]` 和 `nums[mid]`）。
2. 判断 `target` 是否正好落在这个有序的区间范围内。
3. 在就收缩进去，不在就去另一半找。

**💻 核心代码**：
```python
class Solution(object):
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target: return mid
                
            # 左半段是有序的
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # 目标在左侧区间
                else:
                    left = mid + 1   # 否则去右侧找
                    
            # 右半段是有序的
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1   # 目标在右侧区间
                else:
                    right = mid - 1  # 否则去左侧找
                    
        return -1
```

### ⏱ 复杂度分析 (双解法通用)
* **时间复杂度**：$O(\log n)$。解法一常数项略大（约 $2\log n$），解法二是严格的 $1\log n$，但在大 O 渐进意义上完全等价。
* **空间复杂度**：$O(1)$。只使用了几个指针变量。

---

## 🟡 2. 力扣 153. 寻找旋转排序数组中的最小值

### 🛡️ 解法一：寻找“悬崖点”（你的原生模板 - 极度安全）
**📝 解题思路**：
完美复用 33 题思路。在一个由升序数组旋转得来的序列中，**唯一会出现前一个数大于后一个数的地方，就是首尾相接的那个“断层/悬崖”**。
通过 `while left <= right` 配合严格的 `+1/-1` 边界收缩，永远不会陷入死循环。

**💻 核心代码**：
```python
class Solution(object):
    def findMin(self, nums):
        n = len(nums)
        # 边界防御：数组未旋转（绝对升序）或只有一个元素
        if n == 1 or nums[0] < nums[n - 1]: return nums[0]
        
        left, right = 0, n - 1
        # 万能安全模板：寻找“悬崖点”
        while left <= right:
            mid = left + (right - left) // 2
            
            # 定位“悬崖”：前一个数大于后一个数
            if nums[mid] > nums[mid + 1]: 
                return nums[mid + 1]
                
            # 逼近逻辑：如果 mid 大于末尾，悬崖必定在右侧
            elif nums[mid] > nums[n - 1]: 
                left = mid + 1
            # 否则，悬崖必定在左侧
            else: 
                right = mid - 1
                
        return -1 
```

### 🗡️ 解法二：排除法（业界极简模板 - 左闭右开法）
**📝 优化过程**：
不找特征点，而是利用**“排除法”**。不断向里挤压区间，只要能把不是最小值的元素全排除，最后剩下的那个独苗必定是最小值。
**⚠️ 致命易错点**：为了保留真正的最小值，收缩右边界时必须写 `right = mid`。为了防止 `right = mid` 导致的无限死循环，外层循环**必须且只能**写成 `while left < right`！

**💻 核心代码**：
```python
class Solution(object):
    def findMin(self, nums):
        left, right = 0, len(nums) - 1
        
        # 必须是 <，目的是把最后区间收缩到只剩 1 个元素跳出循环
        while left < right:
            mid = left + (right - left) // 2
            
            # mid 值大于最右侧，说明最小值必定在右半边（且绝对不是 mid 本身）
            if nums[mid] > nums[right]:
                left = mid + 1
            # 否则，最小值必定在左半边（可能是 mid 本身，所以绝对不能 -1）
            else:
                right = mid
                
        # 循环结束时 left == right，剩下的独苗就是最小值
        return nums[left]
```

### ⏱ 复杂度分析 (双解法通用)
* **时间复杂度**：$O(\log n)$。每次都排除一半的区间。
* **空间复杂度**：$O(1)$。没有任何额外的数据结构开销。

---

> **🏆 面试实战指南**：
> 1. **关于 33 题**：在纸上白板推演时，解法一（你的解法）思路最清晰，不易出错；如果面试官要求“只能用一次 while”，立刻掏出解法二。
> 2. **关于 153 题**：自己做题或笔试时，强烈推荐**解法一**（因为闭区间模板兼容所有题型，心智负担极低）；阅读他人高赞题解时，要能秒懂**解法二**中 `<` 与 `right = mid` 是如何精妙配合防死循环的。