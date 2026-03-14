# 🌟 算法面试高频核心考点笔记
> **核心标签**：回溯算法 (Backtracking)、决策树、深浅拷贝、全排列与子集
> **学习日期**：2026-03

---

## 🏷️ 1. LeetCode 46: 全排列 (Medium)
> **面试本质考点**：回溯思想的“Hello World”、状态的撤销（吃进去再吐出来）、Python 深浅拷贝机制

### 💡 详细解题思路
排列问题讲究顺序（`[1, 2]` 和 `[2, 1]` 是两个不同的排列），因此每次做选择时，我们都必须**从头到尾**考察整个数组，看看哪个数字还没被用过。

* **回溯三步曲（万能模板）**：
  1. **终止条件**：当收集的路径 `path` 长度等于原数组长度时，说明凑齐了一个全排列，加入结果集并返回。
  2. **做选择（横向遍历与纵向深入）**：用 `for` 循环遍历所有数字，如果数字已经在 `path` 里了就跳过（去重）；否则把它加入 `path`，然后向下递归。
  3. **撤销选择（灵魂所在）**：从下一层递归退回来后，必须把刚刚加进去的数字 `pop()` 出来，把位置腾出来，才能在 `for` 循环的下一步去尝试其他的数字分支。
* **避坑指南（浅拷贝）**：加入结果集时绝对不能写 `res.append(path)`，必须写 **`res.append(path[:])`**！因为 `path` 贯穿全局，如果不照相（浅拷贝）留存那一瞬间的状态，最后 `path` 被清空时，结果集里全是空列表。

### 💻 核心代码 (Python)
```python
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res =[]
        
        def backtrack(path):
            # 1. 终止条件：拼满了一个排列
            if len(path) == len(nums):
                res.append(path[:])  # 🚨 巨坑：必须使用浅拷贝保存当前状态！
                return
            
            # 2. 遍历所有选择
            for num in nums:
                if num in path:      # 已经被当前路径用过的数字，跳过
                    continue
                
                path.append(num)     # 3. 做选择
                backtrack(path)      # 4. 递归进入下一层决策树
                path.pop()           # 5. 撤销选择（回溯的核心：退回上一步尝试其他可能）
                
        backtrack([])
        return res
```

### ⏱️ 详细复杂度分析
* **时间复杂度**：$\mathcal{O}(N \times N!)$。$N$ 个数字的全排列有 $N!$ 种，每次得到一个完整排列时，执行 `path[:]` 浅拷贝需要 $\mathcal{O}(N)$ 的时间。
* **空间复杂度**：$\mathcal{O}(N)$（辅助空间）。主要开销为递归调用栈的深度（最深为 $N$）以及维护当前状态的 `path` 数组（长度为 $N$）。若算上最终返回的 `res` 结果集，总空间复杂度为 $\mathcal{O}(N \times N!)$。

---

## 🏷️ 2. LeetCode 78: 子集 (Medium)
> **面试本质考点**：组合类问题的天然去重机制、`startIndex` 开关的精妙运用

### 💡 详细解题思路
子集问题（以及组合问题）**不讲究顺序**（`[1, 2]` 和 `[2, 1]` 算同一个子集）。如果我们套用全排列的代码，会产生大量的重复集合。
* **核心破局点：`startIndex`（不回头法则）**
  * 我们给递归函数加一个参数 `startIndex`，规定：**当前层只能从原数组的 `startIndex` 位置开始往后挑数字，绝对不能回头看！**
  * 比如当前挑了 `2`（索引为 1），那么传给下一层的起始位置就是 `1 + 1 = 2`（也就是只能去挑 `3`）。
  * 这种“强制按物理顺序向右取”的机制，完美消灭了“先取右边再取左边”导致的倒序重复问题。
* **收集时机**：与全排列必须要走到“叶子节点”才收集不同，子集问题中，**决策树上的每一个节点（包括空集）都是一个合法的子集**。因此，一进入递归函数，立刻无条件收集当前路径。

