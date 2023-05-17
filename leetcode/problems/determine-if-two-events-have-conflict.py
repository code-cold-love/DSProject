# -*- coding: utf-8 -*-
# 2446. 判断两个事件是否存在冲突 https://leetcode.cn/problems/determine-if-two-events-have-conflict/
from typing import List


class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        return not(event1[1] < event2[0] or event2[1] < event1[0])


if __name__ == '__main__':
    obj = Solution()
    print(obj.haveConflict(['01:15', '02:00'], ['02:00', '03:00']))  # True
