#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 1376. 通知所有员工所需的时间 https://leetcode.cn/problems/time-needed-to-inform-all-employees/
from typing import List
from queue import Queue
from collections import defaultdict


class Solution:
    def numOfMinutes(self, n: int, head_id: int, manager: List[int], inform_time: List[int]) -> int:
        # head_id 公司总负责人
        g = defaultdict(list)
        for i in range(n):
            g[manager[i]].append(i)
        q = Queue()
        q.put((head_id, 0))  # (node, time) time 表示信息传递到 node 员工的时间
        res = 0
        while not q.empty():
            tmp_id, val = q.get()
            if len(g[tmp_id]) == 0:  # tmp_id 节点没有下属
                res = max(res, val)
            else:
                for ne in g[tmp_id]:  # 将 tmp_id 节点的下属加入队列，更新时间
                    q.put((ne, val + inform_time[tmp_id]))
        return res


if __name__ == '__main__':
    obj = Solution()
    print(obj.numOfMinutes(1, 0, [-1], [0]))  # 0
    print(obj.numOfMinutes(6, 2, [2, 2, -1, 2, 2, 2], [0, 0, 1, 0, 0, 0]))  # 1
