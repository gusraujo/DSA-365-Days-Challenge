# 21. Merge Two Sorted Lists
#
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by
# splicing together the nodes of the first two lists.
#
# Return the head of the merged linked list.
#
# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
#
# Example 2:
# Input: list1 = [], list2 = []
# Output: []
#
# Example 3:
# Input: list1 = [], list2 = [0]
# Output: [0]
#
# Constraints:
# - The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# - Both list1 and list2 are sorted in non-decreasing order.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(list1: ListNode, list2: ListNode) -> ListNode:
    dummy = ListNode()  # temporary start node
    tail = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    # Append the remaining nodes
    tail.next = list1 if list1 else list2

    return dummy.next


# -------------------- Helpers for Testing --------------------

def list_to_linked(lst):
    head = ListNode(0)
    current = head
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return head.next


def linked_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


# -------------------- Tests --------------------

def test_merge_two_lists():
    l1 = list_to_linked([1, 2, 4])
    l2 = list_to_linked([1, 3, 4])
    assert linked_to_list(merge_two_lists(l1, l2)) == [1, 1, 2, 3, 4, 4]

    l1 = list_to_linked([])
    l2 = list_to_linked([])
    assert linked_to_list(merge_two_lists(l1, l2)) == []

    l1 = list_to_linked([])
    l2 = list_to_linked([0])
    assert linked_to_list(merge_two_lists(l1, l2)) == [0]

    l1 = list_to_linked([5, 6])
    l2 = list_to_linked([1, 2, 3])
    assert linked_to_list(merge_two_lists(l1, l2)) == [1, 2, 3, 5, 6]


def main():
    test_merge_two_lists()


if __name__ == "__main__":
    main()
