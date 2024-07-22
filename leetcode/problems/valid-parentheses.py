#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 20. 有效的括号 https://leetcode.cn/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        left_set = ('(', '[', '{')
        right_to_left = {')': '(', ']': '[', '}': '{'}
        for c in s:
            if c in left_set:
                stk.append(c)
            else:
                if not stk:
                    return False
                if right_to_left[c] != stk[-1]:
                    return False
                stk.pop()
        return True if not stk else False


if __name__ == '__main__':
    solution = Solution()
    print(solution.isValid("()"))  # True
    print(solution.isValid("(]"))  # False
    print(solution.isValid("()[]{}"))  # True
