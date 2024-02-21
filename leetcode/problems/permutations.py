#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 46. 全排列 https://leetcode.cn/problems/permutations/
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []

        def backtrack(first: int = 0):
            if first == n:  # 所有数均填完
                ans.append(nums[:])
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]  # 交换维护数组
                backtrack(first + 1)  # 继续递归地填下一个数
                nums[first], nums[i] = nums[i], nums[first]  # 撤销操作

        backtrack()
        return ans


if __name__ == '__main__':
    obj = Solution()
    print(obj.permute([1, 2, 3]))  # [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]
