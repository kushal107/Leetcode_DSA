def findkvalue(head,k):
    currnode = head
    len = 0
    while currnode:
        currnode = currnode.next
        len += 1
    
    place = len - k

    for _ in range(place):
        head = head.next
    
    return head.value

def findkvalueusingtwopointers(head,k):
    fast = head
    slow = head

    for _ in range(k):
        fast = fast.next
    
    while fast:
        fast = fast.next
        slow = slow.next
    
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

curr01 = head

'''while curr01:
    print(curr01.value)
    curr01 = curr01.next'''

print(findkvalue(head,2))
print(findkvalueusingtwopointers(head,2))
