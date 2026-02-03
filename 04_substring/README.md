# 滑动窗口经典题目总结（力扣 560、239、76）
本文聚焦滑动窗口核心题型，涵盖**和为 K 的子数组**、**滑动窗口最大值**、**最小覆盖子串**三道经典题，从解题思路、核心代码、复杂度分析三个维度梳理，帮助快速掌握滑动窗口及相关优化技巧。

## 一、560. 和为 K 的子数组
### 题目描述
给定整数数组 `nums` 和整数 `k`，统计数组中和为 `k` 的连续子数组个数。

### 解题思路
核心思路：**前缀和 + 哈希表**（暴力解法效率过低，仅作思路参考）。
1. 前缀和定义：`preSum[i]` 表示数组前 `i` 个元素的和，满足 `preSum[0] = 0`，子数组 `[j, i-1]` 的和 = `preSum[i] - preSum[j]`；
2. 关键转化：若子数组和为 `k`，则 `preSum[j] = preSum[i] - k`，只需统计 `preSum[i] - k` 出现的次数；
3. 哈希表优化：记录每个前缀和出现的次数，遍历数组时实时查询，避免重复计算。

### 核心代码
```python
def subarraySum(nums, k):
    # 哈希表：key=前缀和，value=出现次数，初始化preSum=0出现1次（处理边界）
    pre_sum_map = {0: 1}
    pre_sum = 0  # 当前前缀和
    count = 0    # 统计符合条件的子数组个数
    
    for num in nums:
        pre_sum += num  # 更新当前前缀和
        # 查找preSum-k是否存在，存在则累加对应次数
        if (pre_sum - k) in pre_sum_map:
            count += pre_sum_map[pre_sum - k]
        # 更新哈希表，记录当前前缀和的出现次数
        pre_sum_map[pre_sum] = pre_sum_map.get(pre_sum, 0) + 1
    
    return count
```

### 复杂度分析
- 时间复杂度：O(n)，仅遍历一次数组，哈希表查询/更新均为 O(1)；
- 空间复杂度：O(n)，最坏情况下所有前缀和均不同，哈希表存储 n+1 个键值对。

## 二、239. 滑动窗口最大值
### 题目描述
给定整数数组 `nums` 和滑动窗口大小 `k`，返回每个滑动窗口内的最大值。

### 解题思路
核心思路：**单调递减双端队列**（暴力解法 O(nk) 会超时，需优化）。
1. 队列规则：存储数组索引，对应元素值**单调递减**，保证队列头部始终是当前窗口最大值的索引；
2. 窗口扩张：遍历数组时，移除队列尾部所有小于等于当前元素的索引（这些元素不可能成为后续窗口最大值），再加入当前索引；
3. 窗口收缩：检查队列头部索引是否超出窗口左边界，若超出则移除；
4. 结果记录：当窗口形成（遍历到第 k 个元素及之后），队列头部即为当前窗口最大值。

### 核心代码
```python
from collections import deque

def maxSlidingWindow(nums, k):
    q = deque()  # 单调递减队列，存储索引
    res = []     # 存储结果
    n = len(nums)
    
    for i in range(n):
        # 维护单调递减：移除尾部小于等于当前元素的索引
        while q and nums[i] >= nums[q[-1]]:
            q.pop()
        q.append(i)
        
        # 清理过期索引：移除超出窗口左边界的头部索引
        while q[0] <= i - k:
            q.popleft()
        
        # 窗口形成后，记录当前窗口最大值
        if i >= k - 1:
            res.append(nums[q[0]])
    
    return res
```

### 复杂度分析
- 时间复杂度：O(n)，每个元素仅入队、出队各一次；
- 空间复杂度：O(k)，队列最多存储 k 个索引（窗口大小）。

## 三、76. 最小覆盖子串
### 题目描述
给定字符串 `s` 和 `t`，返回 `s` 中涵盖 `t` 所有字符的最短连续子串，若无则返回空字符串。

### 解题思路
核心思路：**滑动窗口 + 哈希表**（双指针动态调整窗口大小）。
1. 需求统计：用哈希表 `need` 记录 `t` 中每个字符的需求数量；
2. 窗口扩张：右指针右移，将字符加入窗口，用哈希表 `window` 记录窗口内字符供给量，用 `valid` 标记已满足需求的字符种类数；
3. 窗口收缩：当 `valid` 等于 `need` 的键数（所有字符需求满足），尝试左移左指针缩小窗口，更新最小窗口的起始位置和长度；
4. 结果返回：遍历结束后，根据最小窗口信息截取子串，若无则返回空。

### 核心代码
```python
from collections import defaultdict

def minWindow(s, t):
    need = defaultdict(int)  # 记录t的字符需求
    window = defaultdict(int)  # 记录窗口内字符供给
    for char in t:
        need[char] += 1
    
    left = right = 0
    valid = 0  # 已满足需求的字符种类数
    start = 0  # 最小窗口起始索引
    min_len = float('inf')  # 最小窗口长度
    
    while right < len(s):
        # 窗口扩张：添加当前字符
        curr_char = s[right]
        right += 1
        if curr_char in need:
            window[curr_char] += 1
            if window[curr_char] == need[curr_char]:
                valid += 1
        
        # 窗口收缩：满足需求时尝试缩小
        while valid == len(need):
            # 更新最小窗口
            if right - left < min_len:
                start = left
                min_len = right - left
            
            # 移除左侧字符
            left_char = s[left]
            left += 1
            if left_char in need:
                if window[left_char] == need[left_char]:
                    valid -= 1
                window[left_char] -= 1
    
    # 返回结果，无则返回空
    return "" if min_len == float('inf') else s[start:start+min_len]
```

### 复杂度分析
- 时间复杂度：O(m + n)，`m`、`n` 分别为 `s`、`t` 长度，左右指针各遍历一次字符串；
- 空间复杂度：O(1)，字符集有限（仅大小写字母），哈希表存储的键值对数量固定。

## 核心技巧总结
1. **前缀和 + 哈希表**：适用于**连续子数组和**类问题，将子数组和转化为前缀和差值，快速统计次数；
2. **单调双端队列**：适用于**滑动窗口极值**类问题，维护队列单调性，保证头部为目标值，避免重复计算；
3. **滑动窗口 + 双哈希表**：适用于**子串覆盖**类问题，通过 `valid` 高效判断窗口有效性，动态调整窗口大小找最优解。