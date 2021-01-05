"""
This problem was asked by Microsoft.

Let's represent an integer in a linked list format by having each node represent a digit in the number. The nodes make up the number in reversed order.

For example, the following linked list:

1 -> 2 -> 3 -> 4 -> 5

is the number 54321.

Given two linked lists in this format, return their sum in the same linked list format.

For example, given

9 -> 9

5 -> 2

return 124 (99 + 25) as:

4 -> 2 -> 1

"""


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def _linked_list_to_value(head):
    if head is None:
        return
    value = ""
    current = head
    while current:
        value += "".join(str(current.val))
        current = current.next
    return int(value[::-1])


def _value_to_linked_list(value):
    value = str(value)[::-1]
    head = Node(value[0])
    for i in range(len(value)):
        if i == 0:
            pass
        else:
            _append_node(head, value[i])
    return head


def _append_node(head, value):
    current = head
    while current:
        if current.next is None:
            current.next = Node(value)
            break
        current = current.next


def display_linked_list(head):
    if not head:
        return
    print(head.val)
    display_linked_list(head.next)


def two_sum(head, head2):
    value = _linked_list_to_value(head) + _linked_list_to_value(head2)
    return _value_to_linked_list(value)


# Driver code
linked_list_1 = Node(9, Node(9))
linked_list_2 = Node(5, Node(2))
display_linked_list(two_sum(linked_list_1, linked_list_2))
