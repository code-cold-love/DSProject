#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 520. 检测大写字母 https://leetcode.cn/problems/detect-capital/
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        lower = word.lower()
        upper = word.upper()
        if upper == word or lower == word:
            return True
        elif word[0].isupper() and word[1:].islower():
            return True
        else:
            return False


if __name__ == '__main__':
    obj = Solution()
    print(obj.detectCapitalUse("USA"))  # True
    print(obj.detectCapitalUse("FlaG"))  # False
