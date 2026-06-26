def reverselinkedlist(head):
    prevnode = None
    currnode = head

    while currnode:
        nextnode = currnode.next
        currnode.next = prevnode
        prevnode = currnode
        currnode = nextnode

    return prevnode
    

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
head1 = head
while head1:
    print (head1.value)
    head1 = head1.next

newhead = reverselinkedlist(head)

while newhead:
    print (newhead.value)
    newhead = newhead.next




