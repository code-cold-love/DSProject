#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 459. 重复的子字符串 https://leetcode.cn/problems/repeated-substring-pattern/
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # 掐头去尾字符串匹配
        return s in (s + s)[1:-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.repeatedSubstringPattern("aba"))  # False
    print(solution.repeatedSubstringPattern("abab"))  # True
