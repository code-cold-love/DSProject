# -*- coding: utf-8 -*-
# 2788. 按分隔符拆分字符串 https://leetcode.cn/problems/split-strings-by-separator/
from typing import List


class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        words = [w for word in words for w in word.split(separator) if w]
        return words


if __name__ == '__main__':
    obj = Solution()
    print(obj.splitWordsBySeparator(['one.two.three', 'four.five', 'six'], '.'))
