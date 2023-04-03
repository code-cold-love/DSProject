# -*- coding: utf-8 -*-
# 1039. 多边形三角剖分的最低得分 https://leetcode.cn/problems/minimum-score-triangulation-of-polygon/
from typing import List


class Solution:
    def minScoreTriangulation_dp(self, values: List[int]) -> int:
        # values[i] 表示凸的多边形的第 i 个顶点的值（顺时针顺序）
        # 返回多边形进行三角剖分后可以得到的最低分
        def dp(i, j):  # 设 dp[i][j] (j >= i+2) 的值为顶点 i, i+1, ..., j-1, j 构成的凸 j−i+1 边形进行三角形剖分后可以得到的最低分
            if j < i + 2:
                return 0
            elif j == i + 2:
                return values[i] * values[i + 1] * values[j]
            else:
                return min((values[i] * values[k] * values[j] + dp(i, k) + dp(k, j)) for k in range(i + 1, j))

        return dp(0, len(values) - 1)

    def minScoreTriangulation(self, values: List[int]) -> int:
        # 递推
        n = len(values)
        f = [[0] * n for _ in range(n)]
        for i in range(n - 3, -1, -1):
            for j in range(i + 2, n):
                f[i][j] = min(f[i][k] + f[k][j] + values[i] * values[j] * values[k] for k in range(i + 1, j))
        return f[0][-1]


if __name__ == '__main__':
    obj = Solution()
    print(obj.minScoreTriangulation([1, 2, 3]))  # 6
    print(obj.minScoreTriangulation([3, 7, 4, 5]))  # 144
    print(obj.minScoreTriangulation([1, 3, 1, 4, 1, 5]))  # 13
    print(obj.minScoreTriangulation_dp([1, 2, 3]))  # 6
    print(obj.minScoreTriangulation_dp([3, 7, 4, 5]))  # 144
    print(obj.minScoreTriangulation_dp([1, 3, 1, 4, 1, 5]))  # 13
