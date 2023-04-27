# -*- coding: utf-8 -*-
# 933. 最近的请求次数 https://leetcode.cn/problems/number-of-recent-calls/
from collections import deque


class RecentCounter:

    def __init__(self):
        self.q = deque()
        self.count = 0

    def ping(self, t: int) -> int:
        self.q.append(t)
        self.count += 1
        while self.q and self.q[0] < t - 3000:
            self.q.popleft()
            self.count -= 1
        return self.count


if __name__ == '__main__':
    obj = RecentCounter()
    param_1 = obj.ping(1)
    param_2 = obj.ping(100)
    param_3 = obj.ping(3001)
    param_4 = obj.ping(3002)
    print(param_1, param_2, param_3, param_4)  # 1 2 3 3
