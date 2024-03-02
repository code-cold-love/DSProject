#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2368. 受限条件下可到达节点的数目 https://leetcode.cn/problems/reachable-nodes-with-restrictions/
from collections import defaultdict, deque
from typing import List


class Solution:
    @staticmethod
    def init_matrix(edges: List[List[int]]) -> defaultdict:
        """初始化邻接矩阵"""
        matrix = defaultdict(list)
        for vi, vj in edges:
            matrix[vi].append(vj)
            matrix[vj].append(vi)
        return matrix

    def reachableNodes_dfs(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        """深度优先搜索"""
        vis = set(restricted)  # 记录已经访问过的节点
        matrix = self.init_matrix(edges)

        def dfs(i: int) -> int:
            vis.add(i)
            return 1 + sum(j not in vis and dfs(j) for j in matrix[i])

        return dfs(0)

    def reachableNodes_bfs(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        """广度优先搜索"""
        q = deque([0])  # 里面只放未受限的节点
        vis = set(restricted + [0])  # 注意此处认为 0 已经被访问过了
        matrix = self.init_matrix(edges)
        ans = 0
        while q:
            i = q.popleft()
            ans += 1
            for j in matrix[i]:
                if j not in vis:
                    q.append(j)
                    vis.add(j)
        return ans


if __name__ == '__main__':
    obj = Solution()
    print(obj.reachableNodes_dfs(7, [[0, 1], [1, 2], [3, 1], [4, 0], [0, 5], [5, 6]], [4, 5]))  # 4
    print(obj.reachableNodes_bfs(7, [[0, 1], [1, 2], [3, 1], [4, 0], [0, 5], [5, 6]], [4, 5]))  # 4
