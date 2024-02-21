#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 592. 分数加减运算 https://leetcode.cn/problems/fraction-addition-and-subtraction/
from math import gcd


class Solution:
    # 本题只会遇到 +-/ 和 0-9 数字
    def fractionAddition(self, expression: str) -> str:
        x, y = 0, 1  # 初始分子、分母
        i, n = 0, len(expression)
        while i < n:
            # 读取分子
            x1, sign = 0, 1
            if expression[i] == '-':
                sign = -1
                i += 1
            elif expression[i] == '+':
                i += 1
            while i < n and expression[i].isdigit():  # 直到读到 / 停止
                x1 = x1 * 10 + int(expression[i])
                i += 1
            x1 = sign * x1
            i += 1

            # 读取分母
            y1 = 0
            while i < n and expression[i].isdigit():  # 直到读到 + 或 - 停止
                y1 = y1 * 10 + int(expression[i])
                i += 1

            # 更新初始分子、分母
            x = x * y1 + x1 * y
            y *= y1

        if x == 0:
            return '0/1'
        g = gcd(abs(x), y)
        return f'{x // g}/{y // g}'


if __name__ == '__main__':
    obj = Solution()
    print(obj.fractionAddition('1/3-1/2'))  # -1/6
    print(obj.fractionAddition('-1/2+1/2'))  # 0/1
    print(obj.fractionAddition('-1/2+1/2+1/3'))  # 1/3