### 💻 核心代码 (Python)
```python
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res =[]
        
        # startIndex 控制当前这一步只能从哪里开始挑
        def backtrack(startIndex, path):
            # 1. 收集结果：决策树的每一个节点都是合法子集，直接收集（依然需要浅拷贝）
            res.append(path[:])
            
            # 2. 从 startIndex 开始往后遍历（绝不回头！）
            for i in range(startIndex, len(nums)):
                path.append(nums[i])       # 做选择
                
                # 3. 递归：告诉下一层，你只能从我挑的这个数字的【下一个位置 (i+1)】开始挑
                backtrack(i + 1, path)     
                
                path.pop()                 # 撤销选择
                
        backtrack(0,[])
        return res
```

### ⏱️ 详细复杂度分析
* **时间复杂度**：$\mathcal{O}(N \times 2^N)$。长度为 $N$ 的数组共有 $2^N$ 个子集。每个子集加入结果集时都需要进行 `path[:]` 的浅拷贝操作，子集的平均长度为 $N/2$，故时间代价精确为 $\mathcal{O}(N \times 2^N)$。
* **空间复杂度**：$\mathcal{O}(N)$（辅助空间）。递归调用栈的最深层数为 $N$（一条路走到黑把所有数字全选上），同时用来暂存状态的 `path` 数组最大长度也是 $N$。若把存放了 $2^N$ 个子集的结果集 `res` 也算进去，总空间复杂度为 $\mathcal{O}(N \times 2^N)$。

---

### 🌟 【黄金总结】回溯算法选型对照表

在考场上，根据题目要求，一秒决定循环的写法：

| 题型 | 顺序要求 | `for` 循环怎么写 | 为什么这么写？ |
| :--- | :--- | :--- | :--- |
| **排列 (Permutation)** | `[1,2] != [2,1]` | `for num in nums:` (每次从 0 开始) | 只要前面没选过的，我都可以选！(需要配合 `if num in path` 去重) |
| **子集 / 组合 (Subset/Combo)** | `[1,2] == [2,1]` | `for i in range(startIndex, len(nums)):` | 只能一直往前走，禁止回头！(天然去重，不需要判断 `num in path`) |


# 🌟 算法面试高频核心考点笔记
> **核心标签**：回溯算法 (Backtracking)、多集合组合、深度优先遍历、极致剪枝
> **学习日期**：2026-03

---

## 🏷️ 1. LeetCode 39: 组合总和 (Medium)
> **面试本质考点**：同一集合的**无限制重复选取**组合、回溯的极速剪枝优化（排序 + 提前终止）

### 💡 解题思路
本题与 78题（子集）极为相似，唯一的区别是：**同一个数字可以无限制被选取**。
* **回溯设计的改变**：
  * 在子集问题中，为了不重复选自己，下一层递归传入的是 `i + 1`。
  * 在本题中，因为可以无限薅羊毛，我们做完选择后，依然留在当前数字，所以下一层递归传入的依然是 **`i`**（绝不回头，但可以原地驻留）。
* **面试惊艳操作：排序 + 极致剪枝**：
  * 先把给定的 `candidates` 数组从小到大排序。
  * 在遍历尝试放数字时，如果我们发现 `目标值 - 当前数字 < 0`（说明装爆了），因为数组是有序的，**后面的数字必然更大，直接 `break` 掉整个 `for` 循环**，砍掉无数的无效搜索树枝！

### 💻 核心代码 (Python)
```python
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res =[]
        # 1. 提前排序，这是能够进行极致剪枝的大前提！
        candidates.sort()
        
        # current_target 记录距离目标还差多少
        def backtrack(startIndex, current_target, path):
            # 2. 终止条件：刚刚好凑齐
            if current_target == 0:
                res.append(path[:])
                return
            
            # 3. 遍历选择（只能往右看，绝不回头）
            for i in range(startIndex, len(candidates)):
                # 🚨 核心优化（剪枝）：如果当前数字都嫌大，后面的更不用看了，直接结束本层循环！
                if current_target - candidates[i] < 0:
                    break
                
                # 做选择
                path.append(candidates[i])
                
                # 4. 递归深入：【精髓】传入 i 而不是 i+1，代表下一层还可以继续选当前数字！
                backtrack(i, current_target - candidates[i], path)
                
                # 撤销选择
                path.pop()
                
        backtrack(0, target,[])
        return res
```

