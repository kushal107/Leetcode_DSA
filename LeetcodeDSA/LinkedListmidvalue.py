def findmidvalue(head):
    #find the length of the linked list
    len = 0
    current_node = head

    while current_node.next:
        len += 1
        current_node = current_node.next
    current_node = head

    for _ in range(len//2):
        current_node = current_node.next
    
    return current_node.value

#using the fast and slow pointers
def findmidvalueslowfast(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow.value


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)

one.next = two
two.next = three
three.next = four
four.next = five

head = one
middle_value = findmidvalue(head)
print(middle_value)

mid_val = findmidvalueslowfast(head)
print(mid_val)


