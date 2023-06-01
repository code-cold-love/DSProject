# -*- coding: utf-8 -*-
# 2517. 礼盒的最大甜蜜度 https://leetcode.cn/problems/maximum-tastiness-of-candy-basket/
from math import inf
from typing import List


class Solution:
    _price = []

    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        self._price = price
        low, high = 0, price[-1] - price[0]  # 二分查找上下界
        while low < high:
            mid = (low + high + 1) // 2
            if self.check(k, mid) is True:
                low = mid
            else:
                high = mid - 1
        return low

    def check(self, k: int, sweetness: int) -> bool:
        prev = -inf
        cnt = 0
        for p in self._price:
            if p - prev >= sweetness:
                cnt += 1
                prev = p
        return cnt >= k


if __name__ == '__main__':
    obj = Solution()
    print(obj.maximumTastiness([13, 5, 1, 8, 21, 2], 3))  # 8
