#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2741. 特别的排列 https://leetcode.cn/problems/special-permutations/
from functools import cache
from typing import List


class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        # nums 包含 n 个互不相同的正整数
        mod = 10 ** 9 + 7
        n = len(nums)

        @cache
        def dfs(state, i):  # 当前排列包含集合 state 表示的所有整数
            # state 是状态压缩后的集合，其二进制表示中第 k 位为 1 则表示包含整数 nums[k]
            if state == (1 << i):  # 表示只含一个元素
                return 1
            ans = 0
            x = nums[i]
            for j, y in enumerate(nums):
                if i == j or not state >> j & 1:
                    continue
                if x % y != 0 and y % x != 0:
                    continue
                ans = (ans + dfs(state ^ (1 << i), j)) % mod  # state ^ (1 << i) 去除 state 中的 nums[i]
            return ans

        return sum(dfs((1 << n) - 1, i) for i in range(n)) % mod


if __name__ == '__main__':
    solution = Solution()
    print(solution.specialPerm([2, 3, 6]))  # 2
    print(solution.specialPerm([1, 4, 3]))  # 2
