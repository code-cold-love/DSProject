# -*- coding: utf-8 -*-
# 14. 最长公共前缀 https://leetcode.cn/problems/longest-common-prefix/
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        s1 = min(strs)
        s2 = max(strs)
        for i, c in enumerate(s1):
            if c != s2[i]:
                return s2[:i]
        return s1

    def longestCommonPrefix_other(self, strs: List[str]) -> str:
        # 纵向扫描
        if not strs:
            return ''
        n, cnt = len(strs[0]), len(strs)
        for i in range(n):
            c = strs[0][i]
            if any(i == len(strs[j]) or strs[j][i] != c for j in range(1, cnt)):
                return strs[0][:i]
        return strs[0]


if __name__ == '__main__':
    obj = Solution()
    print(obj.longestCommonPrefix(['dog', 'racecar', 'car']))  # ''
    print(obj.longestCommonPrefix(['flower', 'flow', 'flight']))  # fl
