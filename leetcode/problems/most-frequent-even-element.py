# -*- coding: utf-8 -*-
# 2404. 出现最频繁的偶数元素 https://leetcode.cn/problems/most-frequent-even-element/
from math import inf
from typing import List
from collections import defaultdict, Counter


class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        max_freq = 0
        for i in nums:
            if i & 1 == 0:  # n & 1：n 为奇数得 1，n 为偶数得 0
                counter[i] += 1
                max_freq = max(max_freq, counter[i])
        if not counter:
            return -1
        ans = inf
        for val, freq in counter.items():
            if freq == max_freq:
                ans = min(ans, val)
        return ans

    def mostFrequentEven_1(self, nums: List[int]) -> int:
        cnt = Counter(x for x in nums if x % 2 == 0)
        if not cnt:
            return -1
        max_cnt = max(cnt.values())
        return min(x for x, c in cnt.items() if c == max_cnt)


if __name__ == '__main__':
    obj = Solution()
    print(obj.mostFrequentEven([0, 1, 4, 4, 2, 2, 1]))  # 2
