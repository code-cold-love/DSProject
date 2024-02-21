#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 1207. 独一无二的出现次数 https://leetcode.cn/problems/unique-number-of-occurrences/
from typing import List
from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        d = dict()
        for k, v in counter.items():
            if d.get(v):
                return False
            d[v] = k
        return True


if __name__ == '__main__':
    obj = Solution()
    print(obj.uniqueOccurrences([1, 2]))  # False
    print(obj.uniqueOccurrences([1, 2, 2, 1, 1, 3]))  # True
    print(obj.uniqueOccurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))  # True
