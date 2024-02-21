#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 1630. 等差子数组 https://leetcode.cn/problems/arithmetic-subarrays/
from typing import List


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        # 2 <= len(nums) <= 500
        # 1 <= len(l) = len(r) <= 500
        # 0 <= l[i] < r[i] < len(nums)
        def check(tmp: List[int]) -> bool:
            tmp.sort()
            diff = tmp[1] - tmp[0]
            n = len(tmp)
            for t in range(n - 1):
                if tmp[t + 1] - tmp[t] == diff:
                    continue
                return False
            return True

        return [check(nums[left: right + 1]) for left, right in zip(l, r)]

    def checkArithmeticSubarrays_1(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        """数学+模拟"""

        def check(nums: List[int], left: int, right: int):
            n = right - left + 1
            s = set(nums[left: right + 1])
            min_val, max_val = min(s), max(s)
            d, mod = divmod(max_val - min_val, n - 1)
            return mod == 0 and all((min_val + (i - 1) * d) in s for i in range(1, n))

        return [check(nums, left, right) for left, right in zip(l, r)]


if __name__ == '__main__':
    obj = Solution()
    print(obj.checkArithmeticSubarrays([4, 6, 5, 9, 3, 7], [0, 0, 2], [2, 3, 5]))  # [True, False, True]
    print(obj.checkArithmeticSubarrays_1([4, 6, 5, 9, 3, 7], [0, 0, 2], [2, 3, 5]))  # [True, False, True]
