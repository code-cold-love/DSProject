#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 1227. 飞机座位分配概率 https://leetcode.cn/problems/airplane-seat-assignment-probability/
class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        return 1.0 if n == 1 else 0.5


if __name__ == '__main__':
    solution = Solution()
    print(solution.nthPersonGetsNthSeat(1))  # 1.00
    print(solution.nthPersonGetsNthSeat(2))  # 0.50
