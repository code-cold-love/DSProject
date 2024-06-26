#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 26. 删除有序数组中的重复项 https://leetcode.cn/problems/remove-duplicates-from-sorted-array/
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # nums 非严格递增
        n = len(nums)
        fast, slow = 1, 0
        while slow <= fast < n:
            while fast < n and nums[slow] == nums[fast]:
                fast += 1
            if fast == n:
                break
            slow += 1
            nums[slow] = nums[fast]
        return slow + 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.removeDuplicates([1, 1, 2]))  # 2
    print(solution.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))  # 5
