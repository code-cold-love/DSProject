# -*- coding: utf-8 -*-
# 83. 删除排序链表中的重复元素 https://leetcode.cn/problems/remove-duplicates-from-sorted-list/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, _next=None):
        self.val = val
        self.next = _next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        slow = head
        fast = head.next
        while slow and fast:
            if slow.val == fast.val:
                slow.next = fast.next
                fast = fast.next
            else:
                slow = slow.next
                fast = fast.next
        return head


if __name__ == '__main__':
    obj = Solution()
    node = ListNode(1)
    node.next = ListNode(1)
    node.next.next = ListNode(2)
    node.next.next.next = ListNode(3)
    node.next.next.next.next = ListNode(3)
    node = obj.deleteDuplicates(node)
    ret = []
    while node:
        ret.append(node.val)
        node = node.next
    print(ret)
