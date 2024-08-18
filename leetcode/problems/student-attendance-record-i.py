#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 551. 学生出勤记录 I https://leetcode.cn/problems/student-attendance-record-i/
class Solution:
    def checkRecord(self, s: str) -> bool:
        # s[i] 为 A、L 或 P
        return s.count('A') < 2 and 'LLL' not in s


if __name__ == '__main__':
    solution = Solution()
    print(solution.checkRecord('PPALLP'))  # True
    print(solution.checkRecord('PPALLL'))  # False
