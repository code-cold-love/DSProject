# -*- coding: utf-8 -*-
# 525. 连续数组 https://leetcode.cn/problems/contiguous-array/
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        count, max_window = 0, 0
        d = dict()
        d[count] = -1
        for i in range(n):
            num = nums[i]
            # count 表示从 0 到 i 之间的元素和（1 表示加一，0 表示减一）
            if num == 1:
                count += 1
            else:
                count -= 1
            if count in d:  # count_i = count_j 代表 [i...j] 之间 1 和 0 出现的次数一致
                prev_idx = d.get(count)
                max_window = max(max_window, i - prev_idx)
            else:
                d[count] = i
        return max_window


if __name__ == '__main__':
    obj = Solution()
    print(obj.findMaxLength([0, 1]))  # 2
    print(obj.findMaxLength([0, 1, 0]))  # 2
