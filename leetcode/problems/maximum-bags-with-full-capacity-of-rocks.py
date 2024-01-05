# -*- coding: utf-8 -*-
# 2279. 装满石头的背包的最大数量 https://leetcode.cn/problems/maximum-bags-with-full-capacity-of-rocks/
from typing import List
from bisect import bisect_right
from itertools import accumulate


class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additional_rocks: int) -> int:
        n = 0
        for i, r in enumerate(rocks):
            n += 1
            capacity[i] -= r  # 在原数组基础上操作，减少空间复杂度
        capacity.sort()
        i = bags = 0
        while i < n and additional_rocks > 0:
            curr_rocks = min(capacity[i], additional_rocks)
            capacity[i] -= curr_rocks
            additional_rocks -= curr_rocks
            if capacity[i] == 0:
                bags += 1
            i += 1
        return bags

    def maximumBags_opt(self, capacity: List[int], rocks: List[int], additional_rocks: int) -> int:
        arr = list(accumulate(sorted(x - y for x, y in zip(capacity, rocks))))
        return bisect_right(arr, additional_rocks)


if __name__ == '__main__':
    obj = Solution()
    print(obj.maximumBags([10, 2, 2], [2, 2, 0], 100))  # 3
    print(obj.maximumBags([2, 3, 4, 5], [1, 2, 4, 4], 2))  # 3
