#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2601. 质数减法运算 https://leetcode.cn/problems/prime-subtraction-operation/
from typing import List
from bisect import bisect_left


class Solution:
    def __init__(self):
        self.MX = 1000
        self.is_prime, self.prime = self.pre_process()

    def pre_process(self):
        """预处理小于 1000 的质数"""
        is_prime = [True] * self.MX
        prime = [0]  # 哨兵，避免二分越界
        for i in range(2, self.MX):
            if is_prime[i]:
                prime.append(i)  # 预处理质数列表
                for j in range(i * i, self.MX, i):
                    is_prime[j] = False
        return is_prime, prime

    def primeSubOperation(self, nums: List[int]) -> bool:
        # 1 <= len(nums) <= 1000，1 <= nums[i] <= 1000
        pre = 0  # 上一个减完后的数字
        for x in nums:
            if x <= pre:
                return False
            # p 是满足 x - p > pre 的最大质数，即 p 是小于 x - pre 的最大质数
            pre = x - self.prime[bisect_left(self.prime, x - pre) - 1]  # 减去 < x-pre 的最大质数
        return True


if __name__ == '__main__':
    obj = Solution()
    print(obj.primeSubOperation([2, 2]))  # False
    print(obj.primeSubOperation([4, 9, 6, 10]))  # True
    print(obj.primeSubOperation([6, 8, 11, 12]))  # True
