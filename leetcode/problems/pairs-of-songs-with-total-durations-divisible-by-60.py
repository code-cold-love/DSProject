#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 1010. 总持续时间可被 60 整除的歌曲 https://leetcode.cn/problems/pairs-of-songs-with-total-durations-divisible-by-60/
from typing import List
from collections import Counter


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        cnt = Counter()
        ans = 0
        for t in time:
            t %= 60
            x = (60 - t) % 60
            ans += cnt[x]
            cnt[t] += 1
        return ans


if __name__ == '__main__':
    obj = Solution()
    print(obj.numPairsDivisibleBy60([60, 60, 60]))  # 3
    print(obj.numPairsDivisibleBy60([30, 20, 150, 100, 40]))  # 3
