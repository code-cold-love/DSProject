#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 605. 种花问题 https://leetcode.cn/problems/can-place-flowers/
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i, s = 0, len(flowerbed)
        while i < s and 0 < n:
            if flowerbed[i] == 1:
                i += 2
            elif (i == s - 1) or (flowerbed[i + 1] == 0):
                n -= 1
                i += 2
            else:
                i += 3
        return n <= 0


if __name__ == '__main__':
    obj = Solution()
    print(obj.canPlaceFlowers([1, 0, 0, 0, 1], n=1))  # True
    print(obj.canPlaceFlowers([1, 0, 0, 0, 1], n=2))  # False
