#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 640. 求解方程 https://leetcode.cn/problems/solve-the-equation/
class Solution:
    def solveEquation(self, equation: str) -> str:
        # 模拟
        factor = val = 0  # factor 表示变量的系数
        i, n = 0, len(equation)
        sign = 1  # 等式左边默认系数为正
        while i < n:
            if equation[i] == '=':  # 找到等号
                i += 1
                sign = -1  # 等式右边默认系数为负，即把右边移到左边
                continue
            s = sign
            if equation[i] == '+':
                i += 1
            elif equation[i] == '-':
                s = -s
                i += 1
            num, flag = 0, False  # num 记录数字，flag 表示 num 是否有效
            while i < n and equation[i].isdigit():
                flag = True
                num = num * 10 + int(equation[i])
                i += 1
            if i < n and equation[i] == 'x':  # 变量
                factor += s * num if flag else s
                i += 1
            else:  # 数值
                val += s * num

        if factor == 0:
            return 'No solution' if val else 'Infinite solutions'
        return f'x={-val // factor}'


if __name__ == '__main__':
    obj = Solution()
    print(obj.solveEquation('2x=x'))  # x=0
    print(obj.solveEquation('x=x'))  # Infinite solutions
    print(obj.solveEquation('x+5-3+x=6+x-2'))  # x=2
