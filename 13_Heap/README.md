# 🚀 算法精进笔记：Top K 问题的全维度降维打击

> **💡 核心心法**：
> 面对“求第 K 大 / 前 K 个高频”的 Top K 问题，永远不要去进行全量排序（$O(N \log N)$）。
> **常规武器**：维护一个大小为 K 的最小堆（$O(N \log K)$）。
> **终极武器**：利用频率特性进行「桶排序」，或利用分治思维进行「快速选择 QuickSelect」，将极限时间复杂度强行拉入 **$O(N)$** 的领域。

---

## 🟢 一、 力扣 215. 数组中的第K个最大元素 (Top K 守门员)

### 📝 解题思路 (大小为 K 的最小堆)
求“最大”的 K 个数，反而要用**最小堆**。我们维护一个容量严格为 K 的最小堆，堆顶永远是这 K 个数里面最小的（也就是 Top K 的门槛）。
遍历数组时，遇到比堆顶大的数，就踢掉堆顶，把自己加进去。遍历结束后，堆顶就是第 K 大的元素。

### 🚨 极客避坑指南 (切片的隐形内存溢出)
很多新手会写 `for num in nums[k:]` 来遍历剩余元素。
**致命缺陷**：Python 的列表切片 `nums[k:]` 会在底层开辟一块全新的内存，拷贝剩下的 $N-K$ 个元素！这直接导致空间复杂度从原本完美的 $O(K)$ 瞬间退化崩溃成 $O(N)$。在处理海量日志（如 10 亿条数据找 Top 10）时会直接 OOM。
**完美解法**：老老实实使用 `range(k, len(nums))` 通过索引遍历，坚决不切片！

### 💻 核心代码 (Python)
```python
import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        # 1. 截取前 K 个元素，并在 O(K) 时间内原地建堆 (合法拷贝，占用 O(K) 空间)
        min_heap = nums[:k]
        heapq.heapify(min_heap) 
        
        # 2. 通过索引遍历剩下的元素，坚决避免 nums[k:] 造成的 O(N) 内存泄漏！
        for i in range(k, len(nums)):
            # 3. 完美剪枝：只有比堆顶门槛高的，才有资格进堆
            if nums[i] > min_heap[0]:
                # heapreplace 结合了 pop 和 push，且只需 1 次向下调整，效率极高
                heapq.heapreplace(min_heap, nums[i])
                
        return min_heap[0]
```
### ⏱ 复杂度分析
*   **时间复杂度**：$O(N \log K)$。建堆 $O(K)$，遍历剩余元素并调整堆 $O((N-K) \log K)$。
*   **空间复杂度**：严格 $O(K)$。只维护了大小为 K 的堆。

---

## 🔴 二、 力扣 347. 前 K 个高频元素 (四重境界极限拉扯)

### 🗡️ 境界一：工业生产环境王炸法 (API 调用)
利用 Python 底层高度优化的 C 语言扩展库。
```python
from collections import Counter
class Solution:
    def topKFrequent(self, nums, k):
        return [num for num, freq in Counter(nums).most_common(k)]
```
*   **黑盒揭秘**：`Counter(nums)` 耗时 $O(N)$。当 $k < N$ 时，`most_common(k)` 底层 C 源码其实就是直接调用了 `heapq.nlargest`，等价于手写最小堆。
*   **时空复杂度**：时间 $O(N \log K)$，空间 $O(N)$。工程常数极小，跑得最快，但面试不能只写这个。

### 🛡️ 境界二：白板面试满分标准解 (手写最小堆)
利用 `(频率, 数字)` 的元组特性，巧妙让 `heapq` 根据频率自动维护 Top K 门槛。
```python
from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums, k):
        freq_map = defaultdict(int)
        for num in nums: freq_map[num] += 1
        
        min_heap =[]
        for num, freq in freq_map.items():
            if len(min_heap) < k:
                heapq.heappush(min_heap, (freq, num))
            elif freq > min_heap[0][0]:
                heapq.heapreplace(min_heap, (freq, num))
                
        return [num for freq, num in min_heap]
```
*   **时空复杂度**：时间 $O(N \log K)$，空间 $O(N)$（哈希表占用）。应对常规大厂面试足矣。

