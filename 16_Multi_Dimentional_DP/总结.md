### 🧠 一、 认知升级：一维与多维的区别在哪？

在一维 DP 中，我们的状态通常是：`dp[i]` 表示“前 `i` 个元素”或者“以第 `i` 个元素结尾”的最值。
但在多维 DP 中，**一个维度不足以描述当前的状态**。我们需要用到 $i, j$ 甚至 $k$。

多维 DP 主要用来解决以下三大类场景：
1. **网格型（Grid）**：二维地图上的移动。
2. **双序列型（Two Strings / Arrays）**：对比两个字符串或数组（大厂高频！）。
3. **区间型（Interval）**：在一个序列中，左右端点同时收缩。

---

### 🗺️ 二、 循序渐进的刷题路线图 (Roadmap)

强烈建议你按照以下 **4 个阶段** 依次推进，千万不要跳跃！

#### 🟢 阶段一：网格地图型（新手村）
**特点**：极其直观，状态 $dp[i][j]$ 直接对应坐标 $(i, j)$，通常只能从上方 $(i-1, j)$ 或左方 $(i, j-1)$ 转移而来。
*   **[62] 不同路径 (Medium)**：纯粹的加法，入门必刷。
*   **[64] 最小路径和 (Medium)**：加了权重的求最小值。
*   **[63] 不同路径 II (Medium)**：加入了障碍物，练习条件判断和初始化。
*   **[221] 最大正方形 (Medium)**：状态转移公式极为精妙，必刷经典。

#### 🟡 阶段二：双序列型 / 字符串对比（核心主干）
**特点**：给你两个字符串 `text1` 和 `text2`。状态 `dp[i][j]` 表示 `text1` 的前 `i` 个字符和 `text2` 的前 `j` 个字符的某种关系。
*   **[1143] 最长公共子序列 (LCS) (Medium)**：双序列的鼻祖！公式 `dp[i][j] = dp[i-1][j-1] + 1`，彻底搞懂它。
*   **[72] 编辑距离 (Hard)**：面试最爱考的 Hard。插入、删除、替换三种操作如何对应到 `i` 和 `j` 的加减。
*   **[97] 交错字符串 (Medium)**：双指针 + DP 的完美结合。
*   **[115] 不同的子序列 (Hard)**：字符串匹配的高级玩法。

#### 🟠 阶段三：区间 DP（进阶挑战）
**特点**：状态 `dp[i][j]` 表示序列中从索引 `i` 到 `j` 这段**区间**的属性。它的难点在于**遍历顺序**——通常需要按“区间长度”从小到大遍历，或者 `i` 倒序、`j` 正序。
*   **[5] 最长回文子串 (Medium)**：可以作为区间 DP 的入门。
*   **[516] 最长回文子序列 (Medium)**：上一题的升级版，非连续。
*   **[312] 戳气球 (Hard)**：非常烧脑的逆向思维区间 DP，把最后被戳破的气球作为转移点。

#### 🔴 阶段四：带有特殊状态的三维 DP（终极 BOSS）
**特点**：在二维的基础上，还需要第三个维度记录“特权”或“剩余次数”。
*   **买卖股票系列 (122, 123, 188)**：状态定义为 `dp[天数][交易次数][是否持有股票]`。
*   **[576] 出界的路径数 (Medium)**：`dp[i][j][步数]`。

---

### 🛠️ 三、 破解多维 DP 的“四步走”心法

面对任何一道多维 DP，严格按照这四步来，绝不会乱：

#### 第一步：明确定义 `dp[i][j]` 的含义（最关键！）
把定义写在注释里，比如：“`dp[i][j]` 代表字符串 A 的前 `i` 个字符和字符串 B 的前 `j` 个字符的最小编辑距离”。
> 💡 **避坑**：搞清楚 `i` 是代表“索引”还是“长度”。通常双序列 DP 开数组时喜欢开 `m+1` 行 `n+1` 列，`dp[i][j]` 代表长度。

#### 第二步：寻找状态转移方程（分类讨论）
问自己：`dp[i][j]` 可以从哪里来？
通常双序列 DP 只有两种情况：
*   **结尾字符相同 (`A[i-1] == B[j-1]`)**：通常是顺风局，`dp[i][j] = dp[i-1][j-1] + ...`
*   **结尾字符不同 (`A[i-1] != B[j-1]`)**：通常需要做抉择，`max/min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])`。

