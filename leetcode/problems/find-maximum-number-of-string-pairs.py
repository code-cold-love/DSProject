# -*- coding: utf-8 -*-
# 2744. 最大字符串配对数目 https://leetcode.cn/problems/find-maximum-number-of-string-pairs/
from typing import List


class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        # words 包含的字符串互不相同，words[i].length == 2
        ans = 0
        visited = set()
        for i, word in enumerate(words):
            if word[::-1] in visited:
                ans += 1
            visited.add(word)
        return ans


if __name__ == '__main__':
    obj = Solution()
    print(obj.maximumNumberOfStringPairs(['aa', 'ab']))  # 0
    print(obj.maximumNumberOfStringPairs(['ab', 'ba', 'cc']))  # 1
    print(obj.maximumNumberOfStringPairs(['cd', 'ac', 'dc', 'ca', 'zz']))  # 2
