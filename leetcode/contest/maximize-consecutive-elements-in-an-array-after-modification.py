#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 100205. 修改数组后最大化数组中的连续元素数目 https://leetcode.cn/contest/biweekly-contest-124/problems/maximize-consecutive-elements-in-an-array-after-modification/
from typing import List
from collections import defaultdict


class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        seen = defaultdict(int)
        nums.sort()
        for v in nums:
            seen[v + 1] = max(seen[v + 1], seen[v] + 1)
            seen[v] = max(seen[v], seen[v - 1] + 1)  # 为什么这一步是这样的？
        return max(seen.values())


if __name__ == '__main__':
    obj = Solution()
    print(obj.maxSelectedElements([1, 4, 7, 10]))  # 1
    print(obj.maxSelectedElements([2, 1, 5, 1, 1]))  # 3
