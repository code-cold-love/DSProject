# -*- coding: utf-8 -*-
# 643. 子数组最大平均数 I https://leetcode.cn/problems/maximum-average-subarray-i/
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans = sum(nums[:k])
        tmp = ans
        for i in range(len(nums) - k):
            tmp = tmp - nums[i] + nums[i + k]
            if tmp > ans:
                ans = tmp
        return ans / k


if __name__ == '__main__':
    obj = Solution()
    print(obj.findMaxAverage([5], 1))  # 5
    print(obj.findMaxAverage([1, 12, -5, -6, 50, 3], 4))  # 12.75
