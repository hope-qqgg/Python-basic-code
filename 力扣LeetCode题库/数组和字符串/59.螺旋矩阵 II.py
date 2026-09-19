"""
给你一个正整数n，生成一个包含1到n²所有元素，且元素按顺时针顺序螺旋排列的n x n正方形矩阵matrix。

示例 1：
1 —— 2 —— 3
          |
8 —— 9    4
|         |
7 —— 6 —— 5
输入：n = 3 输出：[[1,2,3],[8,9,4],[7,6,5]]

示例 2：
输入：n = 1 输出：[[1]]

提示：
1 <= n <= 20
"""
# 模拟题
def generateMatrix(n):
    matrix = [[0] * n for _ in range(n)]
    count = 1
    start = 0
    while count < n ** 2:
        for j in range(start, n - 1 - start):
            matrix[start][j] = count
            count += 1
        for i in range(start, n - 1 - start):
            matrix[i][n - 1 - start] = count
            count += 1
        for j in range(n - 1 - start, start, -1):
            matrix[n - 1 - start][j] = count
            count += 1
        for i in range(n - 1 - start, start, -1):
            matrix[i][start] = count
            count += 1
        start += 1
    if n % 2 != 0:
        matrix[start][start] = count
    return matrix

