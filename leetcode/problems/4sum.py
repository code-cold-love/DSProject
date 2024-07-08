#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 18. 四数之和 https://leetcode.cn/problems/4sum/
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 排序+双指针
        nums.sort()
        n, ans = len(nums), []
        for a in range(n - 3):
            if a > 0 and nums[a] == nums[a - 1]:
                continue  # 跳过重复数字
            if nums[a] + nums[a + 1] + nums[a + 2] + nums[a + 3] > target:
                break
            if nums[a] + nums[-3] + nums[-2] + nums[-1] < target:
                continue

            for b in range(a + 1, n - 2):
                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue  # 跳过重复数字
                if nums[a] + nums[b] + nums[b + 1] + nums[b + 2] > target:
                    break
                if nums[a] + nums[b] + nums[-2] + nums[-1] < target:
                    continue

                c = b + 1
                d = n - 1
                while c < d:
                    s = nums[a] + nums[b] + nums[c] + nums[d]
                    if s > target:
                        d -= 1
                    elif s < target:
                        c += 1
                    else:
                        ans.append([nums[a], nums[b], nums[c], nums[d]])
                        c += 1
                        while c < d and nums[c] == nums[c - 1]:
                            c += 1  # 跳过重复数字
                        d -= 1
                        while d > c and nums[d] == nums[d + 1]:
                            d -= 1  # 跳过重复数字
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.fourSum([2, 2, 2, 2, 2], 8))  # [[2, 2, 2, 2]]
    print(solution.fourSum([1, 0, -1, 0, -2, 2], 0))  # [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
