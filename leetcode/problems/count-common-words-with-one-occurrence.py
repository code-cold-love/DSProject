# -*- coding: utf-8 -*-
# 2085. 统计出现过一次的公共字符串 https://leetcode.cn/problems/count-common-words-with-one-occurrence/
from typing import List
from collections import Counter


class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        counter_1, counter_2 = Counter(words1), Counter(words2)
        ans = 0
        for w in counter_1.keys():
            if counter_1[w] == 1 and counter_2[w] == 1:
                ans += 1
        return ans


if __name__ == '__main__':
    obj = Solution()
    print(obj.countWords(['b', 'bb', 'bbb'], ['a', 'aa', 'aaa']))  # 0
    print(obj.countWords(['leetcode', 'is', 'amazing', 'as', 'is'], ['amazing', 'leetcode', 'is']))  # 2
