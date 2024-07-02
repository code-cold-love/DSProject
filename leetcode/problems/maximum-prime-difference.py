#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 3115. 质数的最大距离 https://leetcode.cn/problems/maximum-prime-difference/
from math import sqrt
from typing import List


class Solution:
    @staticmethod
    def is_prime(x: int) -> bool:
        if x == 1:
            return False
        for i in range(2, int(sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True

    def maximumPrimeDifference(self, nums: List[int]) -> int:
        primes = []
        for i, x in enumerate(nums):
            if self.is_prime(x):
                primes.append(i)
        return primes[-1] - primes[0]


if __name__ == '__main__':
    solution = Solution()
    print(solution.maximumPrimeDifference([1, 7]))  # 0
    print(solution.maximumPrimeDifference([4, 8, 2, 8]))  # 0
    print(solution.maximumPrimeDifference([4, 2, 9, 5, 3]))  # 3
