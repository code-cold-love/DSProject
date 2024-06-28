#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 76. 最小覆盖子串 https://leetcode.cn/problems/minimum-window-substring/
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_n, t_n = len(s), len(t)
        if s_n < t_n:
            return ''
        if s_n == t_n:
            return s if Counter(s) == Counter(t) else ''

        left, right = -1, s_n
        s_cnt = Counter()
        t_cnt = Counter(t)
        i_left = 0
        for i_right, c in enumerate(s):
            s_cnt[c] += 1
            while s_cnt >= t_cnt:  # 涵盖的情况
                if i_right - i_left < right - left:  # 更短的子串
                    left, right = i_left, i_right
                s_cnt[s[i_left]] -= 1  # 左端点字母移出窗口
                i_left += 1  # 移动窗口左端点
        return '' if left < 0 else s[left: right + 1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.minWindow('a', 'a'))  # 'a'
    print(solution.minWindow('a', 'aa'))  # ''
    print(solution.minWindow('ADOBECODEBANC', 'ABC'))  # 'BANC'
