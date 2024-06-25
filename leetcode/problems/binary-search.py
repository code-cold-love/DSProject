#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 704. 二分查找 https://leetcode.cn/problems/binary-search/
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1  # 左闭右闭
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1


if __name__ == '__main__':
    obj = Solution()
    print(obj.search(nums=[-1, 0, 3, 5, 9, 12], target=9))  # 4
    print(obj.search(nums=[-1, 0, 3, 5, 9, 12], target=2))  # -1
