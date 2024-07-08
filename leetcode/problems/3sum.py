#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 15. 三数之和 https://leetcode.cn/problems/3sum/
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 题目要求三数和为 0
        nums.sort()
        n, ans = len(nums), []
        for k in range(n - 2):
            if nums[k] > 0:
                break
            if k > 0 and nums[k] == nums[k - 1]:
                continue  # 跳过一样值的
            i, j = k + 1, n - 1
            while i < j:
                s = nums[i] + nums[j] + nums[k]
                if s < 0:
                    i += 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                elif s > 0:
                    j -= 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
                else:
                    ans.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.threeSum([0, 1, 1]))  # []
    print(solution.threeSum([-1, 0, 1, 2, -1, -4]))  # [[-1, -1, 2], [-1, 0, 1]]
