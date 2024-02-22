#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 12. 整数转罗马数字 https://leetcode.cn/problems/integer-to-roman/
class Solution:
    VALUE_SYMBOLS = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I'),
    ]  # 从大到小排列

    def intToRoman(self, num: int) -> str:
        roman = list()
        for value, symbol in Solution.VALUE_SYMBOLS:
            while num >= value:  # 这个 while 循环很重要，尽可能多地用较大的数去减
                num -= value
                roman.append(symbol)
            if num == 0:
                break
        return "".join(roman)


if __name__ == '__main__':
    obj = Solution()
    print(obj.intToRoman(3))  # III
