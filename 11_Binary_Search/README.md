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

### 二、 核心破局思路：“一刀切”理论（划重点）

忘记数组，我们先回想一下**中位数（Median）的本质是什么？**
中位数的本质是把一个集合**“一刀切成长度相等的两半”**，并且保证：**左半边的所有数都 $\le$ 右半边的所有数。**

既然我们有两个数组 `nums1` 和 `nums2`，如果我们要找它们合并后的中位数，其实就是在 `nums1` 里切一刀，在 `nums2` 里也切一刀，把它们各自切成左右两半。

假设我们把它们切成了这样：
```text
左半边集合                |  右半边集合
nums1[0], nums1[1]... nums1[i-1]  |  nums1[i], nums1[i+1]... nums1[m-1]
nums2[0], nums2[1]... nums2[j-1]  |  nums2[j], nums2[j+1]... nums2[n-1]
```

为了让这条“切分线”变成完美的“中位数切分线”，它必须同时满足**两个条件**：

#### 条件 1：左右两边的人数必须一样多
也就是说，`nums1` 左边的人数（`i` 个）加上 `nums2` 左边的人数（`j` 个），必须等于总人数的一半！
* 如果总长度 $(m+n)$ 是偶数：`i + j = (m + n) / 2`
* 如果总长度 $(m+n)$ 是奇数：我们让左边多放一个人，`i + j = (m + n + 1) / 2`
* （其实这两个公式可以合并成：**`i + j = (m + n + 1) // 2`**）

**💡 神仙推导**：既然 `i + j` 是一个固定值，那么**只要我确定了在 `nums1` 里切哪（即 `i` 的值），`nums2` 里切哪（即 `j` 的值）就自动确定了！** $j = \frac{m+n+1}{2} - i$。

#### 条件 2：左边的最大值，必须 $\le$ 右边的最小值
* `nums1` 左边最大的是 `nums1[i-1]`，它必须 $\le$ `nums2` 右边最小的 `nums2[j]`。
* `nums2` 左边最大的是 `nums2[j-1]`，它必须 $\le$ `nums1` 右边最小的 `nums1[i]`。
（数组本身已经是有序的了，所以 `nums1[i-1] <= nums1[i]` 是天然成立的）。

---

### 三、 把问题转化为：对 `nums1` 进行二分查找！

现在，这道题完全变成了你最熟悉的“二分查找找边界”问题：
我们只需要在**较短的那个数组（假设是 `nums1`，长度为 `m`）**中，二分查找切分线的位置 `i`（范围是 `0` 到 `m`）。

* **初始化**：`left = 0`, `right = m`。
* **二分猜测**：`i = left + (right - left) // 2`。
* **自动计算**：`j = (m + n + 1) // 2 - i`。
* **检查我们猜的这一刀对不对**：
  * 如果 `nums1[i-1] > nums2[j]`：说明 `nums1` 左边的数太大了，说明我们在 `nums1` 里的**这刀切得太靠右了**。我们需要把 `i` 往左移 $\rightarrow$ `right = i - 1`。
  * 如果 `nums2[j-1] > nums1[i]`：说明 `nums2` 左边的数太大了（也就是 `nums1` 左边的数太少了），我们在 `nums1` 里**这刀切得太靠左了**。我们需要把 `i` 往右移 $\rightarrow$ `left = i + 1`。
  * **否则**：太完美了！这一刀刚好满足条件！跳出循环算答案！

---

### 四、 核心代码实现与防越界机制（附详细注释）

这里有一个极具工程美感的技巧：如果切分线刚好在最边缘（比如 `i=0`，说明 `nums1` 左边没有任何元素），那左边最大值是什么？我们可以假设它是一个**超级小的值（负无穷 `-inf`）**，这样无论如何它都会 $\le$ 右边的数。同理，右边没有元素就假设为**正无穷 `inf`**。

```python
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # 💡 神仙细节 1：永远确保对较短的数组进行二分查找。
        # 为什么？因为如果对长数组二分，i 的值可能很大，导致 j 算出负数（越界）！
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        m, n = len(nums1), len(nums2)
        
        # 在 nums1 的区间[0, m] 里寻找最完美的切分线 i
        left, right = 0, m
        
        while left <= right:
            # i 是 nums1 的切分线，j 是 nums2 的切分线
            i = left + (right - left) // 2
            j = (m + n + 1) // 2 - i
            
            # 💡 神仙细节 2：处理边界的“无穷大/无穷小”
            # nums1_left_max: nums1 切分线左边的最大值（如果左边空了，就是负无穷）
            nums1_left_max = float('-inf') if i == 0 else nums1[i - 1]
            # nums1_right_min: nums1 切分线右边的最小值（如果右边空了，就是正无穷）
            nums1_right_min = float('inf') if i == m else nums1[i]
            
            # nums2 同理
            nums2_left_max = float('-inf') if j == 0 else nums2[j - 1]
            nums2_right_min = float('inf') if j == n else nums2[j]
            
            # 开始判断这一刀切得对不对？
            if nums1_left_max <= nums2_right_min and nums2_left_max <= nums1_right_min:
                # 🎯 找到了完美的切分线！
                # 奇数情况：中位数就是左半边的最大值
                if (m + n) % 2 == 1:
                    return max(nums1_left_max, nums2_left_max)
                # 偶数情况：中位数是左边最大值和右边最小值的平均数
                else:
                    return (max(nums1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min)) / 2.0
                    
            elif nums1_left_max > nums2_right_min:
                # nums1 左边太大了，这一刀切得太靠右了，往左逼近
                right = i - 1
            else:
                # nums2 左边太大了，说明 nums1 左边给的太少了，往右逼近
                left = i + 1
```

