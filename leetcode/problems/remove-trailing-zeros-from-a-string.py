#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2710. 移除字符串中的尾随零 https://leetcode.cn/problems/remove-trailing-zeros-from-a-string/
class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        # num 仅由数字组成，不含前导零
        non_zero = 0
        for i, n in enumerate(num):
            if n != '0':
                non_zero = i
        return num[:non_zero + 1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.removeTrailingZeros('123'))  # '123'
    print(solution.removeTrailingZeros('51230100'))  # '512301'
