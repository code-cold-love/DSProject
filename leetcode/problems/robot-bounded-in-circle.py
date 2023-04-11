# -*- coding: utf-8 -*-
# 1041. 困于环中的机器人 https://leetcode.cn/problems/robot-bounded-in-circle/
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        idx = 0
        x, y = 0, 0
        for instruction in instructions:
            if instruction == 'G':
                x += direction[idx][0]
                y += direction[idx][1]
            elif instruction == 'L':
                idx -= 1
                idx %= 4
            else:
                idx += 1
                idx %= 4
        return idx != 0 or (x == 0 and y == 0)


if __name__ == '__main__':
    obj = Solution()
    print(obj.isRobotBounded('GG'))  # False
    print(obj.isRobotBounded('GL'))  # True
    print(obj.isRobotBounded('GGLLGG'))  # True
