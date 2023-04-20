# -*- coding: utf-8 -*-
# 1187. 使数组严格递增 https://leetcode.cn/problems/make-array-strictly-increasing/
from math import inf
from typing import List
from bisect import bisect_right


class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2 = sorted(set(arr2))
        n = len(arr1)
        m = len(arr2)
        dp = [[inf] * (min(m, n) + 1) for _ in range(n + 1)]
        dp[0][0] = -1
        for i in range(1, n + 1):
            for j in range(min(i, m) + 1):
                if arr1[i - 1] > dp[i - 1][j]:
                    dp[i][j] = arr1[i - 1]
                if j and dp[i - 1][j - 1] != inf:
                    k = bisect_right(arr2, dp[i - 1][j - 1], j - 1)
                    if k < m:
                        dp[i][j] = min(dp[i][j], arr2[k])
                if i == n and dp[i][j] != inf:
                    return j
        return -1


if __name__ == '__main__':
    obj = Solution()
    print(obj.makeArrayIncreasing(arr1=[1, 5, 3, 6, 7], arr2=[1, 3, 2, 4]))  # 1
    print(obj.makeArrayIncreasing(arr1=[1, 5, 3, 6, 7], arr2=[4, 3, 1]))  # 2
    print(obj.makeArrayIncreasing(arr1=[1, 5, 3, 6, 7], arr2=[1, 6, 3, 3]))  # -1
