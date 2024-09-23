#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 3289. 数字小镇中的捣蛋鬼 https://leetcode.cn/problems/the-two-sneaky-numbers-of-digitville/
from typing import List


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        counter, cnt = set(), 0
        for num in nums:
            if num in counter:
                cnt += 1
                ans.append(num)
                if cnt == 2:
                    return ans
            counter.add(num)
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.getSneakyNumbers([0, 1, 1, 0]))  # [0, 1]
    print(solution.getSneakyNumbers([0, 3, 2, 1, 3, 2]))  # [2, 3]
