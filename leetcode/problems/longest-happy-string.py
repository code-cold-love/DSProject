#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 1405. 最长快乐字符串 https://leetcode.cn/problems/longest-happy-string/
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        n, ans = 0, []
        cnt = [[a, 'a'], [b, 'b'], [c, 'c']]
        while True:
            cnt.sort(key=lambda x: -x[0])  # 当前数量最多的字母排在最前面
            flag = False
            for i, (f, c) in enumerate(cnt):  # 尽可能优先使用当前数量最多的字母
                if f <= 0:
                    break
                elif n >= 2 and ans[-2] == c and ans[-1] == c:
                    continue  # 加入当前字母会导致出现三个连续相同字母，则跳过
                flag = True
                n += 1
                ans.append(c)
                cnt[i][0] -= 1
                break
            if flag is False:  # 如果尝试所有的字母都无法添加，则直接退出
                return ''.join(ans)


if __name__ == '__main__':
    obj = Solution()
    print(obj.longestDiverseString(2, 2, 1))  # aabbc
    print(obj.longestDiverseString(7, 1, 0))  # aabaa
    print(obj.longestDiverseString(1, 1, 7))  # ccaccbcc
