# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head or not head.next:
            return
        
        # Step 1: Find the middle of the list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half of the list
        prev = None
        current = slow
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        # Step 3: Merge the two halves
        first, second = head, prev
        while second.next:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            
            first = temp1
            second = temp2

# Helper function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Helper function to convert a linked list to a list of values for easy comparison
def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Test the solution
def test_solution():
    solution = Solution()

    # Test case 1
    head1 = create_linked_list([1, 2, 3, 4])
    solution.reorderList(head1)
    print(linked_list_to_list(head1))  # Expected output: [1, 4, 2, 3]

    # Test case 2
    head2 = create_linked_list([1, 2, 3, 4, 5])
    solution.reorderList(head2)
    print(linked_list_to_list(head2))  # Expected output: [1, 5, 2, 4, 3]

# Run the tests
test_solution()
