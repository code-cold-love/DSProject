# #!/usr/bin/env python
# -*- coding: utf-8 -*-
# 1053. 交换一次的先前排列 https://leetcode.cn/problems/previous-permutation-with-one-swap/
from typing import List


class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr)
        for i in range(n - 2, -1, -1):
            if arr[i] > arr[i + 1]:  # i 取倒序首个非递减的
                j = n - 1
                while arr[j] >= arr[i] or arr[j] == arr[j - 1]:
                    j -= 1
                arr[i], arr[j] = arr[j], arr[i]
                break
        return arr


if __name__ == '__main__':
    obj = Solution()
    print(obj.prevPermOpt1(arr=[3, 2, 1]))  # 312
