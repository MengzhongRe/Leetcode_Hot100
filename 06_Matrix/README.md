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