#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 225. 用队列实现栈 https://leetcode.cn/problems/implement-stack-using-queues/
from collections import deque


class MyStack:
    def __init__(self):
        self.q1 = deque()  # q1 是一直有值的队列
        self.q2 = deque()  # q2 是入栈操作的辅助队列

    def push(self, x: int) -> None:
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1  # 最后将 q1 和 q2 互换

    def pop(self) -> int:
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return not self.q1


if __name__ == '__main__':
    obj = MyStack()
    obj.push(1)
    obj.push(2)
    param_2 = obj.pop()
    param_3 = obj.top()
    param_4 = obj.empty()
