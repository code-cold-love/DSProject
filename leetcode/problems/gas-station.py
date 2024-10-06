#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 134. 加油站 https://leetcode.cn/problems/gas-station/
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 当 gas 之和大于 cost 之和时，复制一份后最小油量不会变得更小
        # 所以从油量最低时所处的加油站出发，行驶过程中油量不会变成负数
        ans = capacity = min_capacity = 0
        for i, (g, c) in enumerate(zip(gas, cost)):
            capacity += g - c  # 在 i 处加油，然后从 i 到 i+1
            if capacity < min_capacity:
                min_capacity = capacity  # 更新最小油量
                ans = i + 1
        # 循环结束后，capacity 即为 gas 之和减去 cost 之和
        return -1 if capacity < 0 else ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))  # 3
    print(solution.canCompleteCircuit([2, 3, 4], [3, 4, 3]))  # -1
