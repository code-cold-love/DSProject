#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 682. 棒球比赛 https://leetcode.cn/problems/baseball-game/
from typing import List


class Solution:
    # 返回记录中所有得分的总和
    def calPoints(self, operations: List[str]) -> int:
        # ops[i] 为 "C"、"D"、"+"，或者一个表示整数的字符串
        ans = 0
        points = []
        for op in operations:
            if op == '+':
                pt = points[-1] + points[-2]
            elif op == 'D':
                pt = points[-1] * 2
            elif op == 'C':
                ans -= points.pop()
                continue
            else:
                pt = int(op)
            ans += pt
            points.append(pt)
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.calPoints(['1']))  # 1
    print(solution.calPoints(['5', '2', 'C', 'D', '+']))  # 30
