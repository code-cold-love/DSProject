#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 3216. 交换后字典序最小的字符串 https://leetcode.cn/problems/lexicographically-smallest-string-after-a-swap/

class Solution:
    def getSmallestString(self, s: str) -> str:
        s = list(s)
        for i in range(1, len(s)):
            x, y = s[i - 1], s[i]
            if x > y and ord(x) % 2 == ord(y) % 2:
                s[i - 1], s[i] = y, x
                break
        return ''.join(s)


if __name__ == '__main__':
    solution = Solution()
    print(solution.getSmallestString("001"))  # "001"
    print(solution.getSmallestString("45320"))  # "43520"
