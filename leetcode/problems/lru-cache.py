# -*- coding: utf-8 -*-
# 146. LRU 缓存 https://leetcode.cn/problems/lru-cache/
class DLinkedNode:
    # 双端链表
    def __init__(self, key: int = 0, value: int = 0):
        self.key = key
        self.value = value
        self.prev = self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = dict()
        self.head = DLinkedNode()  # 伪头部
        self.tail = DLinkedNode()  # 伪尾部
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0  # 当前容量

    def add_to_head(self, node: DLinkedNode):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    @staticmethod
    def remove_node(node: DLinkedNode):
        node.prev.next = node.next
        node.next.prev = node.prev

    def move_to_head(self, node: DLinkedNode):
        self.remove_node(node)  # 先在原位置删除节点
        self.add_to_head(node)

    def remove_tail(self) -> DLinkedNode:
        node = self.tail.prev
        self.remove_node(node)
        return node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.move_to_head(node)
        else:
            node = DLinkedNode(key, value)
            self.cache[key] = node
            self.add_to_head(node)
            self.size += 1
            if self.size > self.capacity:
                removed_node = self.remove_tail()
                self.cache.pop(removed_node.key)
                self.size -= 1


if __name__ == '__main__':
    obj = LRUCache(3)
