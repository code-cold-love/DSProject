#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 392. 判断子序列 https://leetcode.cn/problems/is-subsequence/
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_len, t_len = len(s), len(t)
        if s_len > t_len:
            return False
        i = j = 0
        while i < s_len and j < t_len:
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == s_len


if __name__ == '__main__':
    obj = Solution()
    print(obj.isSubsequence('abc', 'ahbgdc'))  # True
