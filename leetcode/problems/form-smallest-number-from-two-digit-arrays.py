#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2605. 从两个数字数组里生成最小数字 https://leetcode.cn/problems/form-smallest-number-from-two-digit-arrays/
from typing import List


class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        # nums1、nums2 只包含 1 到 9，每个数组中的元素互不相同
        ans = []
        min_1 = nums1[0]
        for i in nums1:
            if i in nums2:
                ans.append(i)
            if i < min_1:
                min_1 = i
        min_2 = min(nums2)
        ans.append(min_1 * 10 + min_2)
        ans.append(min_2 * 10 + min_1)
        return min(ans)

    def minNumber_1(self, nums1: List[int], nums2: List[int]) -> int:
        res = []
        nums1.sort()
        nums2.sort()
        for x in nums1:
            if x in nums2:
                res.append(x)
        res.append(nums1[0] * 10 + nums2[0])
        res.append(nums2[0] * 10 + nums1[0])
        return min(res)


if __name__ == '__main__':
    obj = Solution()
    print(obj.minNumber(nums1=[4, 1, 3], nums2=[5, 7]))  # 15
    print(obj.minNumber(nums1=[3, 5, 2, 6], nums2=[3, 1, 7]))  # 3

    print(obj.minNumber_1(nums1=[4, 1, 3], nums2=[5, 7]))  # 15
    print(obj.minNumber_1(nums1=[3, 5, 2, 6], nums2=[3, 1, 7]))  # 3
