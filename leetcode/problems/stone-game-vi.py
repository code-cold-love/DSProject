#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 1686. 石子游戏 VI https://leetcode.cn/problems/stone-game-vi/
from typing import List


class Solution:
    def stoneGameVI(self, alice_values: List[int], bob_values: List[int]) -> int:
        total_values = [[a + b, a, b] for a, b in zip(alice_values, bob_values)]
        total_values.sort(key=lambda x: x[0], reverse=True)
        alice_sum = sum(value[1] for value in total_values[::2])
        bob_sum = sum(value[2] for value in total_values[1::2])
        if alice_sum > bob_sum:
            return 1
        elif alice_sum == bob_sum:
            return 0
        else:
            return -1


if __name__ == '__main__':
    obj = Solution()
    print(obj.stoneGameVI([1, 3], [2, 1]))  # 1
    print(obj.stoneGameVI([1, 2], [3, 1]))  # 0
    print(obj.stoneGameVI([2, 4, 3], [1, 6, 7]))  # -1
