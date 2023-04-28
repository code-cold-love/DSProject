# -*- coding: utf-8 -*-
# 328. 奇偶链表 https://leetcode.cn/problems/odd-even-linked-list/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, _next=None):
        self.val = val
        self.next = _next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        even_head = head.next
        odd, even = head, even_head
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head


if __name__ == '__main__':
    obj = Solution()
