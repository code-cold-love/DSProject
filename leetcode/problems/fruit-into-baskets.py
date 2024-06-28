#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 904. 水果成篮 https://leetcode.cn/problems/fruit-into-baskets/
from collections import Counter
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        cnt = Counter()
        ans = left = 0
        for right, fruit in enumerate(fruits):
            cnt[fruit] += 1
            while len(cnt) > 2:
                cnt[fruits[left]] -= 1
                if cnt[fruits[left]] == 0:
                    cnt.pop(fruits[left])
                left += 1  # 移动窗口左边界
            ans = max(ans, right - left + 1)

        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.totalFruit([1, 2, 1]))  # 3
    print(solution.totalFruit([0, 1, 2, 2]))  # 3
