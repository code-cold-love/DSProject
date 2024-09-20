#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 357. 统计各位数字都不同的数字个数 https://leetcode.cn/problems/count-numbers-with-unique-digits/
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        # 统计并返回【各位数字都不同】的数字 x 的个数，其中 0 <= x <= 10**n
        if n == 0:  # 0 <= x < 1，x 只能为 0
            return 1
        elif n == 1:  # 0 <= x < 10，x 有 0~9 十种选择
            return 10
        else:
            ans, curr = 10, 9
            # 当 x 是多位数时，第一位选择有 9 种，即 1~9；第二位选择有 10-1 种，即 0~9 中去除第一位的选择；
            # 第三位选择有 10-2 种，即 0~9 中去除第一位、第二位的选择......
            for i in range(n - 1):
                curr *= 9 - i
                ans += curr
            return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.countNumbersWithUniqueDigits(0))  # 1
    print(solution.countNumbersWithUniqueDigits(2))  # 91
