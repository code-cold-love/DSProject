#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 541. 反转字符串 II https://leetcode.cn/problems/reverse-string-ii/
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n, ans = len(s), ''
        for i in range(0, n, 2 * k):
            remains = n - i
            if remains <= k:
                ans += s[i:][::-1]
            elif k < remains <= 2 * k:
                ans += s[i:i + k][::-1] + s[i + k:]
            else:
                ans += s[i:i + k][::-1] + s[i + k:i + 2 * k]
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseStr('abcd', 2))  # 'bacd'
    print(solution.reverseStr('abcdefg', 2))  # 'bacdfeg'
