#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2073. 买票需要的时间 https://leetcode.cn/problems/time-needed-to-buy-tickets/
from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # 0 <= k < len(tickets) <= 100
        ans, idx = 0, 0
        n = len(tickets)
        while True:
            if tickets[idx] > 0:
                tickets[idx] -= 1
                ans += 1
                if idx == k and tickets[idx] == 0:
                    break
            idx = (idx + 1) % n
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.timeRequiredToBuy([2, 3, 2], 2))  # 6
    print(solution.timeRequiredToBuy([5, 1, 1, 1], 0))  # 8
