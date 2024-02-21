#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 1657. 确定两个字符串是否接近 https://leetcode.cn/problems/determine-if-two-strings-are-close/
from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        return set(word1) == set(word2) and sorted(Counter(word1).values()) == sorted(Counter(word2).values())


if __name__ == '__main__':
    obj = Solution()
    print(obj.closeStrings(word1='abc', word2='bca'))  # True
    print(obj.closeStrings(word1='cabbba', word2='abbccc'))  # True
