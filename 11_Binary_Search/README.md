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