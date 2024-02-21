#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2432. 处理用时最长的那个任务的员工 https://leetcode.cn/problems/the-employee-that-worked-on-the-longest-task/
from typing import List


class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        min_id, max_time, start_time = n, 0, 0
        for user_id, leave_time in logs:
            task_time = leave_time - start_time
            if task_time > max_time:
                max_time = task_time
                min_id = user_id
            elif task_time == max_time:
                min_id = min(min_id, user_id)
            start_time = leave_time
        return min_id


if __name__ == '__main__':
    obj = Solution()
    print(obj.hardestWorker(n=10, logs=[[0, 3], [2, 5], [0, 9], [1, 15]]))  # 1
    print(obj.hardestWorker(n=26, logs=[[1, 1], [3, 7], [2, 12], [7, 17]]))  # 3
    print(obj.hardestWorker(n=2, logs=[[0, 10], [1, 20]]))  # 0
