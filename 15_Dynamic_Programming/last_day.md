# 📖 每日算法笔记：背包思想与困难状态机的破局

## 🟢 一、LeetCode 416. 分割等和子集 (Medium)

### 📌 题目核心
将数组分成两部分，使得两部分和相等。
**本质**：转化为求一个容量为 `sum // 2` 的 **0-1 背包问题**。

### 🚀 解法一：一维动态规划（标准版）
#### 💡 思路详细
1. **基础剪枝**：如果总和是奇数，或者数组中最大值已经超过了 `sum // 2`，直接返回 `False`。
2. **状态定义**：`dp[j]` 表示是否能从数组中挑出若干个数，使得和恰好为 `j`。
3. **状态转移**：对于每一个数字 `num`，我们可以选择“放”或“不放”。
   `dp[j] = dp[j] or dp[j - num]`
4. **⚠️ 倒序遍历的灵魂**：因为每个数字只能用一次（0-1背包），所以内层循环遍历背包容量 `j` 时**必须倒序**（从 `target` 到 `num`）。如果正序遍历，前面的 `dp[j-num]` 更新后，会被后面的 `dp[j]` 再次利用，导致同一个数字被重复放入（这就变成完全背包了）。

#### 💻 核心代码
```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums_sum = sum(nums)
        if nums_sum % 2 != 0: return False
        
        target = nums_sum // 2
        # 极速剪枝：如果最大数字比目标还大，绝不可能凑出
        if max(nums) > target: return False
        
        dp =[False] * (target + 1)
        dp[0] = True

        for num in nums:
            # 必须倒序遍历！防止数字被重复使用
            for j in range(target, num - 1, -1):
                if dp[j - num]:
                    dp[j] = True
                    
        return dp[target]
```

---

### 🚀 解法二：集合求并集优化（Pythonic 神仙解法）
#### 💡 思路详细
抛弃了对具体容量容量 `j` 的硬性遍历，利用 Python 集合 (Set) 存储**当前所有能凑出来的和**。
遇到一个新数字 `num` 时，把集合里的**所有已有元素都加上 `num`**，生成一批新的和，然后与原来的集合合并。
**优势**：利用了数据的**稀疏性**，集合里只存真实存在的和，不用像数组 DP 那样去遍历大量为 `False` 的无效状态；且底层是 C 语言实现，速度极快。

#### 💻 核心代码
```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums_sum = sum(nums)
        if nums_sum % 2 != 0: return False
        target = nums_sum // 2
        
        dp = {0} # 初始化集合，和为0永远可以凑出
        for num in nums:
            # 集合推导式：当前所有可能和 加上新数字 num
            dp |= {v + num for v in dp if v + num <= target}
            
            # 提前结束：一旦凑出 target，直接下班
            if target in dp:
                return True
                
        return False
```

#### 📊 复杂度分析 (416题)
- **时间复杂度**：两者理论最坏皆为 $O(N \times \text{target})$，但 Set 解法利用稀疏性常数极小。
- **空间复杂度**：$O(\text{target})$。

***

## 🔴 二、LeetCode 32. 最长有效括号 (Hard) 【🔥重点拆解】

### 📌 题目核心
在只包含 `(` 和 `)` 的字符串中，找到**最长的、连续的**有效括号子串长度。
**痛点**：无效括号不仅有“右括号多了”（如 `())`），还有“左括号多了”（如 `(()`）。稍不留神就会导致状态断裂。

---

### 🚀 解法一：双向遍历（极致 O(1) 空间计数法）
#### 💡 思路详细
我们在用计数法单向遍历时，遇到 `(` 加一，遇到 `)` 减一：
- 如果 `右括号太多`，可以立刻判定前面的段落作废，计数器清零，这很好处理。
- **致命弱点**：如果 `左括号太多`（例如 `s = "()(()"`），单向遍历到结尾时，计数器没清零，但也无法确认中间哪段才是合法的，导致漏判或错判。

**破局点：再反向扫一遍！**
既然从左往右扫能完美排查“右括号过多”；那么**从右往左扫一遍**，不就能完美排查“左括号过多”了吗？两者取最大值，天衣无缝！

