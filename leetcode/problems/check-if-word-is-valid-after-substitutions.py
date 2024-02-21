#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 1003. 检查替换后的词是否有效 https://leetcode.cn/problems/check-if-word-is-valid-after-substitutions/
class Solution:
    def isValid(self, s: str) -> bool:
        """辅助栈"""
        stk = []
        for c in s:
            stk.append(c)
            if ''.join(stk[-3:]) == 'abc':
                stk[-3:] = []
        return not stk

    def isValid_1(self, s: str) -> bool:
        """字符串"""
        while 'abc' in s:
            s = s.replace('abc', '')
            if s == '':
                return True
        return False


if __name__ == '__main__':
    obj = Solution()
    print(obj.isValid('aabcbc'))  # True
