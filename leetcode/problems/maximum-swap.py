# -*- coding: utf-8 -*-
# 670. 最大交换 https://leetcode.cn/problems/maximum-swap/
from typing import List


class Solution:
    def maximumSwap(self, num: int) -> int:
        num_list = [int(i) for i in str(num)]
        n = len(num_list)
        ans = num
        for i in range(n - 1):
            c = num_list[i]
            max_idx, max_val = i, c
            for j in range(i + 1, n):
                t = num_list[j]
                if t >= max_val:
                    max_idx, max_val = j, t
            if max_val > c:
                num_list[i] = max_val
                num_list[max_idx] = c
                ans = int(''.join(map(str, num_list)))
                break
        return ans


if __name__ == '__main__':
    obj = Solution()
    print(obj.maximumSwap(2736))  # 7236
    print(obj.maximumSwap(9973))  # 9973
    print(obj.maximumSwap(1993))  # 9913
