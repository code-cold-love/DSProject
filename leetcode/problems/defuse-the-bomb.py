#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 1652. 拆炸弹 https://leetcode.cn/problems/defuse-the-bomb/
from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        # -(n-1) <= k <= (n-1)
        n = len(code)
        ans = [0 for _ in range(n)]
        if k == 0:
            pass
        else:
            flag = 1 if k > 0 else -1
            for i in range(n):
                for j in range(1, flag * k + 1):
                    idx = (i + flag * j) % n
                    ans[i] += code[idx]
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.decrypt([1, 2, 3, 4], 0))  # [0, 0, 0, 0]
    print(solution.decrypt([2, 4, 9, 3], -2))  # [12, 5, 6, 13]
    print(solution.decrypt([5, 7, 1, 4], 3))  # [12, 10, 16, 13]
