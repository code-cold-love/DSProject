#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 299. 猜数字游戏 https://leetcode.cn/problems/bulls-and-cows/
from collections import defaultdict


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # len(secret) == len(guess)
        ans, cnt_s, cnt_g = "", defaultdict(int), defaultdict(int)
        bulls, cows = 0, 0
        for s, g in zip(secret, guess):
            cnt_s[s] += 1
            cnt_g[g] += 1
            if s == g:
                bulls += 1
        cows = sum(min(cnt_s[k], cnt_g[k]) for k in cnt_s.keys())
        cows -= bulls
        return f"{bulls}A{cows}B"


if __name__ == "__main__":
    obj = Solution()
    print(obj.getHint("1807", "7810"))  # "1A3B"
    print(obj.getHint("1123", "0111"))  # "1A1B"
