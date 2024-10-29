#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 78. 子集 https://leetcode.cn/problems/subsets/
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # nums 是不含重复元素的整数数组
        ans = []
        path = []  # 为子集收集元素

        def backtrack(idx: int, n: int) -> None:
            ans.append(path[:])  # 收集子集要放在终止添加的上面

            # if start >= n:  # 没有元素可取了
            #     return
            for j in range(idx, n):  # 枚举选择的数字
                path.append(nums[j])
                backtrack(j + 1, n)
                path.pop()

        backtrack(0, len(nums))
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.subsets([0]))  # [[], [0]]
    print(solution.subsets([1, 2, 3]))  # [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
