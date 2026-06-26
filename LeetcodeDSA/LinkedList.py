class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
one = Node(1)
two = Node(2)
three = Node(3)

one.next = two
two.next = three

head1 = one

print(head1.value)
print(head1.next.value)
print(head1.next.next.value)

def getsum(head):
    ans = 0
    while head:
        ans = ans + head.value
        head = head.next
    return ans

x = getsum(head1)
print(f"Sum = {x}")

class DoubleNode:
    def __init__(self,value1):
        self.value = value1
        self.next = None
        self.prev = None

 