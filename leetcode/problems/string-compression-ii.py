#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 1531. 压缩字符串 II https://leetcode.cn/problems/string-compression-ii/
class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        # 连续出现的字母压缩后的长度
        calc = lambda x: 1 if x == 1 else (2 if x < 10 else (3 if x < 100 else 4))

        n = len(s)
        f = [[10 ** 9] * (k + 1) for _ in range(n + 1)]  # f[i][j] 表示原串 s 的前 i 个字符，删除其中 j 个字符后，可以得到的最小压缩串的长度
        f[0][0] = 0

        for i in range(1, n + 1):
            for j in range(min(k, i) + 1):
                if j > 0:
                    f[i][j] = f[i - 1][j - 1]
                same = diff = 0
                for i0 in range(i, 0, -1):
                    if s[i0 - 1] == s[i - 1]:
                        same += 1
                        f[i][j] = min(f[i][j], f[i0 - 1][j - diff] + calc(same))
                    else:
                        diff += 1
                        if diff > j:
                            break
        return f[n][k]


if __name__ == '__main__':
    obj = Solution()
    print(obj.getLengthOfOptimalCompression('aabbaa', 2))  # 2
    print(obj.getLengthOfOptimalCompression('aaabcccd', 2))  # 4
