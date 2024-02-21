#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 831. 隐藏个人信息 https://leetcode.cn/problems/masking-personal-information/
import re


class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            first = s[0].lower()
            last = re.search(r'\w+?(\w)@.+?$', s).group(1).lower()
            suffix = re.search(r'^\w+?@(.+?)$', s).group(1).lower()
            return first + '*****' + last + '@' + suffix
        else:
            s = re.sub(r'[\s()+-]', '', s)
            local = s[-4:]
            country = s[-13:-10]
            return '+' + len(country) * '*' + '-***-***-' + local if country else '***-***-' + local


if __name__ == '__main__':
    obj = Solution()
    print(obj.maskPII('AB@qq.com'))  # a*****b@qq.com
    print(obj.maskPII('1(234)567-890'))  # ***-***-7890
    print(obj.maskPII('86-(10)12345678'))  # +**-***-***-5678
