#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2455. 可被三整除的偶数的平均值 https://leetcode.cn/problems/average-value-of-even-numbers-that-are-divisible-by-three/
from typing import List


class Solution:
    def averageValue(self, nums: List[int]) -> int:
        n = total = 0
        for i in nums:
            if i % 6 == 0:
                n += 1
                total += i
        return total // n if n > 0 else 0


if __name__ == '__main__':
    obj = Solution()
    print(obj.averageValue([1, 3, 6, 10, 12, 15]))  # 9
