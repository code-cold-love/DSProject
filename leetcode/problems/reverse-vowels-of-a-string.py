#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 345. 反转字符串中的元音字母 https://leetcode.cn/problems/reverse-vowels-of-a-string/
class Solution:
    def reverseVowels(self, s: str) -> str:
        # 元音字母包括 a e i o u
        def is_vowel(c: str) -> bool:
            return c in 'aeiouAEIOU'

        n, s = len(s), list(s)
        i, j = 0, n - 1
        while i < j:
            while i < n and not is_vowel(s[i]):
                i += 1
            while j > 0 and not is_vowel(s[j]):
                j -= 1
            if i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        return ''.join(s)


if __name__ == '__main__':
    obj = Solution()
    print(obj.reverseVowels('hello'))  # holle
    print(obj.reverseVowels('leetcode'))  # leetcode
