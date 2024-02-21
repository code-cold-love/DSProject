#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 1000. 合并石头的最低成本 https://leetcode.cn/problems/minimum-cost-to-merge-stones/
from math import inf
from typing import List


class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        n = len(stones)
        # 每一次合并将 k 堆石头变为 1 堆，堆数减少 k-1，如果合并若干次要使得 n 堆变为 1 堆，就需要 n−1 是 k−1 的倍数
        if (n - 1) % (k - 1) != 0:
            return -1
        # d[l][r] 表示将区间 [l, r] 合并到不能为止时的最小成本
        # 初态：d[i][i] = 0，其他状态设为正无穷
        d = [[inf] * n for _ in range(n)]
        s, prefix_sum = 0, [0] * n
        for i in range(n):
            d[i][i] = 0
            s += stones[i]
            prefix_sum[i] = s
        for L in range(2, n + 1):  # L 枚举区间长度
            for l in range(n - L + 1):  # l 区间起点
                r = l + L - 1  # r 区间终点
                for p in range(l, r, k - 1):  # 枚举最后一次合并的位置
                    d[l][r] = min(d[l][r], d[l][p] + d[p + 1][r])
                if (r - l) % (k - 1) == 0:  # 如果区间长度满足合并条件
                    d[l][r] += (prefix_sum[r] - (0 if l == 0 else prefix_sum[l - 1]))
        return d[0][n - 1]


if __name__ == '__main__':
    obj = Solution()
    print(obj.mergeStones(stones=[3, 2, 4, 1], k=2))  # 20
    print(obj.mergeStones(stones=[3, 2, 4, 1], k=3))  # -1
    print(obj.mergeStones(stones=[3, 5, 1, 2, 6], k=3))  # 25
