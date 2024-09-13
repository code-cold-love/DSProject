#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2064. 分配给商店的最多商品的最小值 https://leetcode.cn/problems/minimized-maximum-of-products-distributed-to-any-store/
from typing import List


class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        # 1 <= m=len(quantities) <= n <= 10**5

        def check(k: int) -> bool:
            """给定数字 k，是否存在可行的分配方案"""
            cnt = 0
            for q in quantities:
                cnt += (q - 1) // k + 1  # 分配完所有商品最少需要的商店数量
            return cnt <= n

        left, right = 1, max(quantities) + 1
        while left < right:
            mid = left + (right - left) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == '__main__':
    solution = Solution()
    print(solution.minimizedMaximum(6, [11, 6]))  # 3
    print(solution.minimizedMaximum(7, [15, 10, 10]))  # 5
