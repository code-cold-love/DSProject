# -*- coding: utf-8 -*-
# 460. LFU 缓存 https://leetcode.cn/problems/lfu-cache/
from typing import Optional
from collections import defaultdict


class DLinkedNode:
    # 双端链表
    def __init__(self, key: int = 0, value: int = 0):
        self.key = key
        self.value = value
        self.freq = 1  # 新书只读了一次
        self.prev = self.next = None


class LFUCache:
    def __init__(self, capacity: int):
        self.min_freq = 0
        self.capacity = capacity
        self.key_to_node = {}

        def new_node() -> DLinkedNode:
            dummy = DLinkedNode()
            dummy.next = dummy
            dummy.prev = dummy
            return dummy

        self.freq_to_dummy = defaultdict(new_node)

    @staticmethod
    def remove(node: DLinkedNode):  # 在原链表删除节点
        node.prev.next = node.next
        node.next.prev = node.prev

    @staticmethod
    def push_front(dummy: DLinkedNode, node: DLinkedNode):
        node.prev = dummy
        node.next = dummy.next
        dummy.next = node
        node.next.prev = node

    def get_node(self, key: int) -> Optional[DLinkedNode]:
        # 1. 从 dict 中找到 key 节点，并从原链表中删除
        # 2. 判断是否增加全局最小频率
        # 3. 增加 key 节点被抽中频率，并放过新频率链表首部
        if key not in self.key_to_node:
            return None
        node = self.key_to_node[key]
        self.remove(node)
        dummy = self.freq_to_dummy[node.freq]
        if dummy.prev == dummy:  # 抽出 key 节点之后，对应的频率链表为空
            del self.freq_to_dummy[node.freq]  # 移除空链表
            if self.min_freq == node.freq:  # 原频率为最小频率
                self.min_freq += 1  # 更新最小频率
        node.freq += 1  # 增加节点被抽出的频率
        self.push_front(self.freq_to_dummy[node.freq], node)  # 将抽出的节点放到更高频率链表的首部
        return node

    def get(self, key: int) -> int:
        node = self.get_node(key)
        return node.value if node else -1

    def put(self, key: int, value: int) -> None:
        node = self.get_node(key)
        if node:
            node.value = value
            return
        if len(self.key_to_node) == self.capacity:  # 原缓存达到了容量上限且此时又新增 key 节点
            dummy = self.freq_to_dummy[self.min_freq]  # key 节点对应的频率链表
            tail = dummy.prev
            del self.key_to_node[tail.key]  # 删除原缓存中 tail 记录
            self.remove(tail)  # 从频率链表中删除 tail
            if dummy.prev == dummy:  # 若移除 tail 后频率链表为空
                del self.freq_to_dummy[self.min_freq]
        self.key_to_node[key] = node = DLinkedNode(key, value)
        self.push_front(self.freq_to_dummy[1], node)
        self.min_freq = 1


if __name__ == '__main__':
    obj = LFUCache(3)
