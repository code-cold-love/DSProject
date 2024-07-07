#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 242. 有效的字母异位词 https://leetcode.cn/problems/valid-anagram/
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


if __name__ == '__main__':
    solution = Solution()
    print(solution.isAnagram('rat', 'car'))  # False
    print(solution.isAnagram('anagram', 'nagaram'))  # True