### ⏱️ 详细复杂度分析
* **时间复杂度**：$\mathcal{O}(S)$。$S$ 为所有可行解的长度之和。最坏情况下的节点数为 $\mathcal{O}(N^{\frac{T}{M}})$（$N$ 为数组长度，$T$ 为目标值，$M$ 为最小元素），但由于我们加入了排序和 `break` 剪枝，实际运行时间被大幅度缩减。
* **空间复杂度**：$\mathcal{O}(\frac{T}{M})$。主要为递归调用栈的深度和 `path` 数组的长度。最深的情况是一直选最小的数字，最多选 $\frac{T}{M}$ 次。

---

## 🏷️ 2. LeetCode 17: 电话号码的字母组合 (Medium)
> **面试本质考点**：**多集合**之间的排列组合、哈希表映射与回溯的结合

### 💡 解题思路
这道题不再是从“一个数组”里挑数字，而是从“多个相互独立的数组”里分别挑出一个字母进行组合。
比如输入 `"23"`，就是先在 `"abc"` 里挑一个，再去 `"def"` 里挑一个。
* **构建映射字典**：首先需要一个哈希表或数组，把数字 `'2'` 到 `'9'` 映射到对应的字符串。
* **递归参数的设计 (`index`)**：
  * 我们不需要 `startIndex` 来防止元素重复使用，因为每一个数字对应的字母集合都是全新的。
  * 我们需要一个参数 `index`，用来记录**“当前递归到了输入字符串 `digits` 的第几个数字”**。
* **横向与纵向**：
  * **纵向（递归深度）**：取决于 `digits` 的长度（输入几个数字，就要往下走几层）。
  * **横向（`for` 循环）**：遍历的是**当前数字所对应的所有字母**。

### 💻 核心代码 (Python)
```python
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        # 特殊情况处理
        if not digits:
            return[]
            
        # 1. 建立数字到字母的映射大字典
        phone_map = {
            '2': "abc", '3': "def", '4': "ghi", '5': "jkl",
            '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"
        }
        res =[]
        
        # index 代表当前正在处理 digits 字符串中的第几个数字
        def backtrack(index, path):
            # 2. 终止条件：当 index 等于 digits 长度时，说明每个数字都挑过字母了
            if index == len(digits):
                # 收集结果：把 path 列表里的字符拼成一个字符串
                res.append("".join(path))
                return
            
            # 3. 找出当前数字对应的全部字母
            current_digit = digits[index]
            letters = phone_map[current_digit]
            
            # 4. 遍历当前集合（比如 'a', 'b', 'c'）
            for char in letters:
                path.append(char)          # 做选择
                backtrack(index + 1, path) # 递归深入：去处理输入字符串的下一个数字！
                path.pop()                 # 撤销选择
                
        # 从第 0 个数字开始回溯
        backtrack(0,path)
        return res
```

---

### 🌟 【终极总结】回溯四大金刚（万能选型对照表）

我们在做回溯题时，最核心的纠结往往只有两个：
1. **横向怎么遍历？**（`for` 循环是从 `0` 开始，还是从 `startIndex` 开始？）
2. **纵向怎么深入？**（递归往下传的是 `i`，`i + 1`，还是别的 `index`？）

看完下面这张表，一切豁然开朗：

