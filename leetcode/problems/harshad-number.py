#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 3099. 哈沙德数 https://leetcode.cn/problems/harshad-number/
class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        total, y = 0, x
        while y:
            total += (y % 10)
            y //= 10
        return total if x % total == 0 else -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.sumOfTheDigitsOfHarshadNumber(18))  # 9
    print(solution.sumOfTheDigitsOfHarshadNumber(23))  # -1
