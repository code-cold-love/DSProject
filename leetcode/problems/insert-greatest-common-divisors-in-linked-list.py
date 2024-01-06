# -*- coding: utf-8 -*-
# 2807. 在链表中插入最大公约数 https://leetcode.cn/problems/insert-greatest-common-divisors-in-linked-list/
from math import gcd
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, _next=None):
        self.val = val
        self.next = _next


class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            cur = head
            while cur.next:
                cur.next = ListNode(gcd(cur.val, cur.next.val), cur.next)
                cur = cur.next.next
        return head


if __name__ == '__main__':
    obj = Solution()
    node = ListNode(18)
    node.next = ListNode(6)
    node.next.next = ListNode(10)
    node.next.next.next = ListNode(3)
    new_node = obj.insertGreatestCommonDivisors(node)
    ans = []
    while new_node:
        ans.append(new_node.val)
        new_node = new_node.next
    print(ans)  # [18, 6, 6, 2, 10, 1, 3]
