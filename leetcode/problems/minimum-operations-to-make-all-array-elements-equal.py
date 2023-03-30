# -*- coding: utf-8 -*-
# 2602. 使数组元素全部相等的最少操作次数 https://leetcode.cn/problems/minimum-operations-to-make-all-array-elements-equal/
from typing import List
from bisect import bisect_left
from itertools import accumulate


class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        # n == nums.length
        # m == queries.length
        # 1 <= n, m <= 105
        # 1 <= nums[i], queries[i] <= 10**9
        nums.sort()  # 排序
        n = len(nums)
        acc = [0] + list(accumulate(nums))  # 前缀和数组
        ans = []
        for q in queries:
            i = bisect_left(nums, q)
            left = q * i - acc[i]  # 左边的小于 q
            right = acc[n] - acc[i] - q * (n - i)  # 右边的大于 q
            ans.append(left + right)
        return ans


if __name__ == '__main__':
    obj = Solution()
    print(obj.minOperations([2, 9, 6, 3], [10]))  # [20]
    print(obj.minOperations([3, 1, 6, 8], [1, 5]))  # [14, 10]
