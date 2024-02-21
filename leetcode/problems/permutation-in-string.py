#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 567. 字符串的排列 https://leetcode.cn/problems/permutation-in-string/
from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = 0, 0
        counter1, counter2 = Counter(), Counter()
        for c1 in s1:
            n1 += 1
            counter1.update(c1)
        left, right = 0, n1 - 1  # 定义滑动窗口的范围是 [left, right]，闭区间，长度与 s1 相等
        for c2 in s2:
            if n2 < right:
                counter2.update(c2)
            n2 += 1
        while right < n2:
            counter2[s2[right]] += 1  # 把 right 位置的元素放到 counter2 中
            if counter1 == counter2:  # 如果滑动窗口内各个元素出现的次数跟 s1 的元素出现次数完全一致，返回 True
                return True
            counter2[s2[left]] -= 1  # 窗口向右移动前，把当前 left 位置的元素出现次数 -1
            if counter2[s2[left]] == 0:
                del counter2[s2[left]]
            left, right = left + 1, right + 1  # 窗口向右移动
        return False


if __name__ == '__main__':
    obj = Solution()
    print(obj.checkInclusion('ab', 'eidbaooo'))  # True
