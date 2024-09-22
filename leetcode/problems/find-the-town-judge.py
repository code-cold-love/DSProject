#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 997. 找到小镇的法官 https://leetcode.cn/problems/find-the-town-judge/
from collections import Counter
from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # 法官不会信任任何人，除了法官外的每个人都信任这位法官
        # trust[i] = [a, b] 表示编号为 a 的人信任编号为 b 的人
        out_degrees = Counter(x for x, _ in trust)
        in_degrees = Counter(y for _, y in trust)
        return next((i for i in range(1, n + 1) if out_degrees[i] == 0 and in_degrees[i] == n - 1), -1)


if __name__ == '__main__':
    solution = Solution()
    print(solution.findJudge(2, [[1, 2]]))  # 2
    print(solution.findJudge(3, [[1, 3], [2, 3]]))  # 3
    print(solution.findJudge(3, [[1, 2], [2, 3]]))  # -1
    print(solution.findJudge(3, [[1, 3], [2, 3], [3, 1]]))  # -1
