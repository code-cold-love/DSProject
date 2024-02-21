#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2908. 元素和最小的山形三元组 I https://leetcode.cn/problems/minimum-sum-of-mountain-triplets-i/
from math import inf
from typing import List


class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        # nums.length > 3
        n, pre_min = 1, [nums[0]]  # pre_min[i] 表示 nums[0: i + 1] 之间的最小值
        for v in nums[1:]:
            n += 1
            pre_min.append(min(pre_min[-1], v))
        suf_min = nums[n - 1]
        ans = inf
        for i in range(n - 2, 0, -1):
            if pre_min[i - 1] < nums[i] and nums[i] > suf_min:
                ans = min(pre_min[i - 1] + nums[i] + suf_min, ans)
            suf_min = min(nums[i], suf_min)
        return ans if ans < inf else -1


if __name__ == '__main__':
    obj = Solution()
    print(obj.minimumSum([1, 2, 1, 2]))  # 4
    print(obj.minimumSum([8, 6, 1, 5, 3]))  # 9
    print(obj.minimumSum([5, 4, 8, 7, 10, 2]))  # 13
    print(obj.minimumSum([6, 5, 4, 3, 4, 5]))  # -1
