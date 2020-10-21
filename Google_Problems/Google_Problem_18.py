# -*- coding: utf-8 -*-
"""
This problem was asked by Google.

Implement an LRU (Least Recently Used) cache. It should be able to be initialized with a cache size n, and contain the following methods:

set(key, value): sets key to value. If there are already n items in the cache and we are adding a new item, then it should also remove the least recently used item. get(key): gets the value at key. If no such key exists, return null. Each operation should run in O(1) time.
"""

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRU:
  def __init__(self,cache_size):
    self.cache_size = cache_size
    self.content = dict()
    self.head = Node(None, None)
    self.tail = Node(None, None)
    self.head.next = self.tail
    self.tail.prev = self.head
  
  def _remove(self,node):
    previous_node = node.prev
    next_node = node.next
    previous_node.next = next_node
    next_node.prev = previous_node
  
  def _add(self, node):
    previous_node = self.tail.prev
    node.next = self.tail
    node.prev = previous_node
    previous_node.next = node
    self.tail.prev = node

  def set(self,key,value):
    if key in self.content:
      node = self.content[key]
      self._remove(node)
    node = Node(key,value)
    self._add(node)
    self.content[key] = node
    if len(self.content) > self.cache_size :
      node_to_delete = self.head.next
      self._remove(node_to_delete)
      del self.content[node_to_delete.key]

  def get(self,key):
    if key in self.content:
      node = self.content[key]
      self._remove(node)
      self._add(node)
      return node.value

    return None

# Driver code
lru = LRU(3)

assert not lru.get("y")
lru.set("y",1)
assert lru.get("y") == 1
lru.set("b", 2)
lru.set("c", 3)
lru.set("d", 4)
lru.set("e", 5)
lru.set("y", 1)
assert lru.get("y") == 1
assert not lru.get("b")
assert lru.get("e") == 5
assert not lru.get("c")
