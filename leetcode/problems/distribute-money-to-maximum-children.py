#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2591. 将钱分给最多的儿童 https://leetcode.cn/problems/distribute-money-to-maximum-children/
class Solution:
    def distMoney(self, money: int, children: int) -> int:
        # 每个儿童至少获得 1 美元，没有人获得 4 美元
        if money < children:  # 每人至少 1 美元
            return -1
        elif money > 8 * children:  # 超过 8 倍，则最少一人获得超过 8 美元，其余人都是 8 美元
            return children - 1
        elif money == 8 * children - 4:  # 若一个人获得 4 美元，其余人都是 8 美元，则需要挑一个获得 8 美元的人出来
            return children - 2
        return (money - children) // 7  # money - 8 * x >= children - x


if __name__ == '__main__':
    obj = Solution()
    print(obj.distMoney(20, 3))  # 1
    print(obj.distMoney(16, 2))  # 2
