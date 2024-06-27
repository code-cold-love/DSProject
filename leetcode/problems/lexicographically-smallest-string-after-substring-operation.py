#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2734. 执行子串操作后的字典序最小字符串 https://leetcode.cn/problems/lexicographically-smallest-string-after-substring-operation/
class Solution:
    def smallestString(self, s: str) -> str:
        # 被替换的子串不能包含 a
        # 从左到右找到第一个不等于 a 的字符 s[i]，然后从 i 开始直到遍历结束或者遇到了 a
        l = list(s)
        for i, c in enumerate(l):
            if c == 'a':
                continue
            for j in range(i, len(l)):
                if l[j] == 'a':
                    break
                l[j] = chr(ord(l[j]) - 1)
            return ''.join(l)
        l[-1] = 'z'  # 所有字符均为 a
        return ''.join(l)


if __name__ == '__main__':
    solution = Solution()
    print(solution.smallestString('cbabc'))  # 'baabc'
    print(solution.smallestString('acbbc'))  # 'abaab'
