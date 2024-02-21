#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2465. 不同的平均值数目 https://leetcode.cn/problems/number-of-distinct-averages/
from typing import List


class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        n, avg = len(nums), set()
        nums.sort()
        i, j = 0, n - 1
        while i < j:
            avg.add((nums[i] + nums[j]) / 2)
            i += 1
            j -= 1
        return len(avg)


if __name__ == '__main__':
    obj = Solution()
    print(obj.distinctAverages([4, 1, 4, 0, 3, 5]))  # 2
