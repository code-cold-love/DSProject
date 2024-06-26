#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 27. 移除元素 https://leetcode.cn/problems/remove-element/
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        slow = 0
        for fast in range(n):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
        return slow


if __name__ == '__main__':
    solution = Solution()
    print(solution.removeElement([3, 2, 2, 3], 3))  # 2
