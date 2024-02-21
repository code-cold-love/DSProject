#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 649. Dota2 参议院 https://leetcode.cn/problems/dota2-senate/
from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        radiant, dire = deque(), deque()
        for i, ch in enumerate(senate):
            if ch == 'R':
                radiant.append(i)
            else:
                dire.append(i)
        del senate

        while radiant and dire:
            if radiant[0] < dire[0]:
                radiant.append(radiant[0] + n)
            else:
                dire.append(dire[0] + n)
            radiant.popleft()
            dire.popleft()
        return 'Radiant' if radiant else 'Dire'


if __name__ == '__main__':
    obj = Solution()
    print(obj.predictPartyVictory('RD'))  # Radiant
    print(obj.predictPartyVictory('RDD'))  # Dire