| 题型本质 | 代表题目 | 选材范围（在哪挑） | 元素选取规则 | `for` 循环写法<br>*(横向遍历)* | 递归传参写法<br>*(纵向深入)* |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **排列**<br>*(讲究顺序)* | **46. 全排列** | **同一个数组** | 元素只能用 1 次。<br>`[1,2] != [2,1]` | `for num in nums:`<br>👉 **每次都从 0 开始扫描全场** | `backtrack(...)`<br>*(依赖 `if num in path` 排除已选)* |
| **单集合组合**<br>*(不讲顺序)* | **78. 子集**<br>77. 组合 | **同一个数组** | 元素只能用 1 次。<br>`[1,2] == [2,1]` | `for i in range(`**`startIndex`**`, len):`<br>👉 **只能往右看，绝不回头** | `backtrack(`**`i + 1`**`, ...)`<br>*(拿完了，强制去下一个货架)* |
| **单集合无限组合**<br>*(不讲顺序)* | **39. 组合总和** | **同一个数组** | 元素可**无限重复**用。<br>`[1,2] == [2,1]` | `for i in range(`**`startIndex`**`, len):`<br>👉 **只能往右看，绝不回头** | `backtrack(`**`i`**`, ...)`<br>*(薅羊毛，继续留在当前货架)* |
| **多集合组合**<br>*(独立组合)* | **17. 电话号码** | **多个独立数组/集合** | **每个集合各挑 1 个**，<br>集合之间互不干扰 | `for char in letters:`<br>👉 **完整遍历当前锁定的这一个小集合** | `backtrack(`**`index + 1`**`, ...)`<br>*(挑完了，去处理下一个独立集合)* |

---

### 💡 核心法则提取（心法口诀）

为了让你形成肌肉记忆，总结三句心法：

1. **只要是在“同一个数组”里求组合/子集，统统加 `startIndex`！**
   * 防回头，防重复。传 `i+1` 是一次性买卖，传 `i` 是无限量自助餐。
2. **只要是求“排列”（讲究顺序），绝对不能加 `startIndex`！**
   * 必须每次从头 `0` 开始找，因为可以先拿后面的再拿前面的，靠 `used` 数组或 `in` 机制去重。
3. **只要是“多个不同的数组”互相拼凑，扔掉 `startIndex`，换成 `index`！**
   * `index` 控制的是“我现在正在哪一个数组里挑选”，`for` 循环直接老老实实把当前的这个数组遍历完就行。

---

# 🌟 算法面试高频核心考点笔记
> **核心标签**：高级回溯算法、动态剪枝、二维矩阵 DFS、卡特兰数
> **学习日期**：2026-03

---

## 🏷️ 1. LeetCode 22: 括号生成 (Medium)
> **面试本质考点**：在生成过程中进行**动态合法性约束（极致剪枝）**、理解递归与字符串不可变性

### 💡 详细解题思路
这道题的本质是每次在 `(` 和 `)` 中做二选一的决策，形成一棵深度为 $2n$ 的二叉树。为了避免生成出不合法的括号再废弃，我们利用**“借款与还款”**的原则，在分支生长时直接掐断非法路径：
* **核心规则（动态剪枝铁律）**：
  1. **左括号（借款）**：只要当前左括号数量 `< n`，随时可以加 `(`。
  2. **右括号（还款）**：只有当当前右括号数量 `< 左括号数量` 时，才能加 `)`。（绝不能没借款就先还款，这会导致 `)(` 非法嵌套）。
* **进阶技巧（隐式回溯）**：在 Python 中，由于字符串是不可变对象，如果在递归传参时直接拼接字符串（如 `current_str + '('`），系统会在内存中生成新字符串传给下一层，**当前层的字符串毫发无损，从而天然省去了 `path.pop()` 撤销选择的步骤**！

### 💻 核心代码 (Python)
```python
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res =[]
        
        # left_count: 当前用掉的左括号数量
        # right_count: 当前用掉的右括号数量
        def backtrack(left_count, right_count, path):
            # 1. 终止条件：当路径长度达到 2n 时，说明拼满了
            if len(path) == 2 * n:
                res.append("".join(path))
                return
            
            # 2. 做选择 1：加左括号（只要还有贷款额度）
            if left_count < n:
                path.append('(')
                backtrack(left_count + 1, right_count, path)
                path.pop()  # 撤销选择
                
            # 3. 做选择 2：加右括号（必须保证已借的大于已还的）
            if right_count < left_count:
                path.append(')')
                backtrack(left_count, right_count + 1, path)
                path.pop()  # 撤销选择
                
        backtrack(0, 0,[])
        return res
```

