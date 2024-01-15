# -*- coding: utf-8 -*-
# 82. 删除排序链表中的重复元素 II https://leetcode.cn/problems/remove-duplicates-from-sorted-list-ii/
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
        dummy = ListNode(0, head)
        curr = dummy
        while curr.next and curr.next.next:
            if curr.next.val == curr.next.next.val:
                tmp = curr.next.val
                while curr.next and curr.next.val == tmp:
                    curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy.next


if __name__ == '__main__':
    obj = Solution()
    node = ListNode(1)
    node.next = ListNode(1)
    node.next.next = ListNode(1)
    node.next.next.next = ListNode(2)
    node.next.next.next.next = ListNode(3)
    node = obj.deleteDuplicates(node)
    ret = []
    while node:
        ret.append(node.val)
        node = node.next
    print(ret)
