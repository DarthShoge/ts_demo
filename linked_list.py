

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def is_circular(self):
        quick_node = self.head
        slow_node = self.head
        while quick_node and quick_node.next:
            slow_node = slow_node.next
            quick_node = quick_node.next.next

            if quick_node.value == slow_node.value:
                print('THERE IS A CYCLE!')
                return True
        
        return False

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            print('first item is :'+str(new_node.value))
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        
        print('new item is :'+ str(new_node.value))
        last_node.next = new_node


ll = LinkedList()
ll.append(1)
circular_node = Node(1)
ll.append(circular_node)
ll.append(2)
ll.append(3)
ll.append(circular_node)
ll.is_circular()
