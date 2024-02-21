#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2614. 对角线上的质数 https://leetcode.cn/problems/prime-in-diagonal/
from typing import List


class Solution:
    @staticmethod
    def is_prime(n: int) -> bool:
        if n < 2:  # 1 不是质数
            return False
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1
        return True

    def diagonalPrime(self, nums: List[List[int]]) -> int:
        ans = 0
        for i, row in enumerate(nums):
            for x in (row[i], row[-1 - i]):  # 同一行两个对角线上的值
                if x > ans and self.is_prime(x):
                    ans = x
        return ans


if __name__ == '__main__':
    obj = Solution()
    print(obj.diagonalPrime([[1, 2, 3], [5, 6, 7], [9, 10, 11]]))  # 11
