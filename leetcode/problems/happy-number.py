#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 202. 快乐数 https://leetcode.cn/problems/happy-number/
class Solution:
    @staticmethod
    def calculate_happy(n: int) -> int:
        m = 0
        while n:
            n, d = divmod(n, 10)
            m += pow(d, 2)
        return m

    def isHappy(self, n: int) -> bool:
        s = set()
        while True:
            m = self.calculate_happy(n)
            if m == 1:
                return True
            elif m in s:
                return False
            else:
                n = m
                s.add(m)


if __name__ == '__main__':
    solution = Solution()
    print(solution.isHappy(2))  # False
    print(solution.isHappy(19))  # True
