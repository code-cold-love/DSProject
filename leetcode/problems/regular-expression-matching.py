# -*- coding: utf-8 -*-
# 10. 正则表达式匹配 https://leetcode.cn/problems/regular-expression-matching/
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        def matches(i: int, j: int) -> bool:
            if i == 0:
                return False
            elif p[j - 1] == '.':
                return True
            return s[i - 1] == p[j - 1]

        f = [[False] * (n + 1) for _ in range(m + 1)]
        f[0][0] = True
        for i in range(m + 1):  # i ~ [0, m]
            for j in range(1, n + 1):  # j ~ [1, n]
                if p[j - 1] == '*':
                    f[i][j] |= f[i][j - 2]
                    if matches(i, j - 1):
                        f[i][j] |= f[i - 1][j]
                else:
                    if matches(i, j):
                        f[i][j] |= f[i - 1][j - 1]
        return f[m][n]


if __name__ == '__main__':
    obj = Solution()
    print(obj.isMatch('aa', 'a'))  # False
    print(obj.isMatch('ab', '.*'))  # True
