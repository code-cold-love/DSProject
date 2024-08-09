#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 3132. 找出与数组相加的整数 II https://leetcode.cn/problems/find-the-integer-added-to-array-ii/
from typing import List


class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        # 测试用例以这样的方式生成：存在一个整数 x，nums1 中的每个元素都与 x 相加后，再移除两个元素，nums1 可以与 nums2 相等
        # 返回能够实现数组相等的最小整数 x
        # 3 <= nums1.length == nums2.length + 2 <= 200
        # 排序 + 判断子序列
        nums1.sort()
        nums2.sort()
        m, n = len(nums1), len(nums2)
        for i in [2, 1, 0]:  # 枚举 nums1 中的前三小的
            left, right = i + 1, 1
            x = nums2[0] - nums1[i]

            # 双指针法判断子序列
            while left < m and right < n:
                if nums2[right] - nums1[left] == x:
                    right += 1
                left += 1
            if right == n:
                return x
        return 0


if __name__ == '__main__':
    solution = Solution()
    print(solution.minimumAddedInteger([3, 5, 5, 3], [7, 7]))  # 2
    print(solution.minimumAddedInteger([4, 6, 3, 1, 4, 2, 10, 9, 5], [5, 10, 3, 2, 6, 1, 9]))  # 0
