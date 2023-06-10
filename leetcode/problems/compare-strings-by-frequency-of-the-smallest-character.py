# -*- coding: utf-8 -*-
# 1170. 比较字符串最小字母出现频次 https://leetcode.cn/problems/compare-strings-by-frequency-of-the-smallest-character/
from typing import List
from bisect import bisect


class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def sum_frequency(s: str):
            mina = s[0]
            suma = 1
            for c in s[1:]:
                if c < mina:
                    mina = c
                    suma = 1
                elif c == mina:
                    suma += 1
            return suma

        q = [sum_frequency(word) for word in queries]
        w = [sum_frequency(word) for word in words]
        n = len(w)
        w.sort()
        ret = []
        for i in q:
            ret.append(n - bisect(w, i))
        return ret


if __name__ == '__main__':
    obj = Solution()
    print(obj.numSmallerByFrequency(['cbd'], ['zaaaz']))  # [1]
    print(obj.numSmallerByFrequency(['bbb', 'cc'], ['a', 'aa', 'aaa', 'aaaa']))  # [1, 2]
