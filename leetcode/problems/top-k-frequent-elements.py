#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 347. 前 K 个高频元素 https://leetcode.cn/problems/top-k-frequent-elements/
from collections import Counter
from heapq import heappush, heappushpop
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        heap = []  # 小顶堆
        for num, freq in cnt.items():
            if len(heap) < k:  # 堆还没满
                heappush(heap, (freq, num))
                # heappush(heap, item) 中 item 可以是元组，按第一个元素排序
            elif freq > heap[0][0]:  # 当前元素的频率高于堆顶元素的频率
                heappushpop(heap, (freq, num))
        return [num for freq, num in heap]


if __name__ == '__main__':
    solution = Solution()
    print(solution.topKFrequent([1], 1))
    print(solution.topKFrequent([1, 1, 1, 2, 2, 3], 2))  # [1, 2]
