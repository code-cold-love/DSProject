#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 3211. 生成不含相邻零的二进制字符串 https://leetcode.cn/problems/generate-binary-strings-without-adjacent-zeros/
from typing import List


class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans = []
        if not (1 <= n <= 18):
            return ans
        path = [''] * n

        def backtrack(i: int, end: int) -> None:
            if i == end:  # 终止条件
                ans.append(''.join(path))
                return

            path[i] = '1'  # 当前位填 1
            backtrack(i + 1, end)

            if i == 0 or path[i - 1] == '1':  # 这两种情况下可以填 0
                path[i] = '0'  # 原位覆盖实现回溯
                backtrack(i + 1, end)

        backtrack(0, n)
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.validStrings(1))  # ['1', '0']
    print(solution.validStrings(3))  # ['111', '110', '101', '011', '010']
