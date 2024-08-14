#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 3152. 特殊数组 II https://leetcode.cn/problems/special-array-ii/
from itertools import pairwise, accumulate
from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        # 0 <= queries[i][0] <= queries[i][1] <= nums.length - 1
        # 前缀和法
        s = list(accumulate((x % 2 == y % 2 for x, y in pairwise(nums)), initial=0))
        return [s[_from] == s[_to] for _from, _to in queries]


if __name__ == '__main__':
    solution = Solution()
    print(solution.isArraySpecial([3, 4, 1, 2, 6], [[0, 4]]))  # [False]
