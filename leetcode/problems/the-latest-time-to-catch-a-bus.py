#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2332. 坐上公交的最晚时间 https://leetcode.cn/problems/the-latest-time-to-catch-a-bus/
from typing import List


class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        # 公交车出发的时间 buses[i] 互不相同，所有乘客到达的时间 passengers[j] 也互不相同
        # 你不能跟别的乘客同时刻到达，最早到达的乘客优先上车
        buses.sort()
        passengers.sort()
        n = len(passengers)
        # 模拟乘客上车
        j = 0
        for t in buses:
            space = capacity
            while space > 0 and j < n and passengers[j] <= t:
                j += 1
                space -= 1

        # 寻找插队时机
        j -= 1  # 这里减一是因为第 j 位乘客上车后把 j 加一了
        ans = buses[-1] if space else passengers[j]
        while j >= 0 and ans == passengers[j]:  # 往前找插队时机
            ans -= 1
            j -= 1
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.latestTimeCatchTheBus([10, 20], [2, 17, 18, 19], 2))  # 16
    print(solution.latestTimeCatchTheBus([10, 20, 30], [4, 11, 13, 19, 21, 25, 26], 2))  # 20
