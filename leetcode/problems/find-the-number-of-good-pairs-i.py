#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 3162. 优质数对的总数 I https://leetcode.cn/problems/find-the-number-of-good-pairs-i/
from collections import Counter
from typing import List


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        ans = 0
        cnt_a = Counter(nums1)
        max_a = max(cnt_a)  # max(cnt_a.keys())
        for b, freq in Counter(nums2).items():
            s = sum(cnt_a.get(y, 0) for y in range(b * k, max_a + 1, b * k))
            ans += s * freq
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.numberOfPairs([1, 3, 4], [1, 3, 4], 1))  # 5