#### 第三步：明确初始化（Base Case）
第一行 (`dp[0][j]`) 和 第一列 (`dp[i][0]`) 分别代表什么？
例如：字符串 A 为空，字符串 B 有 `j` 个字符，此时的值是多少？

#### 第四步：确定遍历顺序
*   **网格 / 双序列**：通常是从上到下，从左到右双重 `for` 循环。
*   **区间 DP**：画个表格！因为 `dp[i][j]` 通常依赖于左下角的值 `dp[i+1][j-1]`，所以**外层循环通常是 `i` 倒序，内层循环 `j` 正序**！

---

### 🐍 四、 Python 选手的专属避坑与起飞技巧

#### 💣 致命陷阱：二维数组的初始化
**绝对不要用：** `dp = [[0] * n] * m`
这会创建 `m` 个指向同一个列表的引用，修改一行会变更多行！
**正确的写法：** `dp = [[0] * n for _ in range(m)]`

#### 🚀 降维打击：`@cache` 神器
如果你在找状态转移方程时觉得“填表格”太抽象，不妨**先写递归（自顶向下）**！
在 Python 中，你只需要写出递归逻辑，然后在函数头上加一句 `@cache`（或者 `@lru_cache(None)`），它就自动变成动态规划了！

**举个例子（最长公共子序列）：**
```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache # 自动记忆化，这就是带备忘录的 DP！
        def dfs(i, j):
            # 边界条件（也就是 DP 的初始化）
            if i < 0 or j < 0:
                return 0
            
            # 状态转移
            if text1[i] == text2[j]:
                return dfs(i-1, j-1) + 1
            else:
                return max(dfs(i-1, j), dfs(i, j-1))
                
        return dfs(len(text1)-1, len(text2)-1)
```
**刷题建议**：初期做多维 DP 极度痛苦时，**先写带有 `@cache` 的递归版**，跑通了之后，再去翻译成 `for` 循环的填表版。这能极大地降低你的认知负担。


# 📖 每日算法笔记：多维 DP 与网格型状态压缩

## 🟢 核心套路总结：网格型 DP
这类题目的共同特征是：在一个二维网格中，每次只能**向右**或**向下**移动。
*   **状态依赖**：走到坐标 `(i, j)` 的状态，必然只依赖于其**正上方 `(i-1, j)`** 和 **正左方 `(i, j-1)`**。
*   **空间优化降维打击**：由于只依赖上一行和当前行，所有此类 $O(M \times N)$ 的二维 DP，都可以无脑压缩成 $O(N)$ 的一维滚动数组：
    *   等号右边的 `dp[j]` 相当于**正上方**（上一行的旧数据，还没被覆盖）。
    *   等号右边的 `dp[j-1]` 相当于**正左方**（当前行刚刚算出的新数据）。

---

## 一、 LeetCode 62. 不同路径 (Medium)

### 📌 题目核心
机器人从左上角走到右下角（无障碍物），求总共有多少条不同的路径。

### 💡 优化思路演进
1. **基础版 (二维数组)**：
   `dp[i][j] = dp[i-1][j] + dp[i][j-1]`
   初始化第一行和第一列全为 1。空间 $O(M \times N)$。
2. **终极优化 (一维滚动数组)**：
   将二维数组压缩为长度为 `n` 的一维数组。
   状态方程精简为：`dp[j] = dp[j] + dp[j-1]`
   初始化一个全为 1 的一维数组即可，因为第一行本来全为 1。

### 💻 核心代码（极致一维版）
```python
class Solution(object):
    def uniquePaths(self, m: int, n: int) -> int:
        # 初始化第一行，全为 1
        dp = [1] * n
        
        # 从第二行开始逐行往下刷
        for i in range(1, m):
            # 第一列始终为1，不需要更新，所以从 j=1 开始
            for j in range(1, n):
                # 新的 dp[j](当前) = 旧的 dp[j](上方) + dp[j-1](左方)
                dp[j] = dp[j] + dp[j - 1]
                
        return dp[-1]
```
### 📊 复杂度
- **时间复杂度**：$O(M \times N)$，遍历整个网格。
- **空间复杂度**：$O(N)$，仅使用一个长度为 $N$ 的一维数组。

