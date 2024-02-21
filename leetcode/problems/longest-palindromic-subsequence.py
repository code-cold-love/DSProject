#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 516. 最长回文子序列 https://leetcode.cn/problems/longest-palindromic-subsequence/
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 1
        elif n == 2:
            return 2 if s[0] == s[1] else 1
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][-1]


if __name__ == '__main__':
    obj = Solution()
    print(obj.longestPalindromeSubseq('ab'))  # 1
    print(obj.longestPalindromeSubseq('aa'))  # 2
    print(obj.longestPalindromeSubseq('abb'))  # 2
    print(obj.longestPalindromeSubseq('bab'))  # 3
    print(obj.longestPalindromeSubseq('cbbd'))  # 2
    print(obj.longestPalindromeSubseq('bbbab'))  # 4
