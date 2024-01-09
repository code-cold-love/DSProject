# -*- coding: utf-8 -*-
# 128. 最长连续序列 https://leetcode.cn/problems/longest-consecutive-sequence/
from typing import List
from collections import defaultdict


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = ans = 0
        counter = defaultdict(int)
        for num in nums:
            n += 1
            counter[num] += 1
        for key in counter.keys():  # 遍历哈希表
            window = 1
            tmp = key + 1
            while window <= n:
                if counter.get(tmp):
                    window += 1
                    tmp += 1
                else:
                    ans = max(ans, window)
                    break
        return ans

    def longestConsecutive_opt(self, nums: List[int]) -> int:
        max_window = 0
        nums = set(nums)
        counter = defaultdict(int)  # 哈希表存储每个端点值对应的连续区间的长度
        for num in nums:
            if counter.get(num):  # 若数已在哈希表中，则跳过
                continue
            left_window = counter[num - 1]  # 左边相邻数已有的连续区间长度
            right_window = counter[num + 1]  # 右边相邻数已有的连续区间长度
            cur_window = left_window + right_window + 1  # 当前数的区间长度
            max_window = max(max_window, cur_window)

            # 更新两端点的长度值
            counter[num] = cur_window
            counter[num - left_window] = cur_window
            counter[num + right_window] = cur_window
        return max_window


if __name__ == '__main__':
    obj = Solution()
    print(obj.longestConsecutive([100, 4, 200, 1, 3, 2]))  # 4
    print(obj.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # 9
    print(obj.longestConsecutive_opt([100, 4, 200, 1, 3, 2]))  # 4
    print(obj.longestConsecutive_opt([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # 9
