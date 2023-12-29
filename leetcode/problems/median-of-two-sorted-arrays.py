# -*- coding: utf-8 -*-
# 4. 寻找两个正序数组的中位数 https://leetcode.cn/problems/median-of-two-sorted-arrays/
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        left = right = 0.0
        if m == 0 and n == 0:
            ...
        elif m == 0 and n:
            right = nums2[n // 2]
            left = right if n % 2 else nums2[n // 2 - 1]
        elif n == 0 and m:
            right = nums1[m // 2]
            left = right if m % 2 else nums1[m // 2 - 1]
        else:
            tmp = [0] * (m + n)  # 辅助数组
            i = j = k = 0
            while i < m and j < n:
                if nums1[i] <= nums2[j]:
                    tmp[k] = nums1[i]
                    i += 1
                    k += 1
                else:
                    tmp[k] = nums2[j]
                    j += 1
                    k += 1
            while i < m:
                tmp[k] = nums1[i]
                i += 1
                k += 1
            while j < n:
                tmp[k] = nums2[j]
                j += 1
                k += 1
            right = tmp[(m + n) // 2]
            left = right if (m + n) % 2 else tmp[(m + n) // 2 - 1]
        return (left + right) / 2


if __name__ == '__main__':
    obj = Solution()
    print(obj.findMedianSortedArrays([1, 3], [2]))  # 2.00
    print(obj.findMedianSortedArrays([1, 2], [3, 4]))  # 2.50
