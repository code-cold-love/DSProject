# -*- coding: utf-8 -*-
# 1090. 受标签影响的最大值 https://leetcode.cn/problems/largest-values-from-labels/
from typing import List
from collections import Counter


class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        n = len(values)
        idx = list(range(n))
        idx.sort(key=lambda i: -values[i])
        ans = choose = 0
        cnt = Counter()
        for i in range(n):
            label = labels[idx[i]]
            if cnt[label] == useLimit:
                continue
            choose += 1
            ans += values[idx[i]]
            cnt[label] += 1
            if choose == numWanted:
                break
        return ans


if __name__ == '__main__':
    obj = Solution()
    print(obj.largestValsFromLabels([5, 4, 3, 2, 1], [1, 3, 3, 3, 2], 3, 2))
