# This is for a linked list structure
from node import Node

"""
File: a5.py
Assignment 5

Define a length function.
Define a printStructure function.
Define an insert function.
Test the above functions and the Node class.
"""


def length(head):
    """Returns the number of items in the linked structure
    referred to by head."""
    probe = head
    count = 0

    while probe:
        count += 1
        probe = probe.next

    # ADD CODE HERE: Count the number of nodes in the structure

    return count


def insert(newItem, head):
    """Inserts newItem at the correct position (ascending order) in
    the linked structure referred to by head.
    Returns a reference to the new structure."""

    new_head = Node(newItem)

    if head is None:
        head = new_head
        return head
    else:
        if head.data.lower() >= new_head.data.lower():
            new_head.next = head
            head = new_head
            return head
        else:
            current_head = head
            while current_head.next is not None and current_head.next.data.lower() < new_head.data.lower():
                next_head = current_head.next
                current_head = next_head

        new_head.next = current_head.next
        current_head.next = new_head
        return head

    # if structure is empty
    # ADD CODE HERE
    # else:
    # Insert newItem in its place (ascending order)
    # ADD CODE HERE


def printStructure(head):
    """Prints the items in the structure referred to by head."""
    probe = head
    while probe is not None:
        print('' + str(probe.data), end=' ')
        probe = probe.next
    print()
    # ADD CODE HERE


def main():
    """Gets words from the user and inserts in the
    structure referred to by head."""

    head = None
    while True:
        userInput = input('Please enter a word (or just hit enter to end): ')
        if userInput == '':
            break
        head = insert(userInput, head)

    print('The structure contains', length(head), 'items:')
    printStructure(head)


if __name__ == "__main__": main()
