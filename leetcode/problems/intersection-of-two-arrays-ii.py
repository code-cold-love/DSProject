#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 350. 两个数组的交集 II https://leetcode.cn/problems/intersection-of-two-arrays-ii/
from typing import List
from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        cnt1, cnt2 = Counter(nums1), Counter(nums2)
        for k in cnt1.keys():
            if cnt2.get(k):
                frequency = min(cnt1[k], cnt2[k])
                ans += [k] * frequency
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.intersect([1, 2, 2, 1], [2, 2]))  # [2, 2]
    print(solution.intersect([4, 9, 5], [9, 4, 9, 8, 4]))  # [4, 9]
