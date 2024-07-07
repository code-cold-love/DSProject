#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 438. 找到字符串中所有字母异位词 https://leetcode.cn/problems/find-all-anagrams-in-a-string/
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # 字母异位词长度一致
        ans = []
        s_len, p_len = len(s), len(p)
        if s_len < p_len:
            return ans
        s_count, p_count = [0] * 26, [0] * 26
        for i in range(p_len):
            s_count[ord(s[i]) - 97] += 1
            p_count[ord(p[i]) - 97] += 1
        if s_count == p_count:
            ans.append(0)

        for i in range(s_len - p_len):
            s_count[ord(s[i]) - 97] -= 1
            s_count[ord(s[i + p_len]) - 97] += 1
            if s_count == p_count:
                ans.append(i + 1)

        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.findAnagrams('abab', 'ab'))  # [0, 1, 2]
    print(solution.findAnagrams('cbaebabacd', 'abc'))  # [0, 6]
