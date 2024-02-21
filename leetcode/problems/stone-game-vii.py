#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 1690. 石子游戏 VII https://leetcode.cn/problems/stone-game-vii/
from typing import List

from executing import cache


class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n, pre = 0, [0]
        for s in stones:
            n += 1
            pre.append(pre[-1] + s)  # 前缀和

        @cache
        def dfs(i, j):
            if i >= j:  # 递归边界
                return 0
            # 子问题：最大化【先手】的得分减去【后手】的得分
            return max(pre[j + 1] - pre[i + 1] - dfs(i + 1, j), pre[j] - pre[i] - dfs(i, j - 1))

        ans = dfs(0, n - 1)
        dfs.cache_clear()  # 防止爆内存
        return ans

    def stoneGameVII_dp(self, stones: List[int]) -> int:
        n = len(stones)
        pre = [0] * (n + 1)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            pre[i + 1] = pre[i] + stones[i]
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                dp[i][j] = max(pre[j + 1] - pre[i + 1] - dp[i + 1][j], pre[j] - pre[i] - dp[i][j - 1])
            return dp[0][n - 1]


if __name__ == '__main__':
    obj = Solution()
    print(obj.stoneGameVII([5, 3, 1, 4, 2]))  # 6
    print(obj.stoneGameVII([7, 90, 5, 1, 100, 10, 10, 2]))  # 122
