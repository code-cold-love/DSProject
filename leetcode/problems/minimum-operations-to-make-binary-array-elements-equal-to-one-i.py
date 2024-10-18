#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 3191. 使二进制数组全部等于 1 的最少操作次数 I https://leetcode.cn/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # 3 <= len(nums) <= 10**5, 0 <= nums[i] <= 1
        ans = 0
        window = 3
        for i in range(0, len(nums) - window + 1):
            if nums[i] == 0:  # 必须操作
                nums[i] ^= 1
                nums[i + 1] ^= 1
                nums[i + 2] ^= 1
                ans += 1
        if nums[-1] == 0 or nums[-2] == 0:
            ans = -1
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.minOperations([0, 1, 1, 1]))  # -1
    print(solution.minOperations([0, 1, 1, 1, 0, 0]))  # 3
    print(solution.minOperations([1, 0, 0, 1, 1, 0, 1, 1, 1]))  # -1
