"""
This problem was asked by Google.

Given k sorted singly linked lists, write a function to merge all the lists into one sorted singly linked list.
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


elements = []


def _get_linked_list_elements(node):
    if not node:
        return
    elements.append(node.data)
    _get_linked_list_elements(node.next)


def merge(all_lists):
    for sll in all_lists:
        _get_linked_list_elements(sll)

    elements.sort()
    head = Node(elements[0])
    for i in range(1, len(elements)):
        new_node = Node(elements[i])
        _append_node(head, new_node)

    return head


def _append_node(node, new_node):
    current = node
    while current.next:
        current = current.next
    current.next = new_node


if __name__ == "__main__":
    singly_linked_list1 = Node(1, Node(2, Node(3, Node(4))))
    singly_linked_list2 = Node(5, Node(7, Node(11, Node(21))))
    singly_linked_list3 = Node(12, Node(13, Node(17, Node(19))))
    all_linked_lists = [singly_linked_list1, singly_linked_list2, singly_linked_list3]
    display_list(merge(all_linked_lists))
