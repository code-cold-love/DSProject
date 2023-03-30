# -*- coding: utf-8 -*-
# 2602. 使数组元素全部相等的最少操作次数 https://leetcode.cn/problems/minimum-operations-to-make-all-array-elements-equal/
from bisect import bisect_left
from itertools import accumulate
from typing import List


class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        # n == nums.length
        # m == queries.length
        # 1 <= n, m <= 105
        # 1 <= nums[i], queries[i] <= 10**9
        nums.sort()
        n = len(nums)
        acc = [0] + list(accumulate(nums))  # 前缀和数组
        ans = []
        for q in queries:
            i = bisect_left(nums, q)
            left = q * i - acc[i]
            right = acc[n] - acc[i] - q * (n - i)
            ans.append(left + right)
        return ans


if __name__ == '__main__':
    obj = Solution()
    print(obj.minOperations([2, 9, 6, 3], [10]))  # [20]
    print(obj.minOperations([3, 1, 6, 8], [1, 5]))  # [14, 10]
    # (3+2) + (1+4) + (6-1) + (8-3) = 5 * 4
    # (3+1+6+8) + (2+4-1-3) = 5 * 4
