"""
This problem was asked by Google.

Given the head of a singly linked list, reverse it in-place.
"""


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def display_list(node):
    if not node:
        return
    print(node.data)
    display_list(node.next)


def reverse_linked_list(node):
    if not node.next:
        return node
    curr = node
    prev = None
    while curr:
        temp_node = curr.next
        curr.next = prev
        prev = curr
        curr = temp_node
    return prev


if __name__ == "__main__":
    head = Node(1, Node(2, Node(3, Node(4, Node(5)))))  # 1->2->3->4->5
    display_list(reverse_linked_list(head))  # 5->4->3->2->1
