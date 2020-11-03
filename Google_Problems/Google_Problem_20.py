# -*- coding: utf-8 -*-
"""
This problem was asked by Google.

Implement a file syncing algorithm for two computers over a low-bandwidth network. What if we know the files in the two computers are mostly the same?
"""

# Credit : Vineet John


import hashlib

m = hashlib.md5


class MerkleNode:
    def __init__(self):
        self.parent = None
        self.node_hash = None


class MerkleDirectory(MerkleNode):
    def __init__(self):
        MerkleNode.__init__(self)
        self.children = list()
        self.is_dir = True

    def recalculate_hash(self):
        if self.children:
            collated_hash = ""
            for child in self.children:
                collated_hash = child.node_hash
            self.node_hash = m(collated_hash.encode()).hexdigest()


class MerkleFile(MerkleNode):
    def __init__(self):
        MerkleNode.__init__(self)
        self.node_contents = None
        self.is_dir = False

    def update_contents(self, new_contents):
        self.node_hash = m(new_contents.encode()).hexdigest()
        self.node_contents = new_contents
        if self.parent:
            self.parent.recalculate_hash()

    def add_to_directory(self, dir_node):
        self.parent = dir_node
        dir_node.children.append(self)

        while dir_node:
            dir_node.recalculate_hash()
            dir_node = dir_node.parent

a_1 = MerkleFile()
b_1 = MerkleDirectory()
a_1.update_contents("abc")
a_1.add_to_directory(b_1)
a_1.update_contents("abcd")

a_2 = MerkleFile()
b_2 = MerkleDirectory()
a_2.update_contents("abc")
a_2.add_to_directory(b_2)
