#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 88. 合并两个有序数组 https://leetcode.cn/problems/merge-sorted-array/
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # nums1 和 nums2 都是按非递减顺序排列，nums1 的初始长度为 m + n
        # 逆向双指针
        idx1, idx2 = m - 1, n - 1
        tail = m + n - 1
        while idx1 >= 0 or idx2 >= 0:
            if idx1 == -1:
                nums1[tail] = nums2[idx2]
                idx2 -= 1
            elif idx2 == -1:
                nums1[tail] = nums1[idx1]
                idx1 -= 1
            elif nums1[idx1] > nums2[idx2]:
                nums1[tail] = nums1[idx1]
                idx1 -= 1
            else:
                nums1[tail] = nums2[idx2]
                idx2 -= 1
            tail -= 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.merge([1], 1, [], 0))  # [1]
    print(solution.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))  # [1, 2, 2, 3, 5, 6]
