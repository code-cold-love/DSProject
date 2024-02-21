#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 47. 全排列 II https://leetcode.cn/problems/permutations-ii/
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        visited = [0] * n

        def backtrack(i: int, arr: List[int]):
            if i == n:  # 终止条件
                ans.append(arr)
                return
            for j in range(n):  # 回溯范围
                if visited[j] == 1:
                    continue
                elif j > 0 and nums[j] == nums[j - 1] and visited[j - 1] == 0:  # 剪枝优化
                    continue
                else:
                    visited[j] = 1
                    backtrack(i + 1, arr + [nums[j]])
                    visited[j] = 0  # 撤销操作

        backtrack(0, [])
        return ans


if __name__ == '__main__':
    obj = Solution()
    print(obj.permuteUnique([1, 1, 2]))  # [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
    print(obj.permuteUnique([1, 2, 3]))  # [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
