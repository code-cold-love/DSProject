# -*- coding: utf-8 -*-
# 1032. 字符流 https://leetcode.cn/problems/stream-of-characters/
from typing import List


class StreamChecker:

    def __init__(self, words: List[str]):
        # 1 <= len(words) <= 2000
        # 1 <= len(words[i]) <= 200
        self.words = {}
        for word in words:
            self.words[word] = len(word)
        self.s = ''
        self.s_len = 0

    def query(self, letter: str) -> bool:
        # letter 是一个小写英文字母
        if letter in self.words:
            return True
        self.s = self.s + letter
        self.s_len += 1
        for word, word_len in self.words.items():
            if word_len > self.s_len:
                continue
            if self.s.endswith(word):
                return True
        return False


class TrieNode:
    def __init__(self):
        self.children = [None] * 26  # 当前节点的子节点
        self.is_end = False  # 当前节点是否是某个字符串的结尾

    def insert(self, word: str):
        node = self
        for char in word[::-1]:  # 反转字符串 word 后，逐个字符插入到前缀树中
            idx = ord(char) - 97  # ord('a') = 97
            if node.children[idx] is None:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        node.is_end = True  # 插入结束后，将当前节点的 is_end 标记为 True

    def search(self, word: List[str]) -> bool:
        node = self
        for char in word[::-1]:
            idx = ord(char) - 97  # ord('a') = 97
            if node.children[idx] is None:
                return False
            node = node.children[idx]
            if node.is_end:
                return True
        return False


class StreamChecker_AC:

    def __init__(self, words: List[str]):
        self.trie = TrieNode()
        self.cs = []  # 字符流
        self.limit = 201  # words 中的字符串长度不超过 200，因此查询时最多只需要遍历 200 个字符
        for word in words:
            self.trie.insert(word)

    def query(self, letter: str) -> bool:
        self.cs.append(letter)
        return self.trie.search(self.cs[-self.limit:])


if __name__ == '__main__':
    obj = StreamChecker(['cd', 'f', 'kl'])
    print(obj.query('a'))  # False
    print(obj.query('b'))  # False
    print(obj.query('c'))  # False
    print(obj.query('d'))  # True
    print(obj.query('e'))  # False
    print(obj.query('f'))  # True
    print(obj.query('g'))  # False
    print(obj.query('h'))  # False
    print(obj.query('i'))  # False
    print(obj.query('j'))  # False
    print(obj.query('k'))  # False
    print(obj.query('l'))  # True

    obj_ac = StreamChecker_AC(['cd', 'f', 'kl'])
    print(obj_ac.query('a'))  # False
    print(obj_ac.query('b'))  # False
    print(obj_ac.query('c'))  # False
    print(obj_ac.query('d'))  # True
    print(obj_ac.query('e'))  # False
    print(obj_ac.query('f'))  # True
    print(obj_ac.query('g'))  # False
    print(obj_ac.query('h'))  # False
    print(obj_ac.query('i'))  # False
    print(obj_ac.query('j'))  # False
    print(obj_ac.query('k'))  # False
    print(obj_ac.query('l'))  # True