*(注：本题也可用组合数学 $C_{m+n-2}^{m-1}$ 在 $O(M)$ 时间、$O(1)$ 空间内秒杀，作为面试装杯技巧。)*

---

## 二、 LeetCode 64. 最小路径和 (Medium)

### 📌 题目核心
网格中每个格子带有非负权重，求从左上走到右下，路径上数字总和的**最小值**。

### 💡 优化思路演进
1. **基础版 (二维数组)**：
   每一步只能从上方或左方走来，要想当前总和最小，就要挑上面和左边的较小者：
   `dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]`
2. **终极优化 (一维滚动数组)**：
   同样压缩为一维数组 `dp[j] = min(dp[j], dp[j-1]) + grid[i][j]`。
   **⚠️ 边界难点**：
   与 62 题第一列全是 1 不同，本题的第一列是累加的。因此在每开启新的一行（外层循环）时，必须**手动更新左边界 `dp[0]`**。

### 💻 核心代码（极致一维版）
```python
class Solution(object):
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [0] * n
        
        # 1. 初始化第一行的数据 (只能从左边走过来)
        dp[0] = grid[0][0]
        for j in range(1, n):
            dp[j] = dp[j - 1] + grid[0][j]
        
        # 2. 逐行向下滚动更新
        for i in range(1, m):
            # 处理本行最左边界 (只能从上面走下来)
            dp[0] += grid[i][0]
            
            # 处理本行其余元素
            for j in range(1, n):
                # 状态转移：min(上方，左方) + 当前格子权重
                dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]
        
        return dp[-1]
```
### 📊 复杂度
- **时间复杂度**：$O(M \times N)$，遍历整个地图。
- **空间复杂度**：$O(N)$，仅使用一个长度为 $N$ 的一维数组，兼顾了极低内存与不污染原数据的优良工程习惯。



# 📖 每日算法笔记：多维 DP 与空间极致压缩

## 🔴 一、 LeetCode 5. 最长回文子串 (Medium)

### 📌 题目核心
**区间 DP 经典题**。判断一段字符串是否是回文，取决于它的“两头是否相等”以及“剥去两头后的内部子串是否是回文”。

---

### 💡 核心思路演进
#### 1. 基础版：二维区间 DP
*   **状态定义**：`dp[i][j]` 表示从索引 `i` 到 `j` 的子串是否为回文。
*   **状态转移**：`dp[i][j] = (s[i] == s[j]) and dp[i+1][j-1]`。
*   **⚠️ 致命考点（遍历顺序）**：因为计算 `dp[i][j]` 依赖于它**左下角**的数据 `dp[i+1][j-1]`。为了保证读到的旧数据已经算好，外层循环 `i` **必须倒序遍历**（从下往上），内层 `j` **正序遍历**（从左往右，且 `j > i`）。

#### 2. 极限压缩版：一维滚动 DP
*   **优化逻辑**：上一行的状态算完后，其实只有“正左方”的数据还有用，可以直接把 2D 数组压成 1D 的 `dp[j]`。
*   **⚠️ 致命陷阱（状态残留与覆盖）**：
    1.  **内层 `j` 必须倒序**：为了拿到没被污染的左下角旧数据。
    2.  **必须擦除状态**：如果两头字符不相等 (`s[i] != s[j]`)，**必须显式地写 `dp[j] = False`**，否则它会继承上一轮循环留下的 `True`（脏数据），导致极其隐蔽的 Bug。

#### 3. 降维打击版：中心扩展法（大厂最优解）
*   **逻辑**：打破 DP 思维，利用回文的物理对称性。像石头落水一样，以每个字符（奇数中心）或两个字符的间隙（偶数中心）为起点，向外双指针扩展。这才是这道题空间 $O(1)$ 的真正满分解法。

---

### 💻 核心代码与复杂度对比

**【1】二维 DP 版** (时间 $O(N^2)$，空间 $O(N^2)$)
```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2: return s
        dp = [[False] * n for _ in range(n)]
        begin, max_len = 0, 1

        # i 必须倒序，保证左下角的 dp[i+1][j-1] 已就绪
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    if j - i <= 2: dp[i][j] = True
                    else: dp[i][j] = dp[i + 1][j - 1]
                
                if dp[i][j] and j - i + 1 > max_len:
                    max_len, begin = j - i + 1, i
        return s[begin : begin + max_len]
```

