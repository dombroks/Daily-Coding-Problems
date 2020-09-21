# -*- coding: utf-8 -*-
"""
This problem was asked by Google.

Suppose we represent our file system by a string in the following manner:

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

dir
    subdir1
    subdir2
        file.ext

The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext

The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.

We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).

Given a string representing the file system in the above format, return the length of the longest absolute path to a file in the abstracted file system. If there is no file in the system, return 0.

Note:

The name of a file contains at least a period and an extension.

The name of a directory or sub-directory will not contain a period.
"""

class Node:
    def __init__(self, name, pathtype):
        self.name = name
        self.type = pathtype
        self.children = list()
        self.length = len(name)
        self.max_child_length = 0

    def __repr__(self):
        return "(name={}, type={}, len={}, max_child_len={})".format(
            self.name, self.type, self.length, self.max_child_length)


def create_graph(node_list):
    if not node_list:
        return None

    parent_node = node_list[0][1]
    level = node_list[0][0]

    for index, (node_level, _) in enumerate(node_list[1:]):
        if node_level <= level:
            break
        if node_level == level + 1:
            child_node = create_graph(node_list[index + 1:])
            parent_node.children.append(child_node)
            if child_node.children or child_node.type == 'file':
                if child_node.max_child_length + child_node.length > parent_node.max_child_length:
                    parent_node.max_child_length = child_node.max_child_length + child_node.length


    return parent_node


def get_path_type(name):
    return 'file' if '.' in name else 'directory'


def get_longest_path(s):
    if not s:
        return 0

    individual_lines = s.split('\n')
    split_lines = [x.split('\t') for x in individual_lines]
    annotated_lines = [(len(x) - 1, Node(name=x[-1], pathtype=get_path_type(x[-1])))
        for x in split_lines]
    graph = create_graph(annotated_lines)

    return graph.max_child_length + graph.length if graph.max_child_length > 0 else 0


print(get_longest_path("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"))
print(get_longest_path(
    "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\t" +
    "subsubdir2\n\t\t\tfile2.ext"))