#### 💻 核心代码
```python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left = right = max_len = 0
        
        # 1. 从左往右（过滤右括号过多的干扰）
        for char in s:
            if char == '(': left += 1
            else: right += 1
            
            if left == right:
                max_len = max(max_len, 2 * right)
            elif right > left: # 右边超了，废弃重置
                left = right = 0
                
        # 2. 从右往左（过滤左括号过多的干扰）
        left = right = 0
        for char in reversed(s):
            if char == '(': left += 1
            else: right += 1
            
            if left == right:
                max_len = max(max_len, 2 * left)
            elif left > right: # 此时左边超了，废弃重置
                left = right = 0
                
        return max_len
```
#### ⚠️ 边界注意点
务必记得在第二遍遍历开始前，将 `left` 和 `right` 变量重新重置为 `0`。

---

### 🚀 解法二：一维动态规划（错位神级推导）
#### 💡 思路详细
> 这也是你今天踩坑最多，但最具数学美感的解法。

**1. 状态定义（带偏移的技巧）：**
通常我们设 `dp[i]` 为以 `s[i]` 结尾的长度。为了避免 `i-1` 越界，我们将 DP 数组多开一位：
**`dp[i+1]` 表示：以 `s[i]` 结尾的最长有效括号长度。**（即字符串里的第 `i` 个字符对应 `dp[i+1]`）。
如果 `s[i] == '('`，必定形不成有效结尾，直接是 `0`。

**2. 核心状态转移：**
当 `s[i] == ')'` 时，有两种情况：
*   **情况 A：紧紧相邻 `...()`**
    `s[i-1] == '('`。这对括号直接匹配！
    长度 = 前面的有效长度 + 2。
    公式：`dp[i+1] = dp[i-1] + 2`
*   **情况 B：跨越山海 `...))`**
    `s[i-1] == ')'`。这意味着前面可能有一整坨已经配对好的括号群体。我们需要跨过它们！
    - 这个群体的长度是多少？是 `dp[i]`。
    - 跨过去后，我们需要配对的左括号坐标在哪？`match_idx = i - dp[i] - 1`。
    - 如果 `s[match_idx] == '('`，说明跨越千山万水匹配成功了！
    - **匹配成功后的总长度 = （包在里面的群体长度） + 2 + （匹配成功的左括号前面的有效长度）**
    公式推导：`dp[i+1] = dp[i] + 2 + dp[match_idx]`  ➡️  **`dp[i+1] = dp[i] + 2 + dp[i - dp[i] - 1]`**

#### 💻 核心代码
```python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s: return 0
        
        n = len(s)
        # dp[k] 代表以 s[k-1] 结尾的最长有效括号长度 (长为 n+1)
        dp = [0] * (n + 1)

        for i in range(1, n):
            if s[i] == ')':
                # 情况 A：形如 "()"
                if s[i - 1] == '(':
                    dp[i + 1] = dp[i - 1] + 2
                    
                # 情况 B：形如 "))"，需要跨过前面整个已配对的段落
                else:
                    match_idx = i - dp[i] - 1
                    # 必须防范 match_idx < 0 (Python负数索引陷阱)
                    if match_idx >= 0 and s[match_idx] == '(':
                        # dp[i] 是中间包住的长度，2 是新配对的括号，dp[match_idx] 是最前面的长度
                        dp[i + 1] = dp[i] + 2 + dp[match_idx]
                                    
        return max(dp)
```

#### ⚠️ 边界注意点（避坑指南）
1. **Python 的负数索引背刺**：
   在判断 `s[match_idx] == '('` 时，**一定一定**要加上 `match_idx >= 0`。否则在 `match_idx = -1` 时，Python 会直接去读取字符串倒数第一个字符！比如测试用例 `s = "())(("`，如果不加限制，代码会错把结尾的 `(` 当成配对对象。
2. **DP 下标的对齐**：
   在情况 B 寻找最前面的有效长度时，使用的是 `dp[match_idx]`，千万不要写成 `dp[match_idx - 1]`，因为我们的 DP 数组天然整体向右平移了 1 位。

#### 📊 复杂度分析 (32题)
- **时间复杂度**：双向遍历与 DP 都是 $O(N)$。字符串只遍历 1~2 遍。
- **空间复杂度**：双向遍历 $O(1)$（最优）；动态规划 $O(N)$（需维护状态数组）。