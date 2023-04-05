# -*- coding: utf-8 -*-
# 35. 搜索插入位置 https://leetcode.cn/problems/search-insert-position/
from typing import List
from bisect import bisect_left


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        pos = bisect_left(nums, target)
        return pos


if __name__ == '__main__':
    obj = Solution()
    print(obj.searchInsert(nums=[1, 3, 5, 6], target=5))  # 2
    print(obj.searchInsert(nums=[1, 3, 5, 6], target=2))  # 1
    print(obj.searchInsert(nums=[1, 3, 5, 6], target=7))  # 4
