#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 3106. 满足距离约束且字典序最小的字符串 https://leetcode.cn/problems/lexicographically-smallest-string-after-operations-with-constraint/
class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        if k == 0:
            return s

        s = list(s)
        distance = 0
        for i, c in enumerate(map(ord, s)):
            for j in range(26):
                new_c = ord('a') + j
                tmp = abs(c - new_c)
                if c >= new_c:
                    tmp = min(tmp, new_c + 26 - c)
                else:
                    tmp = min(tmp, c + 26 - new_c)
                if distance + tmp <= k:
                    s[i] = chr(new_c)
                    distance += tmp
                    break
        return ''.join(s)


if __name__ == '__main__':
    solution = Solution()
    print(solution.getSmallestString("lol", 0))  # "lol"
    print(solution.getSmallestString("zbbz", 3))  # "aaaz"
    print(solution.getSmallestString("xaxcd", 4))  # "aawcd"
