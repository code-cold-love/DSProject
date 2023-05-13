# -*- coding: utf-8 -*-
# 2441. 与对应负数同时存在的最大正整数 https://leetcode.cn/problems/largest-positive-integer-that-exists-with-its-negative/
from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        k = -1
        s = set(nums)
        for x in nums:
            if -x in s:
                k = max(k, x)
        return k

    def findMaxK_sort(self, nums: List[int]) -> int:
        nums.sort()
        i, j = 0, len(nums) - 1
        while i < j:
            while i < j and nums[i] < -nums[j]:
                i += 1
            if nums[i] == -nums[j]:
                return nums[j]
            j -= 1
        return -1


if __name__ == '__main__':
    obj = Solution()
    print(obj.findMaxK([-1, 2, -3, 3]))  # 3
