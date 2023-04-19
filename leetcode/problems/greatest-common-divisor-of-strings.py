# -*- coding: utf-8 -*-
# 1071. 字符串的最大公因子 https://leetcode.cn/problems/greatest-common-divisor-of-strings/
from math import gcd


class Solution:
    def gcdOfStrings_enumeration(self, str1: str, str2: str) -> str:
        # 1 <= len(str1), len(str2) <= 1000
        # str1 和 str2 由大写英文字母组成
        n1, n2 = len(str1), len(str2)
        for i in range(min(n1, n2), 0, -1):
            if n1 % i == 0 and n2 % i == 0:
                if str1[:i] * (n1 // i) == str1 and str1[:i] * (n2 // i) == str2:
                    return str1[:i]
        return ''

    def gcdOfStrings_optimization(self, str1: str, str2: str) -> str:
        """枚举优化"""
        n1, n2 = len(str1), len(str2)
        candidate_len = gcd(n1, n2)
        candidate = str1[:candidate_len]
        if candidate * (n1 // candidate_len) == str1 and candidate * (n2 // candidate_len) == str2:
            return candidate
        return ''

    def gcdOfStrings_math(self, str1: str, str2: str) -> str:
        n1, n2 = len(str1), len(str2)
        candidate_len = gcd(n1, n2)
        candidate = str1[:candidate_len]
        if str1 + str2 == str2 + str1:
            return candidate
        return ''


if __name__ == '__main__':
    obj = Solution()
    print(obj.gcdOfStrings_enumeration('LEET', 'CODE'))  # ''
    print(obj.gcdOfStrings_enumeration('ABCABC', 'ABC'))  # 'ABC'
    print(obj.gcdOfStrings_enumeration('ABA', 'ABAABA'))  # 'ABA'
