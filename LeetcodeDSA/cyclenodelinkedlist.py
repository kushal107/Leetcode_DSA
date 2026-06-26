class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

#solution using hashmap/set
def hascycle(head):
    seen = set()
    currnode = head
    while currnode:
        if currnode in seen:
            return True
        seen.add(currnode)
        currnode = currnode.next
    return False  
  
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

fast = head
slow = head
counter = 0

while (fast and fast.next) :
    fast = fast.next.next
    slow = slow.next
    if fast == slow:
        break

if fast == slow:
    print('Cycle')
else:
    print('No cycle')

print(hascycle(head))





