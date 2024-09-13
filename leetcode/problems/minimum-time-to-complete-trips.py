#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2187. 完成旅途的最少时间 https://leetcode.cn/problems/minimum-time-to-complete-trips/
from typing import List


class Solution:
    def minimumTime_brute(self, time: List[int], totalTrips: int) -> int:
        t, n = 1, len(time)
        while True:
            trips = [t // time[i] for i in range(n)]
            if sum(trips) >= totalTrips:
                return t
            t += 1

    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        # 返回完成至少 totalTrips 趟旅途需要花费的最少时间
        # 时间越多，可以完成的旅途也就越多，有单调性
        min_t = min(time)
        left = min_t - 1  # 这个时间任何车都没法完成一趟旅途
        right = totalTrips * min_t  # 答案不可能超过让最快的车跑全部趟的时间
        f = lambda x: sum(x // t for t in time)
        while left + 1 < right:
            mid = (left + right) // 2
            if f(mid) >= totalTrips:
                right = mid
            else:
                left = mid
        return right


if __name__ == '__main__':
    solution = Solution()
    print(solution.minimumTime([2], 1))  # 2
    print(solution.minimumTime([1, 2, 3], 5))  # 3
