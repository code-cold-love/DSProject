# -*- coding: utf-8 -*-
# 2342. 数位和相等数对的最大和 https://leetcode.cn/problems/max-sum-of-a-pair-with-equal-sum-of-digits/
from typing import List
from collections import defaultdict


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        d = defaultdict(int)
        ans = -1
        for num in nums:
            digits_sum = sum(int(c) for c in str(num))
            if digits_sum in d:
                ans = max(ans, d[digits_sum] + num)
                d[digits_sum] = max(d[digits_sum], num)
            else:
                d[digits_sum] = num
        return ans


if __name__ == '__main__':
    obj = Solution()
    print(obj.maximumSum([18, 43, 36, 13, 7]))  # 54
    print(obj.maximumSum([10, 12, 19, 14]))  # -1
