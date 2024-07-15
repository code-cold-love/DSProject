#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 28. 找出字符串中第一个匹配项的下标 https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h_len, n_len = len(haystack), len(needle)
        for i in range(h_len - n_len + 1):
            h_idx, n_idx = i, 0
            while n_idx < n_len and haystack[h_idx] == needle[n_idx]:
                h_idx += 1
                n_idx += 1
            if n_idx == n_len:
                return i
        return -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.strStr("leetcode", "leeto"))  # -1
    print(solution.strStr("sadbutsad", "sad"))  # 0
