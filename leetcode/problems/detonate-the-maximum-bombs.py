#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2101. 引爆最多的炸弹 https://leetcode.cn/problems/detonate-the-maximum-bombs/
from collections import defaultdict, deque
from typing import List


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        # bombs[i].length == 3
        # 以炸弹为节点，炸弹之间的引爆关系为边建立一个有向图
        n = len(bombs)

        def is_connected(u: int, v: int) -> bool:
            # 判断炸弹 u 是否能引爆炸弹 v
            dx = bombs[u][0] - bombs[v][0]
            dy = bombs[u][1] - bombs[v][1]
            return bombs[u][2] ** 2 >= dx ** 2 + dy ** 2

        edges = defaultdict(list)  # 邻接表
        # 初始化引爆关系有向图
        for i in range(n):
            for j in range(n):
                if i != j and is_connected(i, j):
                    edges[i].append(j)

        ans = 0
        for i in range(n):  # 每个炸弹都分别以起点的身份遍历一次
            visited = [False] * n
            cnt = 1
            dq = deque([i])
            visited[i] = True
            while dq:  # BFS
                idx = dq.popleft()
                for jdx in edges[idx]:
                    if visited[jdx]:  # 跳过已经遍历过的
                        continue
                    cnt += 1
                    dq.append(jdx)
                    visited[jdx] = True
            ans = max(ans, cnt)
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.maximumDetonation([[2, 1, 3], [6, 1, 4]]))  # 2
    print(solution.maximumDetonation([[1, 1, 5], [10, 10, 5]]))  # 1
    print(solution.maximumDetonation([[1, 2, 3], [2, 3, 1], [3, 4, 2], [4, 5, 3], [5, 6, 4]]))  # 5
