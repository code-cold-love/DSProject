#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 383. 赎金信 https://leetcode.cn/problems/ransom-note/
from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine = Counter(magazine)
        for letter in ransomNote:
            if magazine.get(letter):
                magazine[letter] -= 1
            else:
                return False
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.canConstruct('a', 'b'))  # False
    print(solution.canConstruct('aa', 'ab'))  # False
    print(solution.canConstruct('aa', 'aab'))  # True
