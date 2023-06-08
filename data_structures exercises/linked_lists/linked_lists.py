class Node:
    def __init__(self, data, next) -> None:
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print('Linked list is empty')
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> '
            itr = itr.next
        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
        return count

    def remove_at(self, target):
        index = 0
        itr = self.head
        while index < target-1:
            index +=1
            itr = itr.next
        itr.next = itr.next.next

        
if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(['banana', 'mango', 'grapes', 'orange'])
    ll.remove_at(2)
    ll.print()
    print('length:',ll.get_length())