#!/usr/bin/env python3
# coding: utf-8

from __future__ import annotations

from .kakuteipoint import shortest_unique_prefix

sentences = open(0).read().splitlines()
result = shortest_unique_prefix(sentences)
print("\n".join(result))
