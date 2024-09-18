#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2410. 运动员和训练师的最大匹配数 https://leetcode.cn/problems/maximum-matching-of-players-with-trainers/
from typing import List


class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        # 每名运动员至多可以匹配一位训练师，每位训练师最多可以匹配一位运动员
        players.sort()
        trainers.sort()
        j, nt = 0, len(trainers)
        for i, p in enumerate(players):
            while j < nt and trainers[j] < p:
                j += 1
            if j >= nt:  # 当前（即第 i+1 个运动员）无法找到匹配的训练师
                return i
            j += 1  # 匹配一位训练师
        return len(players)  # 所有运动员都能匹配


if __name__ == '__main__':
    solution = Solution()
    print(solution.matchPlayersAndTrainers([4, 7, 9], [8, 2, 5, 8]))  # 2
    print(solution.matchPlayersAndTrainers([1, 1, 1], [10]))  # 1