**【2】一维滚动版** (时间 $O(N^2)$，空间 $O(N)$)
```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2: return s
        dp = [False] * n
        begin, max_len = 0, 1

        for i in range(n - 1, -1, -1):
            # j 也必须倒序，防止读取到本轮已被覆盖的错乱数据
            for j in range(n - 1, i - 1, -1):
                if s[i] == s[j]:
                    if j - i <= 2: dp[j] = True
                    else: dp[j] = dp[j - 1]
                else:
                    # 极其重要：强制擦除上一轮的残留状态
                    dp[j] = False
                    
                if dp[j] and j - i + 1 > max_len:
                    max_len, begin = j - i + 1, i
        return s[begin : begin + max_len]
```

**【3】中心扩展法** (时间 $O(N^2)$，**空间 $O(1)$ 最优**)
```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # 退出时多走了一步，复原起点和长度
            return left + 1, right - left - 1

        begin, max_len = 0, 0
        for i in range(len(s)):
            l1, len1 = expand(i, i)       # 奇数中心
            l2, len2 = expand(i, i + 1)   # 偶数中心
            
            if len1 > max_len: begin, max_len = l1, len1
            if len2 > max_len: begin, max_len = l2, len2
                
        return s[begin : begin + max_len]
```

***

## 🟡 二、 LeetCode 1143. 最长公共子序列 (Medium)

### 📌 题目核心
**双序列 DP 鼻祖题**。两个指针分别遍历两个字符串，对比字符是否相等。重点技巧是开辟 `(m+1) * (n+1)` 大小的数组来做 **补零偏移 (Padding)**，完美处理空字符串边界。

---

### 💡 空间优化的“三级跳” (2D -> 两行 -> 1D)

#### 1. 基础版：二维 DP
*   **状态依赖**：如果相等，依赖**左上角** `dp[i-1][j-1] + 1`；如果不等，依赖**正上方与正左方** `max(dp[i-1][j], dp[i][j-1])`。

#### 2. 进阶版：双行滚动 (Two-Row)
*   **逻辑**：由于当前行 (`curr`) 只依赖上一行 (`prev`)，我们可以只开两行数组。
*   **极致优化**：内层循环强制绑定**较短**的字符串，极度节省内存。换行时绝不申请新内存，直接使用 **$O(1)$ 指针交换** (`prev, curr = curr, prev`)。

#### 3. 终极版：一维数组带 `temp` 传递
*   **逻辑**：只用一行数组。最大的痛点在于**左上角数据会被覆盖**（算 `j` 的时候，上一轮的 `dp[j-1]` 已经被改成新值了）。
*   **破局法**：在每行首记录 `left_up = dp[0]`。在覆盖 `dp[j]` 之前，先将其（即正上方数据）用 `next_left_up` 暂存下来；计算完成后，将其赋值给 `left_up` 传给下一轮当“左上角”。

---

### 💻 核心代码与复杂度对比

**【1】二维 DP 版** (时间 $O(M \times N)$，空间 $O(M \times N)$)
```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]
```

**【2】双行滚动版** (时间 $O(M \times N)$，空间 $O(\min(M,N))$)
```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2): text1, text2 = text2, text1
        m, n = len(text1), len(text2)
        
        prev, curr = [0] * (n + 1), [0] * (n + 1)
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    curr[j] = prev[j - 1] + 1
                else:
                    curr[j] = max(prev[j], curr[j - 1])
            # $O(1)$ 指针交换，环保且极速
            prev, curr = curr, prev
            
        # 注意：最后结果因为多交换了一次，停留在了 prev 中！
        return prev[-1]
```

**【3】一维滚动版 (带左上角暂存)** (时间 $O(M \times N)$，空间 $O(\min(M,N))$)
```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2): text1, text2 = text2, text1
        m, n = len(text1), len(text2)
        dp = [0] * (n + 1)
        
        for i in range(1, m + 1):
            # 每开启新一行，获取最本源的左上角 (通常为0)
            left_up = dp[0] 
            for j in range(1, n + 1):
                # 覆盖前，暂存当前位置的旧值（对下一格来说它就是左上角）
                next_left_up = dp[j] 
                
                if text1[i - 1] == text2[j - 1]:
                    dp[j] = left_up + 1
                else:
                    dp[j] = max(dp[j], dp[j - 1])
                    
                # 完美接力传递
                left_up = next_left_up 
                
        return dp[-1]
```