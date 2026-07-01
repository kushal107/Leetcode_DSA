class Node:
    def __init__(self,value):
        self.next = None
        self.value = value

one = Node(1)
two = Node(2)
three = Node(3)

one.next = two
two.next = three

head = one
head1 = one

while head:
    print (head.value)
    head = head.next

#reverse this linked list

prev = None
curr = head1

while curr:
    nextnode = curr.next
    curr.next = prev
    prev = curr
    curr = nextnode

print('\n ==========REVERSE============')
while prev:
    print(prev.value)
    prev = prev.next

