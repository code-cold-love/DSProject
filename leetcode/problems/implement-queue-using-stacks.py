#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 232. 用栈实现队列 https://leetcode.cn/problems/implement-queue-using-stacks/
class MyQueue:
    def __init__(self):
        self.stk1 = []  # 输入栈
        self.stk2 = []  # 输出栈

    def push(self, x: int) -> None:
        self.stk1.append(x)

    def move(self):
        # 在输出栈为空时，将输入栈的内容移到输出栈中
        if not self.stk2:
            while self.stk1:
                self.stk2.append(self.stk1.pop())

    def pop(self) -> int:
        self.move()
        return self.stk2.pop()

    def peek(self) -> int:
        self.move()
        return self.stk2[-1]

    def empty(self) -> bool:
        return not self.stk1 and not self.stk2


if __name__ == '__main__':
    # Your MyQueue object will be instantiated and called as such:
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    obj.push(3)
    obj.push(4)
    print(obj.pop())  # 1
    obj.push(5)
    print(obj.pop())  # 2
    print(obj.pop())  # 3
    print(obj.pop())  # 4
    print(obj.pop())  # 5