### ⏱️ 详细复杂度分析 (面试王炸级回答)
* **时间复杂度**：$\mathcal{O}\left(\frac{4^n}{\sqrt{n}}\right)$。本题生成的合法括号序列总数严格等于第 $n$ 个**卡特兰数 (Catalan Number)**。由于我们做了极速剪枝，没有任何无效分支的生成，因此时间复杂度的渐进界限就是卡特兰数的渐进界限 $\mathcal{O}(\frac{4^n}{n\sqrt{n}})$ 乘以单次路径拼接的时间 $\mathcal{O}(n)$。
* **空间复杂度**：$\mathcal{O}(n)$（辅助空间）。主要开销为递归调用栈的深度，最大深度也就是拼出完整字符串的长度 $2n$，忽略常数项后为 $\mathcal{O}(n)$。

---

## 🏷️ 2. LeetCode 79: 单词搜索 (Medium)
> **面试本质考点**：二维网格 DFS 遍历、**空间极度压缩的原地标记法**、有效分支系数的时间复杂度计算

### 💡 详细解题思路
这是将“一维数组的回溯”降维打击到“二维迷宫”的祖师爷级题目。
* **双重循环找起点**：先用两层 `for` 循环遍历整个二维网格，遇到和单词首字母匹配的格子，就以它为起点开启 DFS。
* **DFS 与回溯逻辑（涂鸦与擦除）**：
  * **出口判断**：如果匹配到了单词末尾（成功）；如果越界或者字母不匹配（失败）。
  * **做选择（防走回头路）**：题目规定同一个格子不能重复走。我们走到正确格子时，先把它的值暂存，然后**原地将其修改为 `'#'`**（涂鸦标记）。这巧妙地省去了开辟 $\mathcal{O}(M \times N)$ 大小的 `visited` 访问数组。
  * **四向探险**：朝上下左右四个方向递归调用 `dfs` 寻找单词的下一个字母。
  * **撤销选择（灵魂）**：从四个方向退回当前格子后，**必须将格子从 `'#'` 恢复回原字母**。因为从另一条完全不同的探索路径过来时，可能还需要用到这个格子。

### 💻 核心代码 (Python)
```python
class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        
        # r, c 为当前坐标；index 为当前正在找 word 的第几个字母
        def dfs(r, c, index):
            # 1. 成功终止：单词所有字母都找齐了
            if index == len(word):
                return True
            
            # 2. 失败剪枝：越界，或当前格子字母不对，或遇到了 '#' (回头路)
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[index]:
                return False
            
            # 3. 做选择：暂存原字母，并原地涂黑标记（防重复访问）
            temp = board[r][c]
            board[r][c] = '#'
            
            # 4. 递归深入：朝四个方向寻找下一个字母，有一个走通即可
            found = (dfs(r - 1, c, index + 1) or
                     dfs(r + 1, c, index + 1) or
                     dfs(r, c - 1, index + 1) or
                     dfs(r, c + 1, index + 1))
                     
            # 5. 撤销选择：四个方向找完退回来时，把格子恢复原样
            board[r][c] = temp
            
            return found

        # 遍历全图，寻找所有可能的梦开始的地方（首字母匹配的格子）
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
        return False
```

### ⏱️ 详细复杂度分析 (面试高阶细节)
* **时间复杂度**：$\mathcal{O}(M \times N \times 3^L)$。
  * $M, N$ 为矩阵长宽，$L$ 为单词长度。我们需要遍历 $M \times N$ 个起点。
  * **为什么是 $3^L$ 而不是 $4^L$？（高情商必答重点）**：在 DFS 递归树中，虽然代码上每个节点向 4 个方向发起了调用，但由于我们用 `'#'` 标记了走过的路，**必定有 1 个方向是“回头路”**。这个回头路的调用会在 $\mathcal{O}(1)$ 的瞬间触发判断并死亡，不会引起后续裂变。因此，从第二步开始，递归树真正的**有效分支系数 (Effective Branching Factor)** 只有 3。搜索树的规模严格呈 $3^L$ 增长。
* **空间复杂度**：$\mathcal{O}(L)$。
  * 因为采用了原地修改 `board` 为 `'#'` 的神仙操作，我们省下了巨大的辅助访问数组。
  * 空间开销仅剩 DFS 递归调用栈的深度，最深潜入深度即为单词的长度 $L$，故空间复杂度为 $\mathcal{O}(L)$。