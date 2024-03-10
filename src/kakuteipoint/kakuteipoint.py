#!/usr/bin/env python3
# coding: utf-8

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class TrieNode:
    children: dict[str, "TrieNode"] = field(default_factory=dict)
    count: int = 0


@dataclass
class Trie:
    root: TrieNode = field(default_factory=TrieNode)

    def add(self, sentence: str):
        node = self.root
        for char in sentence:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1

    def shortest_prefix(self, sentence: str):
        node = self.root
        prefix = ""
        for char in sentence:
            if node.count == 1:
                break
            prefix += char
            node = node.children[char]
        return prefix


def shortest_prefix(sentences: list[str]) -> list[str]:
    trie = Trie()
    for s in sentences:
        trie.add(s)
    return [trie.shortest_prefix(s) for s in sentences]


def test_shortest_unique_prefix():
    test_cases = [
        {
            "input": ["abstract", "abbreviation", "abema"],
            "want": ["abs", "abb", "abe"],
        },
        {
            "input": [],
            "want": [],
        },
        {
            "input": ["apple", "apple"],
            "want": ["apple", "apple"],
        },
        {
            "input": ["short"],
            "want": ["s"],
        },
        {
            "input": ["a" * 10, "b" * 10],
            "want": ["a", "b"],
        },
        {
            "input": ["dog", "dogs", "doge"],
            "want": ["dog", "dogs", "doge"],  # これはエラーとすべきじゃないか？
        },
    ]
    for i, test_case in enumerate(test_cases):
        got = shortest_prefix(test_case["input"])
        assert got == test_case["want"]
