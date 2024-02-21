#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 49. 字母异位词分组 https://leetcode.cn/problems/group-anagrams/
from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        for st in strs:
            key = ''.join(sorted(st))
            mp[key].append(st)
        return list(mp.values())


if __name__ == '__main__':
    obj = Solution()
    print(obj.groupAnagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']))  # [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
