#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 844. 比较含退格的字符串 https://leetcode.cn/problems/backspace-string-compare/
class Solution:
    @staticmethod
    def process_backspace(s: str) -> str:
        ans = []
        for c in s:
            if c != '#':
                ans.append(c)
            else:
                if ans:
                    ans.pop()
        return ''.join(ans)

    def backspaceCompare(self, s: str, t: str) -> bool:
        s, t = self.process_backspace(s), self.process_backspace(t)
        return s == t


if __name__ == '__main__':
    solution = Solution()
    print(solution.backspaceCompare('ab#c', 'ad#c'))  # True
    print(solution.backspaceCompare('ab##', 'c#d#'))  # True
    print(solution.backspaceCompare('a#c', 'b'))  # False
