# 矩阵篇

## LeetCode 73. 矩阵置零
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

## 54 螺旋矩阵
### 题目核心
按顺时针螺旋顺序遍历二维矩阵，返回所有元素。

### 解题思路
采用**边界收缩法**模拟螺旋遍历过程：
1. 定义四个边界：上边界 `top`、下边界 `bottom`、左边界 `left`、右边界 `right`；
2. 按「从左到右 → 从上到下 → 从右到左 → 从下到上」的顺序遍历矩阵；
3. 每完成一轮遍历后收缩对应边界，遍历中检查边界是否越界，避免重复/错误遍历。

### 核心代码
```python
def spiralOrder(matrix):
    if not matrix or not matrix[0]:
        return []
    
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    result = []
    
    while top <= bottom and left <= right:
        # 左→右遍历上边界
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1
        
        # 上→下遍历右边界（边界检查）
        if top > bottom:
            break
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1
        
        # 右→左遍历下边界（边界检查）
        if left > right:
            break
        for col in range(right, left - 1, -1):
            result.append(matrix[bottom][col])
        bottom -= 1
        
        # 下→上遍历左边界（边界检查）
        if top > bottom:
            break
        for row in range(bottom, top - 1, -1):
            result.append(matrix[row][left])
        left += 1
    
    return result
```

### 复杂度分析
- **时间复杂度**：$O(m×n)$，每个元素仅遍历一次（m 为行数，n 为列数）；
- **空间复杂度**：$O(1)$，除结果存储外无额外空间开销（结果存储为题目要求，不计入算法空间复杂度）。

---

## 48 旋转图像
### 题目核心
不使用额外空间（in-place），将 n×n 二维矩阵顺时针旋转 90 度。

### 解题思路
最优解法为「**先转置矩阵，再反转每行**」：
1. 矩阵转置：行和列互换（仅遍历上三角区域，避免重复交换）；
2. 反转每行：将转置后的矩阵每行元素左右反转，最终得到顺时针旋转 90 度的结果。

### 数学证明（坐标变换等价性）
#### 1. 符号约定
- 原始 n×n 矩阵为 $M$，元素原始坐标为 $(i, j)$（$0 ≤ i,j < n$）；
- 顺时针旋转 90 度后的矩阵为 $M'$，元素 $M[i][j]$ 旋转后坐标为 $(i', j')$，即 $M'[i'][j'] = M[i][j]$。

#### 2. 顺时针旋转 90 度的坐标变换公式
$$
\begin{cases}
i' = j \\
j' = n - 1 - i
\end{cases}
$$

#### 3. 「转置 + 反转行」的坐标变换拆解
- **转置**：原始坐标 $(i,j)$ → 转置后坐标 $(i_1, j_1) = (j, i)$；
- **反转行**：转置后坐标 $(i_1, j_1)$ → 反转后坐标 $(i_2, j_2)$，其中 $i_2 = i_1$，$j_2 = n - 1 - j_1$；
- **组合变换**：$(i_2, j_2) = (j, n - 1 - i)$。

#### 4. 等价性验证
「转置 + 反转行」的最终坐标 $(i_2, j_2)$ 与顺时针旋转 90 度的坐标 $(i', j')$ 完全一致，因此该操作组合等价于矩阵顺时针旋转 90 度。

### 核心代码
```python
class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)
        
        # 步骤1：转置矩阵（上三角遍历，避免重复交换）
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # 步骤2：反转每一行（in-place 操作）
        for i in range(n):
            matrix[i].reverse()
```

### 复杂度分析
- **时间复杂度**：$O(n^2)$，每个元素被访问两次（转置一次、反转一次）；
- **空间复杂度**：$O(1)$，仅使用常量级额外空间，满足 in-place 要求。

---

## 240 搜索二维矩阵 II
### 题目核心
在「每行升序、每列升序」的二维矩阵中，高效判断目标值是否存在。

### 解题思路
利用矩阵有序性，从**右上角**（或左下角）开始遍历，一次比较排除一整行/一整列：
1. 起始位置：右上角（行=0，列=cols-1）；
2. 比较逻辑：
   - 当前元素 == 目标值：返回 True；
   - 当前元素 > 目标值：目标值在左侧，列索引 -1；
   - 当前元素 < 目标值：目标值在下方，行索引 +1；
3. 遍历终止：行/列越界则返回 False。

### 核心代码
```python
class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        
        rows = len(matrix)
        cols = len(matrix[0])
        row, col = 0, cols - 1  # 起始位置：右上角
        
        while row < rows and col >= 0:
            current = matrix[row][col]
            if current == target:
                return True
            elif current > target:
                col -= 1  # 排除当前列，列左移
            else:
                row += 1  # 排除当前行，行下移
        
        return False
```

### 复杂度分析
- **时间复杂度**：$O(m + n)$，最坏情况下遍历到左下角/右上角，最多走 m+n 步（m 为行数，n 为列数）；
- **空间复杂度**：$O(1)$，仅使用常量级额外空间。

---

## 总结
| 题目         | 核心方法               | 时间复杂度 | 空间复杂度 |
|--------------|------------------------|------------|------------|
| 螺旋矩阵     | 边界收缩法             | $O(m×n)$   | $O(1)$     |
| 旋转图像     | 转置 + 反转行          | $O(n^2)$   | $O(1)$     |
| 搜索二维矩阵 | 右上角/左下角定向遍历  | $O(m + n)$ | $O(1)$     |