### 👑 境界三：时间极客法 (O(N) 桶排序 Bucket Sort)
**核心心法**：一个数字出现的频率，绝对不可能超过数组总长度 $N$。因此可以用一个长度为 $N+1$ 的数组作为“频率桶”。
```python
class Solution:
    def topKFrequent(self, nums, k):
        from collections import Counter
        freq_map = Counter(nums)
        
        # 坑点：必须用 for 循环创建独立的空列表，绝不能用 [[]] * (N+1) 导致引用灾难！
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in freq_map.items():
            buckets[freq].append(num)
            
        ans =[]
        for i in range(len(buckets) - 1, 0, -1):
            if buckets[i]:
                ans.extend(buckets[i])
            if len(ans) >= k:
                break
        return ans[:k]
```
*   **时间复杂度深度剖析**：严格 $O(N)$。但带有常数项 4 —— 统计频率 $O(N)$ + 创建空桶 $O(N)$ + 入桶 $O(N)$ + 倒序出桶 $O(N)$ = $4 \times O(N)$。大量内存分配导致实际运行可能不如堆排。
*   **空间复杂度**：$O(N)$。若频率极端稀疏，会导致极大的空桶内存浪费。

### 🚀 境界四：极致原地分治法 (O(N) 快速选择 QuickSelect)
**核心心法**：“只找不排”。选定 Pivot，比它频次高的扔左边。如果 Pivot 落在了第 $K$ 个坑位，直接全剧终！
```python
import random
from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        freq_dict = Counter(nums)
        unique_nums = list(freq_dict.keys())
        
        # Lomuto 划分法：高频在左，低频在右
        def partition(left, right, pivot_index):
            pivot_freq = freq_dict[unique_nums[pivot_index]]
            # 1. 恭请老大靠边站 (藏到最右侧)
            unique_nums[pivot_index], unique_nums[right] = unique_nums[right], unique_nums[pivot_index]
            store_index = left
            # 2. 检票员大清洗 (比老大的大的全扔到左侧)
            for i in range(left, right):
                if freq_dict[unique_nums[i]] >= pivot_freq:
                    unique_nums[store_index], unique_nums[i] = unique_nums[i], unique_nums[store_index]
                    store_index += 1
            # 3. 恭迎老大归位 (检票员当前的位置就是老大的终生坑位)
            unique_nums[right], unique_nums[store_index] = unique_nums[store_index], unique_nums[right]
            return store_index
            
        def quickselect(left, right, k_smallest):
            if left == right: return
            # 必须加 random 防御最坏情况 O(N^2)
            pivot_index = random.randint(left, right)
            pivot_index = partition(left, right, pivot_index)
            
            if pivot_index == k_smallest:
                return # 🎯 一击必杀，完美落在第 K 坑位！
            elif pivot_index < k_smallest:
                quickselect(pivot_index + 1, right, k_smallest) # 目标在右半区
            else:
                quickselect(left, pivot_index - 1, k_smallest)  # 目标在左半区

        quickselect(0, len(unique_nums) - 1, k - 1)
        return unique_nums[:k]
```

#### 🧠 QuickSelect 深度复杂度复盘 (面试必杀技)
*   **K 为什么不参与时间复杂度？**
    $K$ 只是指挥方向的路标（If-Else 判定）。无论 $K$ 是多少，只要能按比例切分数组，递归排除的那一半山头是不计入遍历代价的。等比数列求和 $N + N/2 + N/4...$ 永远收敛于 $O(N)$。
*   **最好情况 (Best Case)**：$\Omega(N)$。第一次选的 Pivot 直接命中靶心（落在索引 $K-1$），执行一次 $N$ 遍历后直接返回，没有任何递归发生！
*   **平均情况 (Average Case)**：期望 $O(N)$。随机选 Pivot 保证较均匀切分。
*   **最坏情况 (Worst Case)**：$O(N^2)$。非酋附体，每次选中的 Pivot 都是极值，每次只能排除 1 个元素。这就是必须加上 `random.randint` 的根本原因。

---

## 🏆 347题 四种解法终极横向对比 (面试选型指南)

| 算法 / 维度 | 平均时间 | 最坏时间 | 额外空间占用 | 适用场景与优劣势 (Trade-offs) |
| :--- | :--- | :--- | :--- | :--- |
| **手写最小堆** | $O(N \log K)$ | $O(N \log K)$ | 极小 ($O(K)$) | **最优通用解**。流数据（Streaming Data）的唯一解法，稳定可靠，空间极其极致。|
| **Counter API** | $O(N \log K)$ | $O(N \log K)$ | 小 ($O(K)$) | **工业界首选**。底层全 C 语言执行，代码最短，常数耗时极小，但面试不体现底层逻辑。|
| **桶排序** | $O(N)$ | $O(N)$ (绝对铁血) | 最大 ($O(N)$桶) | **时间限制极严时选用**。真正的最坏 $O(N)$，但如果频率稀疏会造成极大的空桶内存浪费，且初始化空数组的常数项偏大。|
| **QuickSelect** | $O(N)$ | $O(N^2)$ (极小概率) | 原地操作 | **炫技与内存敏感时选用**。原地切分（In-place）不需大数组，逼格极高；但考验代码能力，必须加 random 防止退化。|




这份为你整合的**「堆 (Heap) 与动态极值终极突围笔记」**已经大功告成！

