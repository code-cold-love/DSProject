# -*- coding: utf-8 -*-
# 1927. 求和游戏 https://leetcode.cn/problems/sum-game/
class Solution:
    # 数学推理
    # 策略 1：Alice 使左边尽可能地大，Bob 使左边尽可能地小
    # 策略 2：Alice 使右边尽可能地大，Bob 使右边尽可能地小
    def sumGame(self, num: str) -> bool:
        length = len(num)
        if length % 2 != 0:
            return False
        mid = length // 2
        left_sum = right_sum = 0
        left_mark = right_mark = 0  # 左半段、右半段中的 ? 数量
        for i in range(mid):
            if num[i] == '?':
                left_mark += 1
            else:
                left_sum += int(num[i])
            j = i + mid
            if num[j] == '?':
                right_mark += 1
            else:
                right_sum += int(num[j])
        if left_mark == 0 and right_mark == 0:
            return False if left_sum == right_sum else True
        elif (left_mark + right_mark) % 2:  # 总的问号数量为奇数，代表最后一次轮到 Alice
            return True
        else:
            return False if left_sum - right_sum + 9 * (left_mark - right_mark) // 2 == 0 else True


if __name__ == '__main__':
    obj = Solution()
    print(obj.sumGame('25??'))  # True
    print(obj.sumGame('5023'))  # False
    print(obj.sumGame('?3295???'))  # False
