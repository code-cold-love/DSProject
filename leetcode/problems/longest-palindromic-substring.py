#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 5. 最长回文子串 https://leetcode.cn/problems/longest-palindromic-substring/
class Solution:
    def longestPalindrome(self, s: str) -> str:
        """中心边界扩展法"""
        n = len(s)

        def expand_around_center(left: int, right: int):
            # left 和 right 是回文中心的左右边界
            while left >= 0 and right < n and s[left] == s[right]:
                # 从回文中心开始一直向左右两边扩展，直到抵达字符串边界或者不符合回文条件
                left -= 1
                right += 1
            return left + 1, right - 1

        start = end = 0
        for i in range(n):
            # 枚举边界情况（即子串长度为 1 或 2 的情况），等价于枚举所有的回文中心
            l1, r1 = expand_around_center(i, i)
            l2, r2 = expand_around_center(i, i + 1)
            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2
        return s[start: end + 1]


if __name__ == '__main__':
    obj = Solution()
    print(obj.longestPalindrome("cbbd"))  # bb
    print(obj.longestPalindrome("babad"))  # bab