我将你今天攻克的**“数据流中位数（Hard）”**完美地融入了之前的 Top K 笔记体系中，并保留了我们讨论过的**“底层 memmove 碾压理论”、“双堆左右互搏术”以及“大厂顶级 Follow-up（进阶追问）”**。

这就是你在这个数据结构上最强硬的护城河，请直接复制并珍藏：

***

# 🚀 算法精进笔记：堆 (Heap) 与动态极值的全维度降维打击

> **💡 核心心法**：
> 1. **Top K 问题**：永远不要去进行全量排序（$O(N \log N)$）。利用「大小为 K 的最小堆」处理流数据，或利用「桶排序 / QuickSelect」将极限时间复杂度强行拉入 **$O(N)$** 的领域。
> 2. **动态极值 / 中位数问题**：只要不求全局有序，只求“宏观分块，微观无序”，**【堆 (Heap)】永远是第一候选人！**

## ⚫ 三、 力扣 295. 数据流的中位数 (动态极值与双堆法 Hard)

### 📝 解题思路 (宏观分块，阶级隔离)
中位数的本质是把数据**“精准劈成两半”**，我们根本不需要全局有序，只需要瞬间拿到：
1. **左半区（小个子）的最大值** $\rightarrow$ **大顶堆 (Max Heap)**
2. **右半区（高个子）的最小值** $\rightarrow$ **小顶堆 (Min Heap)**

**左右互搏术规矩**：
*   **人数平衡**：大顶堆的人数，最多比小顶堆多 1 个人。
*   **阶级隔离**：大顶堆的所有数 $\le$ 小顶堆的所有数。新来的数永远先过大顶堆，大顶堆把自己的老大“吐”给小顶堆，以此保证隔离。

### 🚀 极客探索过程 (工程常数 vs 大 O 理论)
*   **我的原生探索 ($O(N)$ 数组插入)**：利用 `bisect.insort`（二分查找 + 插入）来维护有序数组。由于 Python 底层基于连续内存的 C 语言 `memmove` 指令，且拥有极佳的 CPU Cache 命中率，在十几万数据规模下，它的实际运行时间居然吊打理论更优的树/堆结构！**（工业界暴力美学）**
*   **理论破局**：在面试中，数组插入最坏 $O(N)$ 是不被允许的，必须通过改变数据结构（使用堆），利用指针操作将插入复杂度强行压至绝对的 $O(\log N)$。

### 💻 核心代码 (Python 双堆法)
```python
import heapq

class MedianFinder(object):
    def __init__(self):
        self.max_heap =[] # 存较小的一半 (Python 需乘 -1 模拟大顶堆)
        self.min_heap =[] # 存较大的一半

    def addNum(self, num):
        # 1. 无脑先进大顶堆 (乘 -1)
        heapq.heappush(self.max_heap, -num)
        
        # 2. 阶级隔离：大顶堆交出老大，扔进小顶堆
        max_of_left = -heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap, max_of_left)
        
        # 3. 人数平衡：如果小顶堆人多了，还给大顶堆
        if len(self.min_heap) > len(self.max_heap):
            min_of_right = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -min_of_right)

    def findMedian(self):
        # 奇数情况：大顶堆多一个人，直接取堆顶
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        # 偶数情况：两堆平分秋色，各取堆顶求平均
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
```

### ⏱ 复杂度深度剖析
*   **`addNum` 时间复杂度**：**严格 $O(\log N)$**。每次插入最多经历 3 次 push/pop（常数倍数为 5），大 O 渐进法下极其稳定。
*   **`findMedian` 时间复杂度**：**极致 $O(1)$**。底层堆的极值永远存在数组 `[0]` 索引位，直接读取，无任何树遍历开销。
*   **空间复杂度**：**$O(N)$**。两个堆共同存储数据流的所有元素。

### 👑 面试官绝杀追问 (Follow-up)

**🔥 追问 1：如果数据流 100% 集中在 `[0, 100]`，怎么优化？**
**降维打击回答**：彻底抛弃堆！改用**「计数排序/桶排序」**思想。建立一个长度为 101 的频次数组 `count` 和一个总数变量 `total`。
`addNum` 时只需 `count[num] += 1`，时间降至绝对的 **$O(1)$**。`findMedian` 时只需遍历这 101 个桶累加人数寻找中位点，时间也是 **$O(1)$**！

**🔥 追问 2：如果 99% 在 `[0, 100]`，但有 1% 是极端越界的离群值（Outliers）？**
**架构级回答**：结合双堆法与计数法！`[0, 100]` 区间内依然用 `count` 数组 $O(1)$ 维护；建立 `less_count` 和 `greater_count` 记录异常数量。只有当中位数极小概率落在异常区时，才去维护极小/极大的额外堆。这种架构在省下 99% 内存和耗时的同时，保证了极高的健壮性。

***
