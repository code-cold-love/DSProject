#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 908. 最小差值 I https://leetcode.cn/problems/smallest-range-i/
from typing import List


class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        max_num, min_num = max(nums), min(nums)
        return max(0, max_num - k - (min_num + k))


if __name__ == "__main__":
    solution = Solution()
    print(solution.smallestRangeI([1], 0))  # 0
    print(solution.smallestRangeI([0, 10], 2))  # 6
    print(solution.smallestRangeI([1, 3, 6], 3))  # 0
