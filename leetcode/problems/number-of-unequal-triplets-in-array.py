# -*- coding: utf-8 -*-
# 2475. 数组中不等三元组的数目 https://leetcode.cn/problems/number-of-unequal-triplets-in-array/
from typing import List
from collections import Counter
from itertools import combinations


class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        return sum(cnt[x] * cnt[y] * cnt[z] for x, y, z in combinations(cnt, 3))


if __name__ == '__main__':
    obj = Solution()
    print(obj.unequalTriplets([4, 4, 2, 4, 3]))  # 3
