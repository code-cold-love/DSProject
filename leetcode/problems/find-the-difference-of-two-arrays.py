# -*- coding: utf-8 -*-
# 2215. 找出两数组的不同 https://leetcode.cn/problems/find-the-difference-of-two-arrays/
from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)  # nums1 所有元素的哈希集合
        set2 = set(nums2)  # nums2 所有元素的哈希集合
        return [list(set1 - set2), list(set2 - set1)]


if __name__ == '__main__':
    obj = Solution()
    print(obj.findDifference(nums1=[1, 2, 3], nums2=[2, 4, 6]))  # [[1, 3], [4, 6]]
