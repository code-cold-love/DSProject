# -*- coding: utf-8 -*-
# 739. 每日温度 https://leetcode.cn/problems/daily-temperatures/
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        idx_stk = []
        for i in range(n - 1):
            while idx_stk and temperatures[idx_stk[-1]] < temperatures[i]:
                idx = idx_stk.pop()
                answer[idx] = i - idx
            idx_stk.append(i)
        while idx_stk and temperatures[idx_stk[-1]] < temperatures[-1]:
            idx = idx_stk.pop()
            answer[idx] = n - 1 - idx
        return answer


if __name__ == '__main__':
    obj = Solution()
    print(obj.dailyTemperatures([30, 60, 90]))  # [1, 1, 0]
    print(obj.dailyTemperatures([30, 40, 50, 60]))  # [1, 1, 1, 0]
    print(obj.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))  # [1, 1, 4, 2, 1, 1, 0, 0]
