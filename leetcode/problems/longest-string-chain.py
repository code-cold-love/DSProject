#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 1048. 最长字符串链 https://leetcode.cn/problems/longest-string-chain/
from typing import List
from collections import defaultdict


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        cnt = defaultdict(int)
        words.sort(key=len)
        res = 0
        for word in words:
            cnt[word] = 1
            for i in range(len(word)):
                prev = word[:i] + word[i + 1:]
                if prev in cnt:
                    cnt[word] = max(cnt[word], cnt[prev] + 1)
            res = max(res, cnt[word])
        return res


if __name__ == '__main__':
    obj = Solution()
    print(obj.longestStrChain(['a', 'b', 'ba', 'bca', 'bda', 'bdca']))  # 4
