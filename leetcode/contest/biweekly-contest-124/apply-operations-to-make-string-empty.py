#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 3039. 进行操作使字符串为空 https://leetcode.cn/problems/apply-operations-to-make-string-empty/
from collections import Counter


class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        counter = Counter(s)
        max_freq = max(counter.values())
        ans = []
        for c in s[::-1]:  # 保留频率最高且最后出现的字母，逆序遍历
            if counter[c] == max_freq:
                ans.append(c)
                counter[c] -= 1
        return ''.join(ans[::-1])


if __name__ == '__main__':
    obj = Solution()
    print(obj.lastNonEmptyString("abcd"))  # abcd
    print(obj.lastNonEmptyString("aabcbbca"))  # ba
