# -*- coding: utf-8 -*-
# 2451. 差值数组不同的字符串 https://leetcode.cn/problems/odd-string-difference/
from typing import List


class Solution:
    def oddString(self, words: List[str]) -> str:
        def get(word: str):
            n = len(word)
            diff = [0] * (n - 1)
            for i in range(n - 1):
                diff[i] = ord(word[i + 1]) - ord(word[i])
            return diff

        diff0 = get(words[0])
        diff1 = get(words[1])
        if diff0 == diff1:
            for ele in words[2:]:
                if diff0 != get(ele):
                    return ele
        else:
            diff2 = get(words[2])
            return words[1] if diff0 == diff2 else words[0]


if __name__ == '__main__':
    obj = Solution()
    print(obj.oddString(['adc', 'wzy', 'abc']))  # abc
