#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2418. 按身高排序 https://leetcode.cn/problems/sort-the-people/
from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        indices = list(range(n))
        indices.sort(key=lambda x: heights[x], reverse=True)
        res = []
        for i in indices:
            res.append(names[i])
        return res


if __name__ == '__main__':
    obj = Solution()
    print(obj.sortPeople(['Mary', 'John', 'Emma'], heights=[180, 165, 170]))  # ['Mary', 'Emma', 'John']
