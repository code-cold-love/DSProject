# -*- coding: utf-8 -*-
# 447. 回旋镖的数量 https://leetcode.cn/problems/number-of-boomerangs/
from math import dist
from typing import List
from collections import defaultdict


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ans = 0
        for p in points:  # 回旋镖可以视作一个 V 型的折线，可以枚举每个 points[i]，将其当作 V 型的拐点
            cnt = defaultdict(int)  # 设 points 中有 m 个点到 points[i] 的距离均相等
            for q in points:
                dis = dist(p, q)
                cnt[dis] += 1
            for m in cnt.values():  # # 需要从这 m 点中选出 2 个点当作回旋镖的 2 个端点，总排列数为 m*(m-1)
                ans += m * (m - 1)
        return ans


if __name__ == '__main__':
    obj = Solution()
    print(obj.numberOfBoomerangs([[1, 1]]))  # 0
    print(obj.numberOfBoomerangs([[0, 0], [1, 0], [2, 0]]))  # 2
    print(obj.numberOfBoomerangs([[1, 1], [2, 2], [3, 3]]))  # 2
