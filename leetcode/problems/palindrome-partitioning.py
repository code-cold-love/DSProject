#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 131. 分割回文串 https://leetcode.cn/problems/palindrome-partitioning/
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        path = []

        def backtrack(start: int):
            if start == len(s):  # 终止条件
                ans.append(path[:])  # 存放结果
                return
            for i in range(start + 1, len(s) + 1):  # 选择本层集合中元素
                sub = s[start: i]  # 截取的子串
                if self.is_palindrome(sub):
                    path.append(sub)  # 处理节点
                    backtrack(i)  # 递归
                    path.pop()  # 回溯，撤销处理结果

        backtrack(0)
        return ans

    @staticmethod
    def is_palindrome(s: str) -> bool:
        n = len(s)
        return all(s[i] == s[n - 1 - i] for i in range(n // 2))


if __name__ == '__main__':
    obj = Solution()
    print(obj.partition('a'))  # [['a']]
    print(obj.partition('aab'))  # [['a', 'a', 'b'], ['aa', 'b']]
