#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 1700. 无法吃午餐的学生数量 https://leetcode.cn/problems/number-of-students-unable-to-eat-lunch/
from collections import Counter
from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # len(students) == len(sandwiches)
        # students[i]、sandwiches[i] 要么是 0，要么是 1
        counter = Counter(students)
        for i, sandwich in enumerate(sandwiches):
            if counter[sandwich] == 0:  # 栈顶的面包种类没有学生种类与之匹配
                return counter[0] + counter[1]
            counter[sandwich] -= 1
        return 0


if __name__ == '__main__':
    solution = Solution()
    print(solution.countStudents([1, 1, 0, 0], [0, 1, 0, 1]))  # 0
    print(solution.countStudents([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1]))  # 3
