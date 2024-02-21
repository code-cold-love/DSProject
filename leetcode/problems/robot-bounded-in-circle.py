#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 1041. 困于环中的机器人 https://leetcode.cn/problems/robot-bounded-in-circle/
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        idx = 0
        pos = [0, 0]
        for instruction in instructions:
            if instruction == 'G':
                pos[0] += direction[idx][0]
                pos[1] += direction[idx][1]
            elif instruction == 'L':
                idx -= 1
                idx %= 4
            else:
                idx += 1
                idx %= 4
        return idx != 0 or (pos[0] == 0 and pos[1] == 0)


if __name__ == '__main__':
    obj = Solution()
    print(obj.isRobotBounded('GG'))  # False
    print(obj.isRobotBounded('GL'))  # True
    print(obj.isRobotBounded('GGLLGG'))  # True
