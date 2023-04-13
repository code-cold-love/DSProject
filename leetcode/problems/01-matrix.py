# -*- coding: utf-8 -*-
# 542. 01 矩阵 https://leetcode.cn/problems/01-matrix/
from typing import List
from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # mat[i][j] is either 0 or 1
        m, n = len(mat), len(mat[0])
        ans = [[0] * n for _ in range(m)]  # 构建距离矩阵
        super_zero = [(i, j) for i in range(m) for j in range(n) if mat[i][j] == 0]
        seen = set(super_zero)  # 已遍历的元素
        q = deque(super_zero)
        del super_zero
        while q:
            i, j = q.popleft()  # 取出一个值为 0 的元素
            # 遍历邻接节点
            for new_i, new_j in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= new_i < m and 0 <= new_j < n and (new_i, new_j) not in seen:
                    ans[new_i][new_j] = ans[i][j] + 1
                    q.append((new_i, new_j))
                    seen.add((new_i, new_j))
        return ans


if __name__ == '__main__':
    obj = Solution()
    print(obj.updateMatrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))  # [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
