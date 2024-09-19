#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2414. 最长的字母序连续子字符串的长度 https://leetcode.cn/problems/length-of-the-longest-alphabetical-continuous-substring/
class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        # s 仅由小写英文字母组成
        ans = tmp = 0
        for i, c in enumerate(s):
            if i == 0:
                tmp = 1
            elif ord(c) - 1 == ord(s[i - 1]):
                tmp += 1
            else:
                ans = max(ans, tmp)
                tmp = 1
        return max(ans, tmp)


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestContinuousSubstring('abcde'))  # 5
    print(solution.longestContinuousSubstring('abacaba'))  # 2
    print(solution.longestContinuousSubstring('yrpjofyzubfsiypfre'))  # 2