### 五、 复杂度分析

* **时间复杂度**：$O(\log(\min(m, n)))$。我们只对较短的那个数组（长度为 $\min(m,n)$）进行了二分查找。这是比题目要求的 $O(\log(m+n))$ 还要极致的**终极最优解**！
* **空间复杂度**：$O(1)$。只用了 `left`, `right`, `i`, `j` 等几个常数级指针。

---

### 📝 证明的起点：中位数的绝对定义
假设把 `nums1` 和 `nums2` 融合成一个完整的、长度为 $L = m + n$ 的**严格升序数组 $A$**。
根据中位数的数学定义：
*   **当 $L$ 为偶数时**：中位数是数组 $A$ 最中间两个数的平均值，即 $\frac{A[L/2 - 1] + A[L/2]}{2}$。
*   **当 $L$ 为奇数时**：中位数是数组 $A$ 最中间的那个数，即 $A[(L - 1) / 2]$。

换句话说，求中位数的本质，就是把数组 $A$ **切成长度特定的“左半集 (Left)”和“右半集 (Right)”**。
我们要证明的，就是通过你的条件切出来的 Left 和 Right，**恰好等价于数组 $A$ 的前一半和后一半**。

---

### 🔍 证明步骤 1：证明 Left 集合里的所有数 $\le$ Right 集合里的所有数

根据你的切割方法：
*   **Left 集合** 包含：`nums1[0...i-1]` 和 `nums2[0...j-1]`。
*   **Right 集合** 包含：`nums1[i...m-1]` 和 `nums2[j...n-1]`。

我们要找 Left 集合的最大值 $L_{max}$，和 Right 集合的最小值 $R_{min}$：
1. 因为原数组有序，所以 `nums1` 左边最大的是 `nums1[i-1]`，`nums2` 左边最大的是 `nums2[j-1]`。
   于是，**$Left$ 的最大值 $L_{max} = \max(\text{nums1}[i-1], \text{nums2}[j-1])$**。
2. 同理，`nums1` 右边最小的是 `nums1[i]`，`nums2` 右边最小的是 `nums2[j]`。
   于是，**$Right$ 的最小值 $R_{min} = \min(\text{nums1}[i], \text{nums2}[j])$**。

根据**条件 2**的设定：
*   `nums1[i-1] <= nums2[j]` （交叉小于等于）
*   `nums2[j-1] <= nums1[i]` （交叉小于等于）
并且由原数组有序可知：
*   `nums1[i-1] <= nums1[i]` （内部自然小于等于）
*   `nums2[j-1] <= nums2[j]` （内部自然小于等于）

**结合这四个不等式，可以得出绝对的结论**：
`nums1[i-1]` 和 `nums2[j-1]` 构成的集合中，**任何一个数**，都必然 $\le$ `nums1[i]` 和 `nums2[j]` 构成的集合中的**任何一个数**。
即：**$L_{max} \le R_{min}$**。

**【阶段结论 1】**：既然 Left 里的最大数，都不超过 Right 里的最小数。这就意味着，如果我们把这两个集合合并成一个大的升序数组 $A$，**Left 集合里的所有元素，一定会完美、严丝合缝地占据数组 $A$ 的最前面位置；Right 集合的元素会占据后面的位置。**

---

### 🔍 证明步骤 2：证明中位数必定在切割点上产生

有了阶段结论 1（Left 必然排在 Right 前面），我们现在引入**条件 1**（人数的控制），来看看会发生什么。

#### 🟢 情况 A：总长度 $L = m + n$ 是偶数
根据条件 1 公式：`i + j = (m + n) / 2 = L / 2`。
这意味着 Left 集合里有 $L/2$ 个元素。
根据阶段结论 1，Left 占据了融合数组 $A$ 的前 $L/2$ 个位置，即索引 `0` 到 `L/2 - 1`。
Right 占据了剩下的位置，索引 `L/2` 到 `L - 1`。

*   数组 $A$ 最中间左边的数 $A[L/2 - 1]$，刚好就是 Left 集合的最后一个（也就是最大的那个）数，即 **$L_{max}$**。
*   数组 $A$ 最中间右边的数 $A[L/2]$，刚好就是 Right 集合的第一个（也就是最小的那个）数，即 **$R_{min}$**。

根据中位数定义：
中位数 $= \frac{A[L/2 - 1] + A[L/2]}{2} = \frac{L_{max} + R_{min}}{2} = \frac{\max(\text{nums1}[i-1], \text{nums2}[j-1]) + \min(\text{nums1}[i], \text{nums2}[j])}{2}$。
**推导完全成立！**

#### 🟢 情况 B：总长度 $L = m + n$ 是奇数
根据条件 1 公式：`i + j = (m + n + 1) / 2 = (L + 1) / 2`。
这意味着 Left 集合比 Right 集合**多放了 1 个元素**。
Left 的大小是 $(L+1)/2$。
根据阶段结论 1，Left 占据了融合数组 $A$ 的前 $(L+1)/2$ 个位置，即索引 `0` 到 `(L-1)/2`。

我们要找的中位数，根据奇数定义，刚好是融合数组 $A$ 的第 $(L-1)/2$ 个索引上的元素。
这个位置，**不偏不倚，恰好就是 Left 集合里的最后一个元素！**

而 Left 集合的最后一个元素，必然是 Left 里的最大值（因为已经排序好了），即 **$L_{max}$**。
所以：
中位数 $= L_{max} = \max(\text{nums1}[i-1], \text{nums2}[j-1])$。
**推导完全成立！**
