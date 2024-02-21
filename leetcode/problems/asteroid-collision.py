#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 735. 行星碰撞 https://leetcode.cn/problems/asteroid-collision/
from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for aster in asteroids:
            alive = True  # 当前行星是否爆炸
            while alive and aster < 0 and st and st[-1] > 0:
                alive = st[-1] < -aster
                if st[-1] <= -aster:
                    st.pop()
            if alive:
                st.append(aster)
        return st


if __name__ == '__main__':
    obj = Solution()
    print(obj.asteroidCollision([5, 10, -5]))  # [5, 10]
    print(obj.asteroidCollision([-10, 10, -5]))  # [-10, 10]
