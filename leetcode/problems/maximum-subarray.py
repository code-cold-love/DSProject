# -*- coding: utf-8 -*-
# 53. 最大子数组和 https://leetcode.cn/problems/maximum-subarray/
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 动态规划
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])
        return max(dp)

    def maxSubArray_op(self, nums: List[int]) -> int:
        # 双指针，空间优化
        pre, res = 0, nums[0]
        for val in nums:
            pre = max(val, pre + val)
            res = max(res, pre)
        return res


if __name__ == '__main__':
    obj = Solution()
    print(obj.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
    print(obj.maxSubArray_op([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
