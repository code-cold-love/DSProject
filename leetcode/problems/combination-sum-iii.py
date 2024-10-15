#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 216. 组合总和 III https://leetcode.cn/problems/combination-sum-iii/
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # 找到所有相加之和为 n 的 k 个数的组合,每个数字最多使用一次
        ans, path = [], []

        def backtrack(target: int, k: int, cnt: int, start: int):
            # 剪枝操作
            if cnt > target:
                return

            # 终止条件
            if len(path) == k:  # 已经取完了 k 个元素
                if cnt == target:
                    ans.append(path[:])
                return

            # 单层搜索过程
            for i in range(start, 9 + 1):
                cnt += i
                path.append(i)
                backtrack(target, k, cnt, i + 1)
                cnt -= i  # 回溯
                path.pop()  # 回溯

        backtrack(n, k, 0, 1)
        return ans


if __name__ == "__main__":
    print(Solution().combinationSum3(3, 7))  # [[1, 2, 4]]
