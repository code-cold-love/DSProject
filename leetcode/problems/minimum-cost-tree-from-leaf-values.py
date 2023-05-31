# -*- coding: utf-8 -*-
# 1130. 叶值的最小代价生成树 https://leetcode.cn/problems/minimum-cost-tree-from-leaf-values/
from math import inf
from typing import List


class Solution:
    def mctFromLeafValues_dp(self, arr: List[int]) -> int:
        """动态规划，自上而下构建二叉树"""
        n = len(arr)
        dp = [[inf for i in range(n)] for j in range(n)]
        ma = [[0 for i in range(n)] for j in range(n)]
        for j in range(n):
            ma[j][j] = arr[j]
            dp[j][j] = 0
            for i in range(j - 1, -1, -1):
                ma[i][j] = max(arr[i], ma[i + 1][j])
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + ma[i][k] * ma[k + 1][j])
        return dp[0][n - 1]

    def mctFromLeafValues_stack(self, arr: List[int]) -> int:
        """单调栈，自下而上构建二叉树"""
        res, stk = 0, list()
        for x in arr:
            while stk and stk[-1] <= x:
                y = stk.pop()  # y <= x
                if not stk or stk[-1] > x:
                    res += y * x
                else:
                    res += stk[-1] * y
            stk.append(x)
        while len(stk) >= 2:
            i = stk.pop()
            res += stk[-1] * i
        return res


if __name__ == '__main__':
    obj = Solution()
    print(obj.mctFromLeafValues_dp([6, 2, 4]))  # 32
    print(obj.mctFromLeafValues_stack([6, 2, 4]))  # 32
