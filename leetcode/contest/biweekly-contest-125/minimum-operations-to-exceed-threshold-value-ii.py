# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 3066. 超过阈值的最少操作数 II https://leetcode.cn/problems/minimum-operations-to-exceed-threshold-value-ii/
from heapq import heapify, heappop, heapreplace
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        heapify(nums)
        while nums[0] < k:
            i = heappop(nums)  # 最小值
            heapreplace(nums, i * 2 + nums[0])  # Pop and return the current smallest value, and add the new item
            ans += 1
        return ans


if __name__ == '__main__':
    obj = Solution()
    print(obj.minOperations([1, 1, 2, 4, 9], 20))  # 4
    print(obj.minOperations([2, 11, 10, 1, 3], 10))  # 2
