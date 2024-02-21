#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2909. 元素和最小的山形三元组 II https://leetcode.cn/problems/minimum-sum-of-mountain-triplets-ii/
from math import inf
from typing import List


class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        pre_min, suf_min = [inf] * n, [inf] * n
        pre_min[0] = nums[0]
        suf_min[-1] = nums[n - 1]
        for i in range(1, n):
            pre_min[i] = min(pre_min[i - 1], nums[i])
        for k in range(n - 2, -1, -1):
            suf_min[k] = min(suf_min[k + 1], nums[k])
        ans = inf
        for j in range(1, n - 1):
            if pre_min[j - 1] < nums[j] > suf_min[j + 1]:
                ans = min(ans, pre_min[j - 1] + nums[j] + suf_min[j + 1])
        return ans if ans < inf else -1


if __name__ == '__main__':
    obj = Solution()
    print(obj.minimumSum([8, 6, 1, 5, 3]))  # 9
    print(obj.minimumSum([5, 4, 8, 7, 10, 2]))  # 13
    print(obj.minimumSum([6, 5, 4, 3, 4, 5]))  # -1
