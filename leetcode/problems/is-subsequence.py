#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 392. 判断子序列 https://leetcode.cn/problems/is-subsequence/
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        elif s and not t:
            return False
        s_len, t_len = len(s), len(t)
        if s_len > t_len:
            return False
        i = j = 0
        while i < s_len and j < t_len:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        if i == s_len:
            return True
        return False


if __name__ == '__main__':
    obj = Solution()
    print(obj.isSubsequence('abc', 'ahbgdc'))  # True
