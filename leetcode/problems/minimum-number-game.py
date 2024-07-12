#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2974. 最小数字游戏 https://leetcode.cn/problems/minimum-number-game/
from typing import List


class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        ans = []
        nums.sort()
        for i in range(0, len(nums), 2):
            a, b = nums[i], nums[i + 1]
            ans.append(b)
            ans.append(a)
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.numberGame([2, 5]))  # [5, 2]
    print(solution.numberGame([5, 4, 2, 3]))  # [3, 2, 5, 4]
