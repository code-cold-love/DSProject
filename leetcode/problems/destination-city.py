#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 1436. 旅行终点站 https://leetcode.cn/problems/destination-city/
from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # path[i] = [cityAi, cityBi] 表示从 cityAi 直接前往 cityBi
        # 题目数据保证线路图会形成一条不存在循环的线路，因此恰有一个旅行终点
        inset = set()
        outset = set()
        for a, b in paths:
            outset.discard(a)  # a 一定不是答案
            # discard(element) 方法当元素不存在时，不会引发错误，集合保持不变
            # remove(element) 方法如果指定的元素不在集合中，会引发 KeyError 错误
            if b not in inset:  # b 可能是答案
                outset.add(b)
            inset.add(a)
        return outset.pop()


if __name__ == '__main__':
    solution = Solution()
    print(solution.destCity([['A', 'Z']]))  # 'Z'
    print(solution.destCity([['London', 'New York'], ['New York', 'Lima'], ['Lima', 'Sao Paulo']]))  # Sao Paulo
