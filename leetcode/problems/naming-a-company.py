#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2306. 公司命名 https://leetcode.cn/problems/naming-a-company/
from collections import defaultdict
from itertools import combinations
from typing import List


class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        # ideas[i] 由小写英文字母组成，ideas 中的所有字符串互不相同
        # 按照首字母分组
        groups = defaultdict(set)
        for word in ideas:
            groups[word[0]].add(word[1:])

        ans = 0
        for a, b in combinations(groups.values(), 2):
            # combinations 返回一个迭代器，该迭代器产生输入可迭代对象中所有长度为 r 的组合。组合是无序的，即不考虑元素的顺序
            union = len(a & b)  # 两个字符串交集的大小
            ans += (len(a) - union) * (len(b) - union)
        return ans * 2  # 考虑到两个字符串的先后顺序


if __name__ == '__main__':
    solution = Solution()
    print(solution.distinctNames(['lack', 'back']))  # 0
    print(solution.distinctNames(['coffee', 'donuts', 'time', 'toffee']))  # 6
