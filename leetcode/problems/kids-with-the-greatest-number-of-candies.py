#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 1431. 拥有最多糖果的孩子 https://leetcode.cn/problems/kids-with-the-greatest-number-of-candies/
from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extra_candies: int) -> List[bool]:
        max_candy = max(candies)
        ans = [True if candy + extra_candies >= max_candy else False for candy in candies]
        return ans


if __name__ == '__main__':
    obj = Solution()
    print(obj.kidsWithCandies([2, 3, 5, 1, 3], 3))
    print(obj.kidsWithCandies([4, 2, 1, 1, 2], 1))
