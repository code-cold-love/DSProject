#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 349. 两个数组的交集 https://leetcode.cn/problems/intersection-of-two-arrays/
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1, set2 = set(nums1), set(nums2)
        return list(set1 & set2)


if __name__ == '__main__':
    solution = Solution()
    print(solution.intersection([1, 2, 2, 1], [2, 2]))  # [2]
    print(solution.intersection([4, 9, 5], [9, 4, 9, 8, 4]))  # [9, 4]
