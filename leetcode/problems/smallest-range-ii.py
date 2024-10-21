#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 910. 最小差值 II https://leetcode.cn/problems/smallest-range-ii/
from typing import List


class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        ma, mi = max(nums), min(nums)
        ans = ma - mi
        for i in range(len(nums) - 1):
            a, b = nums[i], nums[i + 1]
            ans = min(ans, max(ma - k, a + k) - min(mi + k, b - k))
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.smallestRangeII([1], 0))  # 0
    print(solution.smallestRangeII([0, 10], 2))  # 6
    print(solution.smallestRangeII([1, 3, 6], 3))  # 3
