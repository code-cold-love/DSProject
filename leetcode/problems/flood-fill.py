#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 733. 图像渲染 https://leetcode.cn/problems/flood-fill/
from typing import List


class Solution:
    def floodFill_dfs(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        source_color = image[sr][sc]

        def dfs(x: int, y: int):
            if image[x][y] == source_color:
                image[x][y] = color
                for mx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                    if 0 <= mx < m and 0 <= ny < n and image[mx][ny] == source_color:
                        dfs(mx, ny)

        if source_color != color:
            dfs(sr, sc)
        return image


if __name__ == '__main__':
    obj = Solution()
    print(obj.floodFill_dfs([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))
