# -*- coding: utf-8 -*-
# 876. 链表的中间结点 https://leetcode.cn/problems/middle-of-the-linked-list/
class ListNode:
    def __init__(self, val=0, _next=None):
        self.val = val
        self.next = _next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


if __name__ == '__main__':
    obj = Solution()
    node = ListNode(val=1)
    node.next = ListNode(2)
    node.next.next = ListNode(3)
    node.next.next.next = ListNode(4)
    node.next.next.next.next = ListNode(5)
    new_node = obj.middleNode(node)
    print(new_node.val)
