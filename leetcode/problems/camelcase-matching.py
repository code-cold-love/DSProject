#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 1023. 驼峰式匹配 https://leetcode.cn/problems/camelcase-matching/
from typing import List


class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        # 所有字符串都仅由大写和小写英文字母组成
        n = len(queries)
        m = len(pattern)
        ans = [True] * n
        for i in range(n):
            p = 0  # pattern 下标
            for c in queries[i]:
                if p < m and pattern[p] == c:  # 下标不超过 pattern 长度
                    p += 1
                elif c.isupper():
                    ans[i] = False
                    break
            if p < m:  # pattern 中还有字符未被匹配
                ans[i] = False
        return ans


if __name__ == '__main__':
    obj = Solution()
    print(obj.camelMatch(['FooBar', 'FooBarTest', 'FootBall', 'FrameBuffer', 'ForceFeedBack'], pattern='FB'))  # [True, False, True, True, False]
