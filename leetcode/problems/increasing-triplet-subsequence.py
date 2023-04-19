# -*- coding: utf-8 -*-
# 334. 递增的三元子序列 https://leetcode.cn/problems/increasing-triplet-subsequence/
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        first, second = nums[0], float('inf')
        for i in range(1, n):
            if nums[i] > second:
                return True
            elif nums[i] > first:
                second = nums[i]
            else:
                first = nums[i]
        return False


if __name__ == '__main__':
    obj = Solution()
    print(obj.increasingTriplet([5, 4, 3, 2, 1]))  # False
    print(obj.increasingTriplet([1, 2, 3, 4, 5]))  # True
    print(obj.increasingTriplet([2, 1, 5, 0, 4, 6]))  # True
