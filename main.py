

# Given a linked list, rotate the list to the right by k places, where k is non-negative.


class ListNode:
    """Definition for a singly-linked list node."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def rotateRight(head, k):
    """
    Figure out if a rotation is needed
    Compute the length of the list
    """
    if head and head.next and k != 0:
        pass
    else:
        return head

   
#    calculates the length of the linked list and ensures the current pointer ends at the last node of the list
    length = 1
    current = head
    while current.next:
        current = current.next
        length += 1

    k %= length
    if k == 0:
        return head  # No rotation needed if k is a multiple of length

    new_tail_position = length - k - 1
    new_tail = head
    for _ in range(new_tail_position):
        new_tail = new_tail.next

    new_head = new_tail.next

  
    current.next = head 
    new_tail.next = None  

    return new_head


def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def print_linked_list(head):
    values = []
    while head:
        values.append(str(head.val))
        head = head.next
    print("->".join(values))



head = create_linked_list([1, 2, 3, 4, 5])
k = 2
rotated_head = rotateRight(head, k)
print_linked_list(rotated_head)
