#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 3174. 清除数字 https://leetcode.cn/problems/clear-digits/
class Solution:
    def clearDigits(self, s: str) -> str:
        # 1 <= len(s) <= 100
        stk = []
        for c in s:
            if c.isdigit():
                if stk:
                    stk.pop()
            else:
                stk.append(c)
        return ''.join(stk)


if __name__ == '__main__':
    solution = Solution()
    print(solution.clearDigits("abc"))  # "abc"
    print(solution.clearDigits("cb34"))  # ""
