#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 1146. 快照数组 https://leetcode.cn/problems/snapshot-array/
from bisect import bisect_left
from collections import defaultdict


class SnapshotArray:

    def __init__(self, length: int):
        self.cur_snap_id = 0
        self.history = defaultdict(list)

    def set(self, index: int, val: int) -> None:
        self.history[index].append((self.cur_snap_id, val))

    def snap(self) -> int:
        self.cur_snap_id += 1
        return self.cur_snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        i = bisect_left(self.history[index], (snap_id + 1,)) - 1
        return self.history[index][i][1] if i >= 0 else 0


if __name__ == '__main__':
    pass
