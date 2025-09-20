class Node:
    def __init__(self, d):
        self.data = d
        self.add = None  

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.add is not None:
                temp = temp.add
            temp.add = new_node
    def reversek(self, head, k):
        prev = None
        curr = head
        next = None
        count = 0
        while curr is not None and count < k:
            next = curr.add
            curr.add = prev
            prev = curr
            curr = next
            count += 1
        if next is not None:
            head.add = self.reversek(next, k)
        return prev 
    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data,end=" ")
            if temp.add is not None:
                print("->",end=" ")
            temp = temp.add
        print()
n = int(input("Enter the number of nodes:"))
llist = LinkedList()
print()
for i in range(n):
    data = int(input("Enter the elements:"))
    llist.append(data)
print()
k = int(input("Enter the value of k:"))
print()
llist.head = llist.reversek(llist.head, k)
print("Output: ",end=" ")
llist.printlist()