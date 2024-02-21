#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 365. 水壶问题 https://leetcode.cn/problems/water-and-jug-problem/
from math import gcd


class Solution:
    def canMeasureWater(self, jug1_capacity: int, jug2_capacity: int, target_capacity: int) -> bool:
        """深度优先搜索"""
        stack = [(0, 0)]
        seen = set()  # 哈希集合，存储已经搜索过的 remain_x, remain_y 状态
        while stack:
            remain_x, remain_y = stack.pop()  # X 和 Y 壶中的水量
            if remain_x == target_capacity or remain_y == target_capacity or remain_x + remain_y == target_capacity:
                return True
            elif (remain_x, remain_y) in seen:
                continue
            seen.add((remain_x, remain_y))

            stack.append((jug1_capacity, remain_y))  # 把 X 壶灌满
            stack.append((remain_x, jug2_capacity))  # 把 Y 壶灌满
            stack.append((0, remain_y))  # 把 X 壶倒空
            stack.append((remain_x, 0))  # 把 Y 壶倒空
            stack.append((remain_x - min(remain_x, jug2_capacity - remain_y),
                          remain_y + min(remain_x, jug2_capacity - remain_y)))  # 把 X 壶中的水灌进 Y 壶，直到灌满或倒空
            stack.append((remain_x + min(remain_y, jug1_capacity - remain_x),
                          remain_y - min(remain_y, jug1_capacity - remain_x)))  # 把 Y 壶中的水灌进 X 壶，直到灌满或倒空
        return False

    def canMeasureWater_opt(self, jug1_capacity: int, jug2_capacity: int, target_capacity: int) -> bool:
        """数学"""
        if jug1_capacity + jug2_capacity < target_capacity:
            return False
        elif jug1_capacity == 0 or jug2_capacity == 0:
            return target_capacity == 0 or jug1_capacity + jug2_capacity == target_capacity
        return target_capacity % gcd(jug1_capacity, jug2_capacity) == 0


if __name__ == '__main__':
    obj = Solution()
    print(obj.canMeasureWater(3, 5, 4))  # True
    print(obj.canMeasureWater(2, 6, 5))  # False
    print(obj.canMeasureWater(1, 2, 3))  # True
