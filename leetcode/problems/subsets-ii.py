#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 90. 子集 II https://leetcode.cn/problems/subsets-ii/
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # nums 可能包含重复元素
        ans = []
        path = []
        nums.sort()  # 去重需要排序

        def backtrack(idx: int, n: int) -> None:
            ans.append(path[:])

            for j in range(idx, n):
                if j > idx and nums[j] == nums[j - 1]:
                    # 前后元素相同时，跳入下一个循环去重
                    continue
                path.append(nums[j])
                backtrack(j + 1, n)
                path.pop()

        backtrack(0, len(nums))
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.subsetsWithDup([0]))  # [[], [0]]
    print(solution.subsetsWithDup([1, 2, 2]))  # [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
    print(solution.subsetsWithDup([4, 4, 4, 1, 4]))
