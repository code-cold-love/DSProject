#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2427. 公因子的数目 https://leetcode.cn/problems/number-of-common-factors/
class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        # 1 <= a, b <= 1000
        upper = min(a, b)
        ans = 0
        for i in range(1, upper + 1):
            if a % i == 0 and b % i == 0:
                ans += 1
        return ans


if __name__ == '__main__':
    obj = Solution()
    print(obj.commonFactors(12, 6))  # 4
    print(obj.commonFactors(25, 30))  # 2
