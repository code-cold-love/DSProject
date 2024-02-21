#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2171. 拿出最少数目的魔法豆 https://leetcode.cn/problems/removing-minimum-number-of-magic-beans/
from typing import List


class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        n = len(beans)
        ans = total = sum(beans)
        for i in range(n):
            ans = min(ans, total - beans[i] * (n - i))  # (n - i) 为豆子数大于等于 beans[i] 的袋子数量
        return ans


if __name__ == '__main__':
    obj = Solution()
    print(obj.minimumRemoval([4, 1, 6, 5]))  # 4
    print(obj.minimumRemoval([2, 10, 3, 2]))  # 7